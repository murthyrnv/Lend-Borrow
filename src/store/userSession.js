const state = {
  user: {},
  isAuthenticated: false,
  totalBorrowed: 0
}
const mutations = {
  startUserSession: (state, payload) => {
    state.user = payload
    state.isAuthenticated = true
  },
  setTotalBorrowed: (state, payload) => {
    state.totalBorrowed = payload
  }
}
const actions = {
  startUserSession ({ commit }, payload) {
    commit('startUserSession', payload)
  },
  setTotalBorrowed ({ commit }, payload) {
    commit('setTotalBorrowed', payload)
  }
}
const getters = {
  currentUser: state => {
    return state.user
  },
  isAuthenticated: state => {
    return state.isAuthenticated
  },
  totalBorrowed: state => {
    return state.totalBorrowed
  }
}
export default {
  state,
  mutations,
  getters,
  actions
}
