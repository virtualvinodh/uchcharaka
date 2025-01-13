<template>
    <q-page padding>
      <!-- <q-page-sticky position="top-right">
        <controls-plug v-model="options" :extra="false" :minimizeO="true"> </controls-plug>
      </q-page-sticky> -->
        <div class="q-body-1" :style="{'width': '100%'}">{{ about }}</div> <br/>

        <!-- <div :style="{'width': '80%'}"><transliterate :text="about" src="en-gb" :tgt="scriptRandom" :sourcePreserve="'Medium'"></transliterate></div>
        <br/> -->
        <div class="q-body-1">Uccharaka is also available as a <a href="https://pypi.org/project/uccharaka/">Python package</a>. You can read the usage instructions <a href="http://uccharaka.aksharamukha.com/python">here</a>.
        </div><br/>

        <div class="q-body-1">The source code is released under GNU AGPL and can be found in <a href="https://github.com/virtualvinodh/uchcharaka">Github</a>. Please report any bugs or suggestions over there.</div>

        <span v-if="!$q.platform.is.cordova">
        <div class="q-display-1 q-mt-lg q-mb-md">Donate</div>
        <div class="q-body-1">If you'd like to donate to support and/or appreciate the work, you can send a donation through Paypal.</div> <br/>
<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
<input type="hidden" name="cmd" value="_s-xclick" />
<input type="hidden" name="hosted_button_id" value="68RQQBSK9Z52J" />
<input type="image" src="https://www.paypalobjects.com/en_GB/i/btn/btn_donateCC_LG.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" />
<img alt="" border="0" src="https://www.paypal.com/en_IN/i/scr/pixel.gif" width="1" height="1" />
</form>
</span>

        <div class="q-display-1 q-mt-lg q-mb-md">Feedback</div>
        <div class="q-body-1">Please send your feedback/comments to vinodh@virtualvinodh.com</div>

  </q-page>
</template>

<script>
import { QTooltip, QPageSticky } from 'quasar'
import { ScriptMixin } from '../mixins/ScriptMixin'
import ControlsPlug from '../components/ControlsPlug'
import Transliterate from '../components/Transliterate'

export default {
  // name: 'PageName',
  mixins: [ScriptMixin],
  meta: {
    // meta tags
    meta: {
      description: { name: 'description', content: 'Aksharamukha' },
      keywords: { name: 'keywords', content: 'scripts, writing systems, trascription, english, indian scripts, indian languages, transliteration, unicode, conversion' }
    },

    // <noscript> tags
    noscript: {
      default: 'Aksharamukha '
    }
  },
  components: {
    QTooltip,
    ControlsPlug,
    Transliterate,
    QPageSticky
  },
  data () {
    return {
      options: {},
      about: 'The tool is designed to transcribe non-Indian languages into Indian scripts while closely preserving their native pronunciations. It offers three levels of transcription, ranging from low to high fidelity. The high-fidelity level retains as many non-Indic phonemes as possible, while the low-fidelity level captures only the essential phonetic elements. Currently, the tool supports English (US and UK), Spanish (Spain and Latin America), German, and French.'
    }
  }
}
</script>

<style scoped>
.invoc {
  display:inline;
}
.invoc-img {
  margin-top: -30px;
  display:inline-block;
}
.quote {
  text-align: left;
  margin-right: 0px;
  --q-color-primary: #777;
  font-style:italic;
  font-size:14px;
  line-height:20px;
}
.scriptlist li {
  float : left;
  margin-right: 40px;
}
</style>
