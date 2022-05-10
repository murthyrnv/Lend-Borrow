<template>
  <div id="app">
    <div v-if="this.isAuthenticated">
      <router-view/>
    </div>
    <div v-else>
      <Login />
    </div>
  </div>
</template>
<script>
import Login from './views/Login.vue'
import { mapGetters } from 'vuex'
export default {
  data () {
    return {
    }
  },
  name: 'app',
  components: {
    Login
  },
  computed: {
    ...mapGetters(['isAuthenticated'])
  }
}
</script>

<style>
body {
  margin: 0px;
}
</style>
