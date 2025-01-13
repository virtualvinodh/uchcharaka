<template>
    <q-collapsible :sublabel="label"
         icon="settings" dense class="q-mb-xs q-mt-xs print-hide" ref="collapse"
     >
     <span>
    <div class="col-xs-12 col-md-12 print-hide">
      <q-option-group
        color="dark"
        type="checkbox"
        inline
        class="q-ml-sm q-mt-sm print-hide"
        v-model="postOptions"
        @input="convert"
        v-if="inputScript !== 'IPA'"
        :options="postOptionList"
      />
    </div>
      <span v-if="!inaccurateScripts.includes(outputScript)">
      <div class="q-mb-md q-ml-sm q-mt-md">
        Accuracy:
        <q-radio v-model="sourcePreserve" val="Low" label="Low" class="q-mr-sm" @input="convert"/>
        <q-radio v-model="sourcePreserve" val="Medium" label="Medium" class="q-mr-sm" @input="convert" />
        <q-radio v-model="sourcePreserve" val="High" label="High" class="q-mr-sm" @input="convert"/>
      </div>
        <small><div class="q-ml-xl print-hide" v-html="preserveSourceExampleOut[outputScript]"></div></small>
      </span>
    </span>
  </q-collapsible>
</template>

<script>
import {QRadio, QTooltip, QField, QBtnToggle, QToggle, QSelect, QBtn, QOptionGroup, QSlideTransition, QCollapsible} from 'quasar'
import Transliterate from '../components/Transliterate'
import {ScriptMixin} from '../mixins/ScriptMixin'

export default {
  // name: 'ComponentName',
  mixins: [ScriptMixin],
  props: ['inputScript', 'outputScript', 'postOptionsInput', 'convertText', 'sourcePreserveInput', 'hideSourcePreserve', 'showscriptName'],
  components: {
    QRadio,
    QField,
    QBtnToggle,
    QToggle,
    QSelect,
    QBtn,
    QOptionGroup,
    QSlideTransition,
    Transliterate,
    QTooltip,
    QCollapsible
  },
  data () {
    return {
      postOptions: this.postOptionsInput,
      sourcePreserve: this.sourcePreserveInput
    }
  },
  mounted: function () {
  },
  updated: function () {
  },
  computed: {
    activeOptionsCount: function () {
      let count = 0
      if (!this.inaccurateScripts.includes(this.outputScript)) {
        count = this.postOptions.length + 1
      } else {
        count = this.postOptions.length
      }

      return count
    },
    label: function () {
      if (this.showscriptName) {
        return '<i>' + this.outputScript + ' output options (' + this.optionCount + ')</i> : ' + this.activeOptionsCount + ' active'
      } else {
        return '<i>Output options (' + this.optionCount + ')</i> : ' + this.activeOptionsCount + ' active'
      }
    },
    optionCount: function () {
      var optionCount
      if (!this.inaccurateScripts.includes(this.outputScript)) {
        optionCount = 1 + this.postOptionList.length
      } else {
        optionCount = this.postOptionList.length
      }

      return optionCount
    },
    postOptionList: function () {
      var postOptionList = [{value: 'showstress', label: 'Show stress'}]

      if (typeof this.postOptionsGroup[this.outputScript] !== 'undefined') {
        postOptionList = postOptionList.concat(this.postOptionsGroup[this.outputScript])
      }

      if (typeof this.postOptionsGroupSpecific[this.outputScript + this.inputScript] !== 'undefined') {
        postOptionList = postOptionList.concat(this.postOptionsGroupSpecific[this.outputScript + this.inputScript])
      }

      return postOptionList
    }
  },
  watch: {
    optionCount (newV, oldV) {
      if (newV === 0) {
        if (typeof this.$refs.collapse !== 'undefined') {
          this.$refs.collapse.hide()
        }
      }
    },
    postOptionsInput: function () {
      this.postOptions = this.postOptionsInput
    },
    sourcePreserveInput: function () {
      this.sourcePreserve = this.sourcePreserveInput
    }
  },
  methods: {
    convert: function () {
      this.postOptions = this.filterRadio(this.postOptions, this.outputScript)
      console.log(this.postOptions)
      console.log('Source preserve component is' + this.sourcePreserve)
      if (!this.hideSourcePreserve) {
        this.$emit('input', [this.postOptions, this.sourcePreserve])
      } else {
        this.$emit('input', this.postOptions)
      }
    }
  }
}
</script>

<style scoped>
.notice {
  color: gray;
  font-size: 12px;
}
.float-div {
  display: inline-block;
  float: left;
}
</style>
