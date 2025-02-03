export const ScriptMixin = {
  data () {
    return {
      apiCall: this.$axios.create({
        // Always use http://localhost:8085/api/ (with a leading slash)
        // http://localhost:8085/api/
        baseURL: 'http://localhost:8085/api/',
        timeout: 100000
      }),
      wikipediaCall: this.$axios.create({
        baseURL: 'https://en.wikipedia.org/w',
        timeout: 100000
      }),
      scriptSourceCall: this.$axios.create({
        baseURL: 'http://scriptsource.org/cms/scripts/page.php?item_id=script_detail&key=Zanb',
        timeout: 100000
      }),
      voices: {
        'en-gb': ['en-GB'],
        'en-us': ['en-US'],
        'it': ['it-IT'],
        'pt-pt': ['pt-PT'],
        'pt-br': ['pt-BR'],
        'fr': ['fr-FR'],
        'de': ['de-DE'],
        'es': ['es-ES'],
        'es-419': ['es-US', 'es-MX'],
        'IPA': []
      },
      preserveSourceExampleOut: {
      },
      preserveSourceExampleIn: {
      },
      preOptionsIndic: {
      },
      preOptionSemiticAllIndic: [
      ],
      preOptionsSemitic: {
      },
      preOptionsGroup: {
        'en-us': [
          {value: 'AspirateStops', label: 'Aspirate stops<br/><small>pat spat → pʰæt spæt</small>'}
        ],
        'en-gb': [
          {value: 'AspirateStops', label: 'Aspirate stops<br/><small>pat spat → pʰat spat</small>'}
        ],
        'de': [
          {value: 'AspirateStops', label: 'Aspirate stops<br/><small>Katze → kʰatsə</small>'}
        ]
      },
      preOptionsGroupSpecific: {
        'DevanagariLimbu': [
          { label: 'Limbu Devanagari conventions<br/><small><span class="limbudev">e.g. ए़ ओ़ ए़ः के़ को़ के़ः</span></small>', value: 'LimbuDevanagariConvention' }
        ]
      },
      postOptionsGroupSpecific: {
        'Kannadaen-us': [
          { label: 'Show diphthongs', value: 'showDiphthongs' }
        ],
        'Kannadaen-uk': [
          { label: 'Show diphthongs', value: 'showDiphthongs' }
        ],
        'Sinhalaen-us': [
          { label: 'Show diphthongs', value: 'showDiphthongs' }
        ],
        'Sinhalaen-uk': [
          { label: 'Show diphthongs', value: 'showDiphthongs' }
        ],
        'Malayalamen-us': [
          { label: 'Show diphthongs', value: 'showDiphthongs' }
        ],
        'Malayalamen-uk': [
          { label: 'Show diphthongs', value: 'showDiphthongs' }
        ],
        'Teluguen-us': [
          { label: 'Show diphthongs', value: 'showDiphthongs' }
        ],
        'Teluguen-uk': [
          { label: 'Show diphthongs', value: 'showDiphthongs' }
        ],
        'Tamilen-us': [
          { label: 'Show diphthongs', value: 'showDiphthongs' }
        ],
        'Tamilen-uk': [
          { label: 'Show diphthongs', value: 'showDiphthongs' }
        ],
        'Devanagarien-us': [
          { label: 'Show diphthongs', value: 'showDiphthongs' }
        ],
        'Devanagarien-uk': [
          { label: 'Show diphthongs', value: 'showDiphthongs' }
        ]
      },
      postOptionsRadioGroup: {
        'Kannada': [['simple', 'minimal', 'full']]
      },
      postOptionsGroup: {
        'Devanagari': [{
          label: 'Show word-final viramas<br/><small> <span class="devanagari">इंदऽ सॉल्ट</span> → <span class="devanagari">इंद सॉल्ट्</span>',
          value: 'showWordEndVirama'
        }],
        'Tamil': [
          {
            label: 'Differentiate only /g/ /d/ /b/ <br/><small><span class="tamil">கேᵏட்ᵗ கேᵍட்ᵗ மேட்ᵈ பீᵇட்ᵗ பீᵖட்ᵗ</span> → <span class="tamil">கேட் கேᵍட் மேட்ᵈ பீᵇட் பீட்</span></small>',
            value: 'gdbDifferentiationTamil'
          },
          {
            label: 'Remove all differentiation<br/><small><span class="tamil">கேட் கேட் மேட் பீட் பீட்</span> → <span class="tamil">கேட் கேட் மேட் பீட் பீட்</span></small>',
            value: 'removeDifferentiationTamil'
          }
        ],
        'TamilPhonetic': [
          {
            label: 'Differentiate only /g/ /d/ /b/ <br/><small><span class="tamil">கேᷜட்ͭ கேᷚட்ͭ மேட்ͩ பீᷨட்ͭ பீᷮட்ͭ</span> → <span class="tamil">கேட் கேᷚட் மேட்ͩ பீᷨட் பீட்</span></small>',
            value: 'gdbDifferentiationTamilPhonetic'
          },
          {
            label: 'Remove all differentiation<br/><small> <span class="tamil">காᷚᷲட்ͩ காᷜᷲட்ͩ காᷜᷭட்ͭ</span> → <span class="tamil">காட் காட் காட்</span></small>',
            value: 'removeDifferentiationTamilPhonetic'
          }
        ]
      },
      autodetect: [],
      inaccurateScripts: ['IPA', 'Brahmi', 'Grantha', 'Sharada', 'Sinhala', 'Urdu'],
      scriptsIndic: [
        {
          label: 'Devanagari',
          value: 'Devanagari'
        },
        {
          label: 'Kannada',
          value: 'Kannada'
        },
        {
          label: 'Malayalam',
          value: 'Malayalam'
        },
        {
          label: 'Sinhala',
          value: 'Sinhala'
        },
        {
          label: 'Tamil',
          value: 'Tamil'
        },
        {
          label: 'Tamil Phonetic',
          value: 'TamilPhonetic'
        },
        {
          label: 'Telugu',
          value: 'Telugu'
        },
        {
          label: 'Urdu',
          value: 'Urdu'
        },
        {
          label: 'IPA',
          value: 'IPA'
        }
      ],
      scriptsSemitic: [],
      scriptsRomanization: []
    }
  },
  computed: {
    scriptRandom: function () {
      return this.scriptIndicList[this.getRandomInt(0, this.scriptIndicList.length - 1)]
    },
    scriptsOutput: function () {
      return this.scriptsIndic
    },
    scriptsInput: function () {
      return [
        {
          label: 'English (UK)',
          value: 'en-gb'
        },
        {
          label: 'English (US)',
          value: 'en-us'
        },
        {
          label: 'Italian',
          value: 'it'
        },
        {
          label: 'Portuguese (Brazil)',
          value: 'pt-br'
        },
        {
          label: 'Portuguese (Portugal)',
          value: 'pt-pt'
        },
        {
          label: 'Spanish (Spain)',
          value: 'es'
        },
        {
          label: 'Spanish (Latin America)',
          value: 'es-419'
        },
        {
          label: 'German',
          value: 'de'
        },
        {
          label: 'French',
          value: 'fr'
        },
        {
          label: 'International Phonetic Alphabet',
          value: 'IPA'
        }
      ]
    },
    scripts: function () {
      return this.scriptsIndic.concat(this.scriptsInput)
    },
    scriptsAll: function () {
      return this.scriptsIndic.concat(this.scriptsInput)
    },
    scriptSemiticSorted: function () {
      var scriptSemiticSort = this.scriptsSemitic.slice()
      scriptSemiticSort.sort(this.compareObjects)
      // console.log(scriptSemiticSort)
      return scriptSemiticSort
    },
    scriptSemiticSortedHebr: function () {
      var scriptSemiticSort = this.scriptsSemitic.slice()
      scriptSemiticSort.sort(this.compareObjects)
      // console.log(scriptSemiticSort)
      return scriptSemiticSort
    },
    scriptIndicList: function () {
      return this.scriptsIndic.map(x => x.value)
    },
    semiticLatinList: function () {
      return this.semiticLatin.map(x => x.value)
    },
    scriptLatinList: function () {
      return this.scriptsLatin.map(x => x.value)
    },
    scriptSemiticList: function () {
      return this.scriptsSemitic.map(x => x.value)
    },
    scriptSemiticListAll: function () {
      return this.scriptSemiticList.concat(['Latn', 'Type', 'Urdu', 'Thaana', 'Shahmukhi', 'Hebrew', 'ISO259', 'ISO233', 'HebrewSBL'])
    }
  },
  methods: {
    filterRadio: function (postOptions, outputScript) {
      var latest = postOptions.pop()

      if (typeof this.postOptionsRadioGroup[outputScript] !== 'undefined') {
        this.postOptionsRadioGroup[outputScript].forEach(function (options) {
          // console.log(options)
          if (options.includes(latest)) {
            var toCheck = options.filter(x => x !== latest)
            // console.log('To Check')
            toCheck.forEach(function (option) {
              // console.log('removing ' + option)
              postOptions = postOptions.filter(x => x !== option)
            })
          }
        })
      }

      if (typeof latest === 'string') {
        postOptions = postOptions.concat(latest)
      }
      return postOptions
    },
    getResultPost: function (url, data = {}) {
      return new Promise(resolve => {
        this.$axios.post(url, data)
          .then(function (response) {
            resolve(response)
          })
          .catch(function (error) {
            console.log(error)
          })
      })
    },
    getVoiceList: function (language) {
      const synth = window.speechSynthesis
      const voices = synth.getVoices()
      const voiceMatch = voices.filter(voice => this.voices[language].includes(voice.lang))
      return voiceMatch.map(x => ({value: x.name, label: x.name}))
    },
    speakText: function (text, rate, voiceName) {
      const synth = window.speechSynthesis
      const voices = synth.getVoices()
      const voice = voices.find(voice => voice.name === voiceName) // Find UK English voice
      const utterance = new SpeechSynthesisUtterance(text)
      utterance.rate = rate
      utterance.voice = voice
      synth.cancel()

      synth.speak(utterance)
    },
    compareObjects: function (a, b) {
      if (a.label < b.label) {
        return -1
      } else if (a.label > b.label) {
        return 1
      }
      return 0
    },
    getScriptObject: function (name) {
      // console.log('gettingObject')
      for (const s of this.scriptsAll) {
        if (s.value === name) {
          // console.log(s)
          return s
        }
      }
      if (name === 'autodetect') {
        return this.autodetect[0]
      }
      return { label: '', value: '' }
    },
    getScriptObjectLabel: function (label) {
      for (const s of this.scriptsAll) {
        if (s.label === label) {
          return s
        }
      }
      if (name === 'autodetect') {
        return this.autodetect[0]
      }
      return { label: '', value: '' }
    },
    getOutputClass: function (tgt, postOptions = [], outputText = '') {
      if (postOptions.includes('tradOrtho') && tgt === 'Malayalam') {
        return 'malayalamold'
      } else {
        return tgt.toLowerCase()
      }
    },
    getInputClass: function (src, preOptions = []) {
      if (preOptions.includes('siddhammukta') && src === 'Siddham') {
        return 'siddhammukta'
      } else {
        return src.toLowerCase()
      }
    },
    replaceCommaJSON: function (script, array2) {
      if (script === 'Urdu' || script === 'Thaana') {
        if (typeof array2 !== 'object') {
          array2 = JSON.parse(array2.replace(/،/g, ','))
        }
      }
      return array2
    },
    getRandomInt: function (min, max) {
      return Math.floor(Math.random() * (max - min + 1)) + min
    },
    convertAsync: function (src, tgt, txt, sourcePreserve, optionsPost, optionsPre) {
      return new Promise(resolve => {
        var data = {
          source: src,
          target: tgt,
          text: txt,
          accuracy: sourcePreserve,
          postOptions: optionsPost,
          preOptions: optionsPre
        }
        this.apiCall.post('/convert', data)
          .then(function (response) {
            resolve(response.data)
          })
          .catch(function (error) {
            console.log(error)
          })
      })
    },
    convertJSONAsync: function (src, tgt, txt, sourcePreserve, optionsPre, optionsPost) {
      return new Promise(resolve => {
        var data = {
          source: src,
          target: tgt,
          text: txt,
          accuracy: sourcePreserve,
          postOptions: optionsPost,
          preOptions: optionsPre
        }
        this.apiCall.post('/convertJSON', data)
          .then(function (response) {
            resolve(response.data)
          })
          .catch(function (error) {
            console.log(error)
          })
      })
    },
    convertMapAsync: function (src, txt, optionsPre, optionsPost) {
      return new Promise(resolve => {
        var data = {
          source: src,
          text: txt,
          postOptions: optionsPost,
          preOptions: optionsPre
        }
        this.apiCall.post('/convertMap', data)
          .then(function (response) {
            resolve(response.data)
          })
          .catch(function (error) {
            console.log(error)
          })
      })
    }
  }
}
