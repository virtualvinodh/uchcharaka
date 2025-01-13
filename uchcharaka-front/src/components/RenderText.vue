<template>
  <div>
   <div v-if="mode == 'tooltip'" :style="{'line-height': '1.5em'}">
   <div class="q-ma-md text-grey-7" v-if="voiceName"><i>Click on the word to hear it.</i></div>
  <span v-for="(t, i) in textJSON" :key="i" class="q-mb-md">
    <span>
      <q-btn dense size="15px" class="q-ml-sm" compact flat @click="speakText(t, 0.75, voiceName)"
      :label="t" no-caps v-if="voiceName"/>
      <q-tooltip class="text-black-11" :style="{'font-size': '110%'}">
        <span :class="getOutputClass(options.script, [], convertText[i])">
          {{convertText[i]}}
        </span>
      </q-tooltip>
    </span>
  </span>
</div>
  <span v-if="mode == 'sentence'">
  <div  v-for="(t, i) in textJSON" :key="i" class="q-mb-md">
      <div class="q-mb-sm text-grey">{{t}}</div>
      <div class="text-black-11" :style="{'font-size': '110%'}">
        <q-btn icon="record_voice_over" flat class="q-mr-sm" compact @click="speakText(t, rate, voiceName)" v-if="voiceName"/>
        <span :class="getOutputClass(options.script, [], convertText[i])" v-html="convertText[i]"></span>
      </div>
  </div>
</span>
<span  v-if="mode == 'word'">
  <div class="q-ma-md text-grey-7" v-if="voiceName"><i>Click on the transcription to hear it.</i></div>
  <table>
  <tr>
    <td v-for="(t, i) in textJSON" :key="i">
    <div class="q-ma-sm">{{t }}</div>
    <div :class="getOutputClass(options.script, [], convertText[i])">
      <q-btn dense size="20px" class="q-ml-sm" compact flat @click="speakText(t, 0.75, voiceName)" :label="convertText[i]" v-if="voiceName"/>
      <q-btn dense size="20px" class="q-ml-sm" compact flat :label="convertText[i]" v-else/>
    </div>

    </td>
  </tr>
</table>
</span>
    </div>

</template>

<style scoped>
.demo {
      font-family: Arial;
  }

td {
  display: inline-block;
  padding: 10px;
}

</style>

<script>
import { ScriptMixin } from '../mixins/ScriptMixin'
import {QInnerLoading, QBtn, QTooltip, QAlert} from 'quasar'

export default {
  mixins: [ScriptMixin],
  components: {
    QAlert,
    QTooltip,
    QInnerLoading,
    QBtn
  },
  props: ['text', 'options', 'mode', 'rate', 'source', 'voiceName'],
  data () {
    return {
      convertText: [],
      textJSON: [],
      updateMenu: true,
      loading: true
    }
  },
  watch: {
    text (to, from) {
      this.renderPage()
    },
    options (to, from) {
      this.renderPage()
    }
  },
  mounted: function () {
    this.renderPage()
  },
  methods: {
    renderPage: async function () {
      let splitPattern = this.mode === 'word' || this.mode === 'tooltip' ? ' ' : /((\. )|\n)/
      this.loading = true
      this.textJSON = this.text.split(splitPattern)
      this.textJSON = this.textJSON.filter(item => item && item.trim() !== '.' && item.trim() !== ',' && item.trim() !== '' && item.trim() !== '\n')
      this.convertText = await this.convertJSONAsync(this.source, this.options.script, this.textJSON, this.options.sourcePreserve, typeof this.options['preOptions'] !== 'undefined' ? this.options.preOptions : [], typeof this.options['postOptions'] !== 'undefined' ? this.options.postOptions : [])
      this.loading = false
    }
  }
}
</script>
