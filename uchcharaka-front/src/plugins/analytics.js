import VueAnalytics from 'vue-analytics'
import router from '../router/index'

export default ({ Vue }) => {
  Vue.use(VueAnalytics, {
    id: 'UA-127048353-1',
    router
  })
}
