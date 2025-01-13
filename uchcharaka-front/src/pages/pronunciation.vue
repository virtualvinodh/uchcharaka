<template>
    <q-page padding>
      <div class="q-display-1 q-mb-xl">Non-Indian Phonemes</div>
      <audio v-for="(data,i) in consonants.concat(vowels)"
        :src="'../statics/audio/'+data.filename+'.ogg'" :key="i" :id="data.phoneme">
      </audio>
      <q-spinner-gears size="50px" color="dark" v-if="loading" ></q-spinner-gears>
      <q-tabs color="grey-8" v-if="!loading">
        <q-tab v-for="script in scriptIndicList" :key="script+'title'"
                :default="script === 'Devanagari'" slot="title" :name="script" :label="script" v-if="script !== 'IPA'" />
        <q-tab-pane v-for="script in scriptIndicList" :key="script+'content'" :name="script">
            <q-btn-group push class="q-mb-md">
              <q-btn push label="Consonants"
                @click="mode = 'Consonants'" :color="mode == 'Consonants' ? 'grey-8': ''"/>
              <q-btn push label="Vowels"
                @click="mode = 'Vowels'" :color="mode == 'Vowels' ? 'grey-8': ''"/>
           </q-btn-group>
            <phoneme-list :consonants="consonants" :consonantsMap="consonantsMap" :script="script"
              v-if="mode == 'Consonants'"/>
            <phoneme-list :consonants="vowels" :consonantsMap="vowelsMap" :script="script"
            v-if="mode == 'Vowels'"/>
        </q-tab-pane>
      </q-tabs>
  </q-page>
</template>

<script>
import { QTooltip, QPageSticky, QTabs, QTab, QTabPane, QBtnGroup, QSpinnerGears } from 'quasar'
import { ScriptMixin } from '../mixins/ScriptMixin'
import ControlsPlug from '../components/ControlsPlug'
import Transliterate from '../components/Transliterate'
import PhonemeList from '../components/PhonemeList.vue'

export default {
  // filename: 'Pagefilename',
  mixins: [ScriptMixin],
  components: {
    QSpinnerGears,
    QTooltip,
    QBtnGroup,
    ControlsPlug,
    Transliterate,
    QPageSticky,
    QTabs,
    QTab,
    QTabPane,
    PhonemeList
  },
  computed: {
    vowelsIPA: function () {
      return this.vowels.map(item => item.phoneme + ' k' + item.phoneme)
    },
    consonantsIPA: function () {
      return this.consonants.map(item => item.phoneme + 'ə')
    }
  },
  mounted: function () {
    this.renderPage()
  },
  watch: {
    options: function () {
      this.renderPage()
    }
  },
  data () {
    return {
      mode: 'Consonants',
      loading: true,
      consonantsMap: {},
      vowelsMap: {},
      vowels: [
        {
          phoneme: 'æ',
          name: 'Near-open front unrounded vowel',
          filename: 'Near-open_front_unrounded_vowel',
          wikilink: 'Near-open front unrounded vowel',
          transcription: '',
          approximation: '',
          note: ''
        },
        {
          phoneme: 'ɔ',
          name: 'Open-mid back rounded vowel',
          filename: 'PR-open-mid_back_rounded_vowel',
          wikilink: 'Open-mid back rounded vowel',
          transcription: '',
          approximation: '',
          note: ''
        },
        {
          phoneme: 'ɔː',
          name: 'Long: Open-mid back rounded vowel',
          filename: '',
          wikilink: 'Open-mid back rounded vowel',
          transcription: '',
          approximation: '',
          note: ''
        },
        {
          phoneme: 'ɒ',
          name: 'Open back rounded vowel',
          filename: 'PR-open_back_rounded_vowel',
          wikilink: 'Open back rounded vowel',
          transcription: '',
          approximation: '',
          note: ''
        },
        {
          phoneme: 'ʌ',
          name: 'Open-mid back unrounded vowel',
          filename: 'PR-open-mid_back_unrounded_vowel2',
          wikilink: 'Open-mid back unrounded vowel',
          transcription: '',
          approximation: '',
          note: ''
        },
        {
          phoneme: 'ɚ',
          name: 'R-colored_vowel (Retroflex ə)',
          filename: 'En-us-er',
          wikilink: 'R-colored_vowel',
          transcription: '',
          approximation: '',
          note: ''
        },
        {
          phoneme: 'ɐ',
          name: 'Near-open central vowel',
          filename: 'Near-open_central_unrounded_vowel',
          wikilink: 'Near-open central vowel',
          transcription: '',
          approximation: '',
          note: ''
        },
        {
          phoneme: 'ɑ',
          name: 'Open back unrounded vowel',
          filename: 'Open_back_unrounded_vowel',
          wikilink: 'Open back unrounded vowel',
          transcription: '',
          approximation: '',
          note: ''
        },
        {
          phoneme: 'a',
          name: 'Open front unrounded vowel',
          filename: 'Open_front_unrounded_vowel',
          wikilink: 'Open front unrounded vowel',
          transcription: '',
          approximation: '',
          note: ''
        },
        {
          phoneme: 'aː',
          name: 'Long: Open front unrounded vowel',
          filename: 'Open_front_unrounded_vowel',
          wikilink: 'Open front unrounded vowel',
          transcription: '',
          approximation: '',
          note: ''
        },
        {
          phoneme: 'i',
          name: 'Close front unrounded vowel',
          filename: 'Close_front_unrounded_vowel',
          wikilink: 'Close front unrounded vowel',
          transcription: '',
          approximation: '',
          note: ''
        },
        {
          phoneme: 'ᵻ',
          name: 'Close central unrounded vowel',
          filename: 'Close_central_unrounded_vowel',
          wikilink: 'Close central unrounded vowel',
          transcription: '',
          approximation: '',
          note: ''
        },
        {
          phoneme: 'u',
          name: 'Close back rounded vowel',
          filename: 'Close_back_rounded_vowel',
          wikilink: 'Close back rounded vowel',
          transcription: '',
          approximation: '',
          note: ''
        },
        {
          phoneme: 'y',
          name: 'Close front rounded vowel',
          filename: 'Close_front_rounded_vowel',
          wikilink: 'Close front rounded vowel',
          transcription: '',
          approximation: '',
          note: ''
        },
        {
          phoneme: 'yː',
          name: 'Long: Close front rounded vowel',
          filename: '',
          wikilink: '',
          transcription: '',
          approximation: '',
          note: ''
        },
        {
          phoneme: 'ɛː',
          name: 'Long: Open-mid front unrounded vowel',
          filename: 'Open-mid_front_unrounded_vowel',
          wikilink: 'Open-mid front unrounded vowel',
          transcription: '',
          approximation: '',
          note: ''
        },
        {
          phoneme: 'e',
          name: 'Close-mid front unrounded vowel',
          filename: 'Close-mid_front_unrounded_vowel',
          wikilink: 'Close-mid front unrounded vowel',
          transcription: '',
          approximation: '',
          note: ''
        },
        {
          phoneme: 'ɜ',
          name: 'Open-mid central unrounded vowel',
          filename: 'Open-mid_central_unrounded_vowel',
          wikilink: 'Open-mid central unrounded vowel',
          transcription: '',
          approximation: '',
          note: ''
        },
        {
          phoneme: 'ɜː',
          name: 'Long: Open-mid central unrounded vowel',
          filename: '',
          wikilink: 'Open-mid central unrounded vowel',
          transcription: '',
          approximation: '',
          note: ''
        },
        {
          phoneme: 'ø',
          name: 'Close-mid front rounded vowel',
          filename: 'Close-mid_front_rounded_vowel',
          wikilink: 'Close-mid front rounded vowel',
          transcription: '',
          approximation: '',
          note: ''
        },
        {
          phoneme: 'øː',
          name: 'Long: Close-mid front rounded vowel',
          filename: '',
          wikilink: 'Close-mid front rounded vowel',
          transcription: '',
          approximation: '',
          note: ''
        },
        {
          phoneme: 'œ',
          name: 'Open-mid front rounded vowel',
          filename: 'Open-mid_front_rounded_vowel_(2)',
          wikilink: 'Open-mid front rounded vowel',
          transcription: '',
          approximation: '',
          note: ''
        }
      ],
      consonants: [
        {
          phoneme: 'z',
          name: 'Voiceless Alveolar Plosive',
          filename: 'Voiceless_alveolar_plosive',
          wikilink: 'Voiceless_dental_and_alveolar_plosives',
          transcription: '',
          approximation: '',
          note: 'The tongue does not go as far back'
        },
        {
          phoneme: 'f',
          name: 'Voiceless Alveolar Plosive',
          filename: 'Voiceless_alveolar_plosive',
          wikilink: 'Voiceless_dental_and_alveolar_plosives',
          transcription: '',
          approximation: '',
          note: 'The tongue does not go as far back'
        },
        {
          phoneme: 't',
          name: 'Voiceless Alveolar Plosive',
          filename: 'Voiceless_alveolar_plosive',
          wikilink: 'Voiceless_dental_and_alveolar_plosives',
          transcription: '',
          approximation: '',
          note: 'The tongue does not go as far back'
        },
        {
          phoneme: 'tʰ',
          name: 'Aspirated Voiceless Alveolar Plosive',
          filename: '',
          wikilink: '',
          transcription: '',
          approximation: '',
          note: ''
        },
        {
          phoneme: 'd',
          name: 'Voiced Alveolar Plosive',
          filename: 'Voiced_alveolar_plosive',
          wikilink: 'Voiced_dental_and_alveolar_plosives',
          transcription: '',
          approximation: '',
          note: 'The tongue does not go as far back'
        },
        {
          phoneme: 'θ',
          name: 'Voiceless Dental Fricative',
          wikilink: 'Voiceless_dental_fricative',
          filename: 'Voiceless_dental_fricative',
          transcription: '',
          approximation: '',
          note: ''
        },
        {
          phoneme: 'ð',
          name: 'Voiced Dental Frivative',
          wikilink: 'Voiced_dental_fricative',
          filename: 'Voiced_dental_fricative',
          transcription: '',
          approximation: '',
          note: ''
        },
        {
          phoneme: 'w',
          name: 'Voiced Label-Velar Approximant',
          wikilink: 'Voiced labial–velar approximant',
          filename: 'Voiced_labio-velar_approximant',
          transcription: '',
          approximation: '',
          note: 'try saying v but with the lips in an u position'
        },
        {
          phoneme: 'v',
          name: 'Voiced Labiodental Fricative',
          wikilink: 'Voiced labiodental fricative',
          filename: 'Voiced_labio-dental_fricative',
          transcription: '',
          approximation: '',
          note: 'Something in between Indian /v/ and /f/'
        },
        {
          phoneme: 'β',
          name: 'Voiced Bilabial Fricative',
          wikilink: 'Voiced bilabial fricative',
          filename: 'Voiced_bilabial_fricative',
          transcription: '',
          approximation: '',
          note: 'Something in between Indian /v/ and /b/'
        },
        {
          phoneme: 'ʎ',
          name: 'Voiced palatal lateral approximant',
          wikilink: 'Voiced palatal lateral approximant',
          filename: 'Palatal_lateral_approximant',
          transcription: '',
          approximation: '',
          note: 'In between Indian /y/ and /j/'
        },
        {
          phoneme: 'ʝ',
          name: 'Voiced palatal fricative',
          wikilink: 'Voiced palatal fricative',
          filename: 'Voiced_palatal_fricative',
          transcription: '',
          approximation: '',
          note: 'Sort of heavy /y/'
        },
        {
          phoneme: 'ɹ',
          name: 'Postalveolar_approximant',
          wikilink: 'Voiced alveolar and postalveolar approximants',
          filename: 'Postalveolar_approximant',
          transcription: '',
          approximation: '',
          note: 'Indian /r/ but far lighter'
        },
        {
          phoneme: 'ʁ',
          name: 'Voiced uvular fricative',
          wikilink: 'Voiced uvular fricative',
          filename: 'Voiced_uvular_fricative',
          transcription: '',
          approximation: '',
          note: 'Like pronouncing Indian /r/ and /g/ at he same time'
        },
        {
          phoneme: 'ʒ',
          name: 'Voiced postalveolar fricative',
          wikilink: 'Voiced postalveolar fricative',
          filename: 'Voiced_palato-alveolar_sibilant',
          transcription: '',
          approximation: '',
          note: 'Like Indian /sh/ with element of /j/'
        },
        {
          phoneme: 'ç',
          name: 'Voiceless palatal fricative',
          wikilink: 'Voiceless palatal fricative',
          filename: 'Voiceless_palatal_fricative',
          transcription: '',
          approximation: '',
          note: 'In between /h/ and /sh/'
        },
        {
          phoneme: 'h',
          name: 'Voiceless glottal fricative',
          wikilink: 'Voiceless glottal fricative',
          filename: 'Voiceless_glottal_fricative',
          transcription: '',
          approximation: '',
          note: 'Like /h/ but slightly harder'
        },
        {
          phoneme: 'x',
          name: 'Voiceless velar fricative',
          wikilink: 'Voiceless velar fricative',
          filename: 'Voiceless_velar_fricative',
          transcription: '',
          approximation: '',
          note: 'Like saying /h/ and /k/ at the same time'
        },
        {
          phoneme: 'ɣ',
          name: 'Voiced velar fricative',
          wikilink: 'Voiced velar fricative',
          filename: 'Voiced_velar_fricative',
          transcription: '',
          approximation: '',
          note: 'Like saying /h/ and /g/ at the same time'
        }
      ]
    }
  },
  methods: {
    renderPage: async function () {
      this.loading = true
      let postOptions = ['showWordEndVirama']
      this.consonantsMap = await this.convertMapAsync('IPA', this.consonantsIPA, [], postOptions)
      console.log(this.consonantsMap)
      this.vowelsMap = await this.convertMapAsync('IPA', this.vowelsIPA, [], postOptions)
      this.loading = false
    }
  }
}
</script>

<style scoped>
</style>
