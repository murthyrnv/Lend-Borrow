<template>
    <div class="page">
        <div class='body'>
            <div class='form-wrapper'>
                <form>
                    <div class="title">
                        <span><img class="title_logo" src="../assets/lending.png"/>{{this.title}}</span>
                    </div>
                    <div class="field" v-if="mode=='Sign Up'">
                        <label for="name">Name</label>
                        <input type="text" name="name" id="name" v-model.trim="name" size="50">
                    </div>
                    <div class="field">
                        <label for="email">Email</label>
                        <input type="email" name="email" id="email" v-model.trim="email" size="50">
                    </div>
                    <div class="field">
                        <label for="password">Password</label>
                        <input type="password" name="password" id="password" v-model.trim="password" size="50">
                    </div>
                    <div class="btnfield">
                        <button class="loginBtn" @click.prevent="login()">
                            <span>Log in</span>
                        </button>
                    </div>
                    <div class="btnfield">
                        <button class="" @click.prevent="">
                            <span>Forgot Password?</span>
                        </button>
                    </div>
                    <!-- <hr/>
                    <div class="btnfield">
                        <button class="loginBtn" @click.prevent="validateForm()">
                            <span>Sign up</span>
                        </button>
                    </div> -->
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import cfg from '../config'
import axios from 'axios'
import { mapActions } from 'vuex'
export default {
  data () {
    return {
      email: '',
      password: '',
      name: '',
      keyFeatures: cfg.keyFeatures,
      title: cfg.title,
      mode: 'Log in'
    }
  },
  methods: {
    login () {
      // start loading
      const url = '/login'
      var credentials = btoa(this.email + ':' + this.password)
      var basicAuth = 'Basic ' + credentials
      var headers = { Authorization: basicAuth }
      axios.post(url, {}, { headers: headers })
        .then((res) => {
          if (res.data.authenticated) {
            this.startUserSession(res.data.userDetails)
            this.$router.push('/dashboard')
            axios.defaults.headers.common.Authorization = 'Bearer ' + res.data.token
          } else {
            // handle user not found case by prompting to sign up
          }
          // stop loading
        })
        .catch((error) => {
          console.log(error)
          // handle wrong password case by showing an error
          // stop loading
        })
    },
    ...mapActions([
      'startUserSession'
    ])
  }
}
</script>

<style scoped>
.page {
    display:flex;
    flex-direction: row;
}
.page::before {
  content: "";
  position: absolute;
  background-image: url("../assets/bg7.jpg");
  background-position: top;
  background-repeat: no-repeat;
  background-size: cover;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background-color: rgba(33, 30, 28, 0.03)
  /* opacity: 0.8; */
}
.loginBtn {
  background: #0066c3;
  font-size: 18px;
  font-weight: bold;
  color: #fff;
  padding: 5px 15px;
  border: 1px solid #0066c3;
  border-radius: 5px;
}
.loginBtn:hover{
  background: #025099;
}
.field {
  margin-bottom: 10px;
  font-size: 22px;
  padding: 0 8%;
  width: inherit;
}
.field input {
  width: 100%;
  border: 1.5px solid rgba(151, 151, 151, 0.6);
  height: 30px;
  margin:0 auto;
  border-radius: 5px;
  background-color: white !important;
  /* padding-left: 5px; */
}
.body {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  margin-top:10%;
}
.page-left {
  width: 50%;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top:13%;
  font-size: 30px;
  color: gray;
  font-weight: bold;
}
.form-wrapper {
  background: whitesmoke;
  position: absolute;
  width: max-content;
  /* margin: 37%; */
  max-width: fit-content;
  max-height: fit-content;
  height: fit-content;
  border-radius: 0.5rem;
  padding: 25px;
  width: 20rem;
}
.btnfield {
  text-align: center;
  padding: 0 8%;
  margin: 15px 0px;
}
.title_logo {
    height: 28px;
    vertical-align: middle;
    margin-right: 5px;
    margin-bottom: 5px;
}
.title {
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    color: green;
    font-family: 'Bahnschrift SemiBold';
    margin: 25px
}
</style>
