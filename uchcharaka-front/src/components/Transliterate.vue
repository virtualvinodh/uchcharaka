<template>
  <span>
  <span :class="getOutputClass(tgt, postOptions, convertText)" v-html="convertText.replaceAll('<br/>', '. ')">
  </span>
  </span>
</template>

<script>
import {QInnerLoading, QSpinnerGears, QIcon, QBtn} from 'quasar'
import { ScriptMixin } from '../mixins/ScriptMixin'

export default {
  // name: 'ComponentName',
  mixins: [ScriptMixin],
  components: {
    QBtn,
    QInnerLoading,
    QSpinnerGears,
    QIcon
  },
  props: ['src', 'tgt', 'text', 'sourcePreserve', 'postOptions', 'preOptions'],
  mounted: function () {
    this.convert()
  },
  data () {
    return {
      convertText: '. . .',
      loading: true
    }
  },
  watch: {
    src: function () {
      this.convert()
    },
    tgt: function () {
      this.convert()
    },
    text: function () {
      this.convert()
    },
    sourcePreserve: function () {
      this.convert()
    },
    preOptions: function () {
      this.convert()
    },
    postOptions: function () {
      this.convert()
    }
  },
  methods: {
    convert: function () {
      if (this.text === '' || this.text === '. . .') {
        this.convertText = this.text
        return
      }
      var text = this.text
      var data = {
        source: this.src,
        target: this.tgt,
        text: text,
        accuracy: this.sourcePreserve,
        postOptions: typeof this['postOptions'] !== 'undefined' ? this.postOptions : [],
        preOptions: typeof this['preOptions'] !== 'undefined' ? this.preOptions : []
      }
      var dhis = this
      this.apiCall.post('/convert', data)
        .then(function (response) {
          dhis.convertText = response.data
          dhis.loading = false
        })
        .catch(function (error) {
          console.log(error)
        })
    }
  }
}
</script>

<style>
</style>
