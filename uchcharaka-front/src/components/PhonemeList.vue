<template>
  <span class="phonelist">
    <table :style="{'border-collapse': 'collapse'}">
          <tr>
              <th>IPA</th>
              <th v-if="!inaccurateScripts.includes(script)">High</th>
              <th v-if="!inaccurateScripts.includes(script)">Medium</th>
              <th v-if="!inaccurateScripts.includes(script)">Low</th>
              <th v-if="inaccurateScripts.includes(script)"></th>
            </tr>
            <tr v-for="(data,i) in consonants" :key="i">
              <td :class="ipa">{{data.phoneme}}
                <q-btn icon="record_voice_over" flat compact class="q-ml-sm" @click="audioIPA(data.phoneme)" v-if="data.filename"/>
                <a :href="'https://en.wikipedia.org/wiki/'+data.wikilink" target="_blank" v-if="data.wikilink" class="text-grey-10"><q-icon name="link"></q-icon></a>
              </td>
              <td :class="script.toLowerCase()" v-if="!inaccurateScripts.includes(script)">
                {{consonantsMap[script]['High'][i]}}
              </td>
              <td :class="script.toLowerCase()" v-if="!inaccurateScripts.includes(script)">
                {{consonantsMap[script]['Medium'][i]}}</td>
              <td :class="script.toLowerCase()" v-if="!inaccurateScripts.includes(script)">
                {{consonantsMap[script]['Low'][i]}}
              </td>
              <td :class="script.toLowerCase()" v-if="inaccurateScripts.includes(script)">
                {{consonantsMap[script]['Low'][i]}}
              </td>
            </tr>
          </table>
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
  props: ['script', 'consonants', 'consonantsMap'],
  mounted: function () {
  },
  data () {
    return {
    }
  },
  watch: {
  },
  methods: {
    audioIPA: function (ipa) {
      let audio = document.getElementById(ipa)
      audio.play()
    }
  }
}
</script>

<style>
.phonelist {
  width: 70%; /* Optional: Set table width */
  border-collapse: collapse; /* Ensures borders don't double up */
}

.phonelist th, .phonelist td {
  text-align: center; /* Horizontal centering */
  vertical-align: middle; /* Vertical centering */
  padding: 8px; /* Optional: Add padding */
  border: 1px solid #ddd; /* Optional: Add borders */
}
</style>
