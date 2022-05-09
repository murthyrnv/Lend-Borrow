const state = {
  user: {},
  isAuthenticated: false
}
const mutations = {
  startUserSession: (state, payload) => {
    state.user = payload
    state.isAuthenticated = true
  }
}
const actions = {
  startUserSession ({ commit }, payload) {
    commit('startUserSession', payload)
  }
}
const getters = {
  currentUser: state => {
    return state.user
  },
  isAuthenticated: state => {
    return state.isAuthenticated
  }
}
export default {
  state,
  mutations,
  getters,
  actions
}
