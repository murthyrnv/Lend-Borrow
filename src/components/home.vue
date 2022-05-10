<template>
  <div class='page' v-if="this.loading" >
    <div class='page-top'>
    </div>
    <div class='page-bottom' v-if="transactions.owed">
        <div class='page-bottom-left'>
            <div v-for="(tx,index) in transactions.owed" :key="index">
                <div class='txdetails'>
                    <span>{{tx.amount}}</span>
                    <span>{{tx.borrowedBy}}</span>
                    <span>on {{tx.date}} </span>
                </div>
                <div>
                    <button class="" @click.prevent="this.settle(tx.id)">
                        <span>Settle</span>
                    </button>
                </div>
            </div>
        </div>
        <div class='page-bottom-right' v-if="transactions.owe> 0">
            <div v-for="(tx,index) in transactions.owe" :key="index">
                <div class='txdetails'>
                    <span>{{tx.amount}}</span>
                    <span>{{tx.lentBy}}</span>
                    <span>on {{tx.date}} </span>
                </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex'
export default {
  data () {
    return {
      transactions: {},
      loading: false
    }
  },
  created () {
    this.getTransactions()
    this.unsubscribe = this.$store.subscribe((action, state) => {
      if (action.type === 'reloadData') {
        this.getTransactions()
      }
    })
  },
  computed: {
    ...mapGetters([
      'display',
      'currentUser'
    ])
  },
  methods: {
    getTransactions () {
      this.loading = true
      const params = new URLSearchParams()
      params.append('user_id', this.currentUser.id)
      const path = '/get_transactions'
      axios
        .get(path, {
          params: params
        })
        .then((res) => {
          this.transactions = res.data.transactions
          this.loading = false
        })
        .catch((error) => {
          console.error(error)
          this.loading = false
        })
    },
    settle () {
    }
  }
}
</script>

<style scoped>

</style>
