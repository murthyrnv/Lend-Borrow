import Vue from 'vue'
import userSession from './userSession'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    display: 0
  },
  mutations: {
    setDisplay: (state, payload) => {
      state.display = parseInt(payload, 10)
    }
  },
  actions: {
    setDisplay ({ commit }, payload) {
      commit('setDisplay', payload)
    }
  },
  getters: {
    display: state => {
      return state.display
    }
  },
  modules: {
    userSession
  }
})
