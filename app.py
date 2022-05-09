# noinspection PyInterpreter
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
# /add_transaction - it accepts ( transaction id - random hash, transaction type (borrows /lends) , transaction date- date type,, transaction status  - unpaid by default, transaction with , transaction from - creator username
# /mark_paid - it accepts transaction id  and change transaction status

if __name__ == "__main__":
    CORS(app, resources={r"/*": {"origin": "*", "supports_credentials": "true"}})
    app.run(debug=True, host="localhost", port="5000", threaded=True, processes=1)
