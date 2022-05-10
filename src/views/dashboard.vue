<template>
  <div class="page">
    <div class='page-left'>
      <div class="page-left-top">
        <div class='title'><span><img class="title_logo" src="../assets/lending.png"/>Lend and Borrow</span></div>
        <div class="nav-item">
          <img class='nav-logo' src='../assets/home.png'/>
          Home
        </div>
        <div class="nav-item">
          <img class='nav-logo' src='../assets/settings.png'/>
          Settings
        </div>
        <div class="nav-item">
          <img class='nav-logo' src='../assets/logout.png' />
          Logout
        </div>
      </div>
      <div>
        <div class='page-left-bottom-title'>Borrow Status</div>
      <div class="page-left-bottom">
        <vue-ellipse-progress :progress="this.totalBorrowed">
          <span slot="legend-value">/{{this.limit}}</span>
          <!-- <p slot="legend-caption">GOOD JOB</p> -->
        </vue-ellipse-progress>
      </div>
      </div>
    </div>
    <div class='page-right'>
      <component :is="dynamicComponent"></component>
    </div>
  </div>
</template>

<script>
import home from '../components/home.vue'
import settings from '../components/settings.vue'
import { mapGetters } from 'vuex'
export default {
  data () {
    return {
      options: ['Home', 'Settings', 'Logout'],
      limit: 500
    }
  },
  computed: {
    ...mapGetters([
      'display',
      'currentUser',
      'totalBorrowed'
    ]),
    dynamicComponent () {
      var cmp = ''
      if (this.display === 0) {
        cmp = 'home'
      } else if (this.display === 1) {
        cmp = 'settings'
      }
      return cmp
    }
  },
  components: { home, settings }
}
</script>

<style>
.page {
  display: flex;
  flex-direction: row;
}
.page-left {
  display: flex;
  flex-direction: column;
  width: 20%;
  background-color: #a3c3d3;
  height: 100vh;
}
.page-right {
  width: 80%;
  background-color: #ededed;
  height: 100vh;
}
.page-left-bottom {
  display: flex;
  justify-content: center;
  border-radius: 5px;
  height: 40%;
  padding: 20px;
}
.page-left-top {
  border-radius: 5px;
  padding-top:20px;
  height: 60%;
}
.nav-item {
  cursor: pointer;
  /* text-align: center; */
  font-size: 18px;
  vertical-align: middle;
  padding: 10px 10px 10px 30px;
  border-bottom: 1px solid black;
  border-radius: 5px;;
  /* color: white; */
}
.nav-item:hover {
  background-color: rgb(141, 140, 138, 0.15);
}
.nav-logo {
  height: 18px;
}
.page-left-top span, .page-left-bottom-title {
  font-size: 22px;;
  padding-left:20px
}
.title_logo{
  height: 22px;
  margin-right:5px;
}
.title {
  margin-bottom: 15px;
}
</style>
