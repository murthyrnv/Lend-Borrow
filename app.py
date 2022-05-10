# noinspection PyInterpreter
import json
from flask import Flask, request, jsonify, session
from flask_cors import CORS
from datetime import datetime, timedelta
import config
import jwt
from dbConnection import db 
app = Flask(__name__)
FLASK_DEBUG = 1
CORS(
    app,
    resources={
        r"/*": {"origin": "*", "supports_credentials": "true"}
    },
)
app.config["SECRET_KEY"] = config.SECRET_KEY
app.config.update(SESSION_COOKIE_SAMESITE="Lax", SESSION_COOKIE_SECURE=False)
# app.config.update(SESSION_COOKIE_SAMESITE="Strict", SESSION_COOKIE_SECURE=True)


@app.route('/login', methods=['POST'])
def login():
    credentials = request.authorization
    db_con = db()
    db_con.initializeDB()
    cursor = db_con.getcursor()
    sql = "SELECT * FROM users WHERE email = ? "
    cursor.execute(sql,(credentials['username'],))
    if cursor.rowcount == 0:
        session.clear()
        return jsonify({'message': 'User not Found', 'authenticated': False}), 200
    userDetails = dict(cursor.fetchone())
    db_con.closeconn()
    if userDetails['password'] != credentials['password']:
        session.clear()
        return jsonify({'message': 'Incorrect Password', 'authenticated': False}), 401
    session['userDetails'] = userDetails
    token = jwt.encode({
        'sub': userDetails['id'],
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=config.TIME_OUT)},
        config.SECRET_KEY)
    response = {
        'token': token.decode('UTF-8'),
        'tokenCreated': datetime.utcnow(),
        'tokenExpiry': datetime.utcnow() + timedelta(minutes=config.TIME_OUT),
        'expiresIn': config.TIME_OUT,
        'userDetails': userDetails,
        'authenticated': True
    }
    return jsonify(response),200
  
# /get_transactions -  it accepts username and fetches all the transactions where user is either borrower or lender
@app.route('/get_transactions', methods=['GET'])
def get_transactions():
    totalBorrowed = 0
    totalLent = 0
    transactions = {
        'owe': [],
        'owed': []
    }
    args = request.args
    user_id = int(args["user_id"])
    db_con = db()
    db_con.initializeDB()
    cursor = db_con.getcursor()
    sql = "SELECT * FROM transactions WHERE borrowedBy = ? OR lentBy = ? "
    cursor.execute(sql,(user_id,user_id))
    if cursor.rowcount == 0: return jsonify(transactions)
    for tx in cursor.fetchall():
        if tx['lentBy'] == user_id:
            transactions['owed'].append(dict(tx))
            totalLent += tx['amount'] if tx['status'] == 0 else 0
        else:
            transactions['owe'].append(dict(tx))
            totalBorrowed += tx['amount'] if tx['status'] == 0 else 0
    db_con.closeconn()
    response = {'totalBorrowed':totalBorrowed, 'totalLent': totalLent, 'transactions': transactions}
    return jsonify(response)

@app.route('/addTransaction', methods=['POST'])
def addTransaction():
    tx = tuple(request.form.get('transaction').values())
    db_con = db()
    db_con.initializeDB()
    cursor = db_con.getcursor()
    sql = "INSERT INTO transactions(type, date,status,lentBy,borrowedBy,Reason,amount) "\
        " VALUES (?,?,?,?,?,?,?)"
    cursor.execute(sql,tx)
    db_con.closeconn()
    return 'done'

@app.route('/settleTransaction', methods=['POST'])
def addTransaction():
    txID = request.form.get('transactionID')
    db_con = db()
    db_con.initializeDB()
    cursor = db_con.getcursor()
    sql = "SELECT * FROM transactions WHERE id = ?"
    cursor.execute(sql,(txID,))
    if cursor.rowcount == 0: return jsonify('Transaction not found')
    tx = cursor.fetchone()
    lentBy = tx['lentBY']
    borrowedBy = tx['borrowedBy']
    amount = tx['amount']
    sql = 'UPDATE transactions set status = 1 WHERE id = ?'
    cursor.execute(sql,(txID,))
    sql = "UPDATE users set balance = balance + ? WHERE id = ?"
    cursor.execute(sql, (amount, borrowedBy))
    db_con.closeconn()
    return 'done'

if __name__ == "__main__":
    CORS(app, resources={r"/*": {"origin": "*", "supports_credentials": "true"}})
    app.run(debug=True, host="localhost", port="5000", threaded=True, processes=1)
