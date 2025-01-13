<template>
  <span>
    <div v-if="inputScript == 'IPA'" class="text-grey-7"><small>Only a subset of IPA is supported. Unsupported IPA characters will not be converted.</small></div>
    </span>
</template>

<script>
import {ScriptMixin} from '../mixins/ScriptMixin'
import Transliterate from '../components/Transliterate'

export default {
  // name: 'ComponentName',
  mixins: [ScriptMixin],
  components: {
    Transliterate
  },
  props: ['inputScript', 'outputScript', 'preOptions', 'postOptions', 'OCRPerformed'],
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
