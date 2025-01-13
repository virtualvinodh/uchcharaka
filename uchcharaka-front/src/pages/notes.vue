<template>
    <q-page padding>
      <q-page-sticky position="top-right">
        <controls-plug v-model="options" :extra="false" :minimizeO="true"> </controls-plug>
      </q-page-sticky>
      <p class="q-display-1">Notes</p>
      <p class="q-display-1">English</p>
      <p class="q-body-3">
      <b>Phonetic Simplifications</b>
    </p>
    <p class="q-body-1">
     Indian English frequently simplifies English phonology by mapping non-native sounds to their closest Indian sounds, as many English sounds simply do not exist in Indian languages. For instance, the consonants /t/ and /d/ are almost always realized as retroflex sounds <transliterate text="/ʈ/ /ɖ/" src="IPA" :tgt="options.script" sourcePreserve="high"></transliterate> by Indian speakers. But they are actually alveolar sounds <transliterate text="/t/ /d/" src="IPA" :tgt="options.script" sourcePreserve="high"></transliterate> (that many Indian languages lack). Similarly, the words /this/ and /three/ are often realized using dental plosives as <transliterate text="/d̪ɪs/ /t̪ɾiː/" src="IPA" :tgt="options.script" sourcePreserve="high"></transliterate>, when they should ideally be realized using fricatives as /<transliterate text="this" src="en-gb" :tgt="options.script" sourcePreserve="high"></transliterate>/ /<transliterate text="three" src="en-gb" :tgt="options.script" sourcePreserve="high"></transliterate>/. On the same note, Indian english rarely differentiates /v/ and /w/ and both of them are merged into the Indian phoneme /ʋ/. As a result of this, a word like /wavy/ <transliterate text="wavy" src="en-UK" :tgt="options.script" sourcePreserve="high"></transliterate> becomes <transliterate text="ʋeːʋɪ" src="IPA" :tgt="options.script" sourcePreserve="high"></transliterate>. English /r/ is also typically a postalveolar approximant /<transliterate text="ɹ" src="IPA" :tgt="options.script" sourcePreserve="high"></transliterate>/, while an Indian speaker might typically use a tap /<transliterate text="ɾ" src="IPA" :tgt="options.script" sourcePreserve="high"></transliterate>/ or even a trill /<transliterate text="r" src="IPA" :tgt="options.script" sourcePreserve="high"></transliterate>/.
    </p>
    <p class="q-body-1">
       Indian languages are usually used to only two diphthongs <transliterate text="əɪ əʊ" src="IPA" :tgt="options.script" sourcePreserve="high"></transliterate>.  Even those are now-a-days realized as <transliterate text="əj əʋ" src="IPA" :tgt="options.script" sourcePreserve="high"></transliterate> in South India and are monopthongized in North India. In English, many sounds heard/realized as single vowels [by Indians] are actually two vowels pronounced in quick succession. For example:  break coke grown :: <transliterate text="break coke grown" src="en-us" :tgt="options.script" sourcePreserve="high"></transliterate>. These are often monophthongized in Indian English as <transliterate text="bɾeːk koːk ɡɾoːn" src="IPA" :tgt="options.script" sourcePreserve="low"></transliterate>.
    </p>
    <p class="q-body-3">
      <b>Spelling Pronunciation</b>
    </p>
    <p class="q-body-1">
     Indian English is rife with spelling pronunciations. For instance, /wednesday/ should actually be realized as <transliterate text="wednesday" src="en-UK" :tgt="options.script" sourcePreserve="high"></transliterate> but is often pronounced as <transliterate text="ʋɛɖneːsɖeː" src="IPA" :tgt="options.script" sourcePreserve="high"></transliterate>. On the same not, the doubling of consonants in English occurs only in spelling and it is not to be pronounced. Words such as /cutter/, /suppose/ and /winning/ are to be realized without the doubling as <transliterate text="supper cutter winning" src="en-UK" :tgt="options.script" sourcePreserve="high"></transliterate>, whereas Indian English often duplicates them phonetically as <transliterate text="səppəɾ kəʈʈəɾ ʋɪnnɪŋ" src="IPA" :tgt="options.script" sourcePreserve="high"></transliterate>.
    </p>
    <p class="q-body-1">Also, the sequances /ir/ in words such as /bird/ <transliterate text="bird" src="en-UK" :tgt="options.script" sourcePreserve="high"></transliterate> and /er/ in words such as /personal/ /Germany/ <transliterate text="Personal Germany" src="en-UK" :tgt="options.script" sourcePreserve="high"></transliterate> actually denote vowels and do not indicate the presence of an /r/ sound. Indians frequently inserting /r/ due to spelling pronunication in such words is very common in Indian English.</p>
    <p class="q-body-3">
      <b>Rhoticity</b>
    </p>
    <p class="q-body-1">The transcription used for British English is non-rhotic, as in, the /r/ is rarely vocalized, unless it is followed by a vowel. This implies the words /car/ and /dark/ are actually pronounced as <transliterate text="kɑː dɑːk" src="IPA" :tgt="options.script" sourcePreserve="high"></transliterate>.  However, Indian English is strongly rhotic, retain the /r/ pretty much universally.</p>
    <p class="q-body-3">
      <b>Aspiration</b>
    </p>
    <p class="q-body-1">
      Like many Indian languages, English also has aspirated (Mahaprana) sounds. But they only occur in specific contexts. For instance, the word /cake/ is actually pronounced as <transliterate text="kʰeɪk" src="IPA" :tgt="options.script" sourcePreserve="high"></transliterate> and /totally/ as <transliterate text="tʰəʊtəli" src="IPA" :tgt="options.script" sourcePreserve="high"></transliterate>. For many native speakers, the difference between /t/ /d/, /p/ /b/ & /k/ /g/ is primary perceived through lack of the additional /h/ sound in the latter (as /d b g/ often get devoiced to /t p k/). So, it's often necessary to pronounce the aspiration to differentiate them.
    </p>
    <p class="q-body-3">
      <b>Long vs Short vowels</b>
    </p>
    <p class="q-body-1">Indian languages usually teach vowels in pairs: short and long. The traditional Indian perception is that the vowels are purely differentiated by their duration. However, in many modern Indian languages, it is also a matter of quality. As in the long and short vowels are phonetically different - <transliterate text="ə ɑː ɪ iː ʊ uː" src="IPA" :tgt="options.script" sourcePreserve="high"></transliterate> :: ə ɑː ɪ iː ʊ uː. Hence, it is often challenging to hear and reproduce the actual longer version of the traditional short vowels and the shorter version of the traditional long vowels. </p>
    <p class="q-body-1">This is particularly true for Spanish or Italian, where there is no phonemic vowel length and the vowels in those languages usually correspond to vowels that only occur in their longer form in Indian languages.</p>
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
  components: {
    QTooltip,
    ControlsPlug,
    Transliterate,
    QPageSticky
  },
  data () {
    return {
      options: {script: 'IPA', sourcePreserve: 'High'},
      extra: false
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
