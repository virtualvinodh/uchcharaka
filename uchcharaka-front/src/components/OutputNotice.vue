<template>
  <span class="print-hide">
      <div class="notice q-ma-sm" v-show="String(convertText).includes('ॆ') || String(convertText).includes('ऎ')">ऎ कॆ should be pronounced as a short (hrasva) ए के </div>
      <div class="notice q-ma-sm" v-show="String(convertText).includes('ॊ') || String(convertText).includes('ऒ')">ऒ कॊ should be pronounced as a short (hrasva) ओ को </div>
      <div class="notice q-ma-sm" v-show="outputScript == 'Tamil'">This requires Chakreshvari Tamil Phonetic font to be installed.</div>
      <div class="notice q-ma-sm" v-show="outputScript == 'Telugu'">The font used is Tiro Telugu to ensure the correct placement of the Nukta. </div>
      <div class="notice q-ma-sm" v-show="outputScript == 'Kannada'">The font used is Tiro Kannada to ensure the correct placement of the Nukta. </div>
      <div class="notice q-ma-sm" v-show="outputScript == 'Malaylam'">The font used is Noto Sans Malayalam to support the placement of the dot below. </div>
  </span>
</template>

<script>
import {ScriptMixin} from '../mixins/ScriptMixin'

export default {
  // name: 'ComponentName',
  mixins: [ScriptMixin],
  props: ['inputScript', 'outputScript', 'postOptions', 'convertText', 'inputText'],
  data () {
    return {}
  }
}
</script>

<style scoped>
.notice {
  color: gray;
  font-size: 12px;
}
</style>
