<template>
  <div class="bg-grey-2 q-pr-md">
    <q-slide-transition>
    <div v-show="minimize">
    <q-select
        filter
        autofocus-filter
        @input="updateScript"
        filter-placeholder="search"
        v-model="outputScript"
        float-label="Guide Script"
        placeholder="Output Script"
        class="col-xs-6 col-md-6 q-ma-sm"
        :options="scriptsOutput"
      />
      <span v-if="!inaccurateScripts.includes(outputScript) && extra">
      <div class="q-mb-md q-ml-sm q-mt-md">
        <i>Accuracy</i><br/>
        <q-radio v-model="sourcePreserve" val="Low" label="Low" class="q-mr-sm q-mt-sm" @input="updateScript"/> <br/>
        <q-radio v-model="sourcePreserve" val="Medium" label="Medium" class="q-mr-sm" @input="updateScript" /><br/>
        <q-radio v-model="sourcePreserve" val="High" label="High" class="q-mr-sm" @input="updateScript"/>
      </div>
        <small><div class="q-ml-xl print-hide" v-html="preserveSourceExampleOut[outputScript]"></div></small>
      </span>
      <q-option-group
        color="dark"
        type="checkbox"
        class="q-ml-sm q-mb-sm"
        v-model="postOptions"
        @input="update"
        :options="typeof postOptionsGroup[outputScript] !== 'undefined' ? postOptionsGroup[outputScript] : []"
        v-show="typeof postOptionsGroup[outputScript] !== 'undefined'"
        v-if="extra"
      />
    </div>
    </q-slide-transition>
    <q-btn flat :icon="minimize ? 'call made' : 'call received' " @click="minimize = !minimize" color="dark"/>
    <span class = "demo"></span>

  </div>
</template>

<script>
import {QRadio, QField, QBtnToggle, QToggle, QSelect, QBtn, QOptionGroup, QSlideTransition} from 'quasar'
import {ScriptMixin} from '../mixins/ScriptMixin'

export default {
  // name: 'ComponentName',
  mixins: [ScriptMixin],
  props: ['minimizeO', 'value', 'extra'],
  components: {
    QRadio,
    QField,
    QBtnToggle,
    QToggle,
    QSelect,
    QBtn,
    QOptionGroup,
    QSlideTransition
  },
  data () {
    return {
      postOptions: [],
      minimize: this.minimizeO,
      advanced: 'false',
      outputScript: '',
      sourcePreserve: 'High'
    }
  },
  mounted: function () {
    console.log(this.value)
    this.outputScript = this.value.script
    this.update()
  },
  methods: {
    updateScript: function () {
      this.postOptions = []
      this.update()
    },
    update: function () {
      var options = {}

      this.postOptions = this.filterRadio(this.postOptions, this.outputScript)

      options['script'] = this.outputScript
      options['sourcePreserve'] = this.sourcePreserve
      options['postOptions'] = this.postOptions

      this.$emit('input', options)
    }
  }
}
</script>

<style scoped>
.demo {
  font-family: Arial;
}
</style>
