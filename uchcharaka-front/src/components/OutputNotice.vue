<template>
  <span class="print-hide">
      <div class="notice q-ma-sm" v-show="String(convertText).includes('ॆ') || String(convertText).includes('ऎ')">ऎ कॆ should be pronounced as a short (hrasva) ए के </div>
      <div class="notice q-ma-sm" v-show="String(convertText).includes('ॊ') || String(convertText).includes('ऒ')">ऒ कॊ should be pronounced as a short (hrasva) ओ को </div>
      <div class="notice q-ma-sm" v-show="outputScript == 'TamilPhonetic'">This requires <a href="https://www.virtualvinodh.com/projects/chakreshvari" target="_blank">Chakreshvari Tamil Phonetic</a> font to be installed.</div>
      <div class="notice q-ma-sm" v-show="outputScript == 'Telugu'" target="_blank"> <a href="https://fonts.google.com/specimen/Tiro+Telugu">Tiro Telugu</a> is used to ensure the correct placement of the Nukta. </div>
      <div class="notice q-ma-sm" v-show="outputScript == 'Kannada'" target="_blank"> <a href="https://fonts.google.com/specimen/Tiro+Kannada">Tiro Kannada</a> is used to ensure the correct placement of the Nukta. </div>
      <div class="notice q-ma-sm" v-show="outputScript == 'Malayalam'" target="_blank">The font used is <a href="https://fonts.google.com/noto/specimen/Noto+Sans+Malayalam">Noto Sans Malayalam</a> to support the placement of the dot below. </div>
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
