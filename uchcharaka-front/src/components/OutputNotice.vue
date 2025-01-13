<template>
  <span class="print-hide">
      <div class="notice q-ma-sm" v-show="String(convertText).includes('ॆ') || String(convertText).includes('ऎ')">ऎ कॆ should be pronounced as a short (hrasva) ए के </div>
      <div class="notice q-ma-sm" v-show="String(convertText).includes('ॊ') || String(convertText).includes('ऒ')">ऒ कॊ should be pronounced as a short (hrasva) ओ को </div>
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
