
<template>
  <q-page class="q-pa-md" id="scrollstart">
          <q-alert
          color="red-4"
          icon="signal_cellular_alt"
          appear
          :actions="[{ label: 'Retry', handler: retryPage }]"
          class="q-mb-sm q-mr-xl"
          v-if="!checkifOnline && $q.platform.is.cordova"
        > You're not currently connected. Please activate your mobile data or Wi-Fi to use the app.
      </q-alert>
  <div class="row">
      <div class="row col-xs-12 col-md-11 col-xl-5 q-ma-md float-div print-hide">
       <div class="row">
       <q-select
        filter
        inset
        autofocus-filter
        filter-placeholder="search"
        @input="updateInput"
        placeholder="Input Language"
        v-model="inputScript"
        class="col-xs-6 col-md-6 q-ma-sm"
        :options="scriptsInput"
      />

      <q-btn class="col-xs-3 col-md-3 q-ma-sm" v-show="inputPast !== ''"
        @click="updateHist" dense> <small>{{getScriptObject(inputPast).label}}</small> </q-btn>
      <q-icon name="history" size="25px" v-show="inputPast !== ''" class="print-hide"/>
  </div>
  <!-- <q-btn class="q-ma-sm q-mt-md btn2 print-hide col-xs-1 col-md-1" @click="copySource" :data-clipboard-text="textInput.replace(/<br\/>/g, '\n')"> <q-icon name="file_copy" /><q-tooltip>Copy source text</q-tooltip></q-btn> -->
  <input-options :inputScript="inputScript" :outputScript="outputScript" :preOptionsInput="preOptions" :showscriptName="false"
      :postOptions="postOptions" v-model="preOptions" @input="convert" />
  <q-input
    v-model.trim="textInput"
    type="textarea"
    float-label="Input text"
    class="text-input col-xs-12 col-md-12 q-ma-sm"
    :class="getInputClass(inputScript, preOptions)"
    autofocus
    @input="throttled"
    clearable
    color="dark"
    rows="10"
    :max-height="1500"
  />
  <input-notice :inputScript="inputScript" :outputScript="outputScript" :preOptions="preOptions"
    :postOptions="postOptions"></input-notice>
  </div>
    <div class="q-ma-md print-hide">

    </div>
    <div class="row col-xs-12 col-md-11 col-xl-5 q-ma-md float-div">
      <div class="row">
       <q-select
        filter
        autofocus-filter
        @input="updateOuput"
        filter-placeholder="search"
        v-model="outputScript"
        placeholder="Output Script"
        class="col-xs-6 col-md-6 q-ma-sm print-hide"
        :options="scriptsOutput"
      />
      <q-btn class="col-xs-3 col-md-3 q-ma-sm print-hide" v-show="outputPast !== ''"
       @click="updateHistOut" dense> <small>{{getScriptObject(outputPast).label}}</small> </q-btn>
      <q-icon name="history" size="25px" v-show="outputPast !== ''" class="print-hide"/>
      </div>
  <div class="q-mt-sm"><output-buttons @fontsizeinc="fontSize += 20" @fontsizedec="fontSize -= 20"
       @printdoc="printDocument" @screenshot="imageConvert(downloadImage.bind(this))" @copytext="copy" :convertText="convertText" :content="''"></output-buttons></div>
       <span v-if="voiceExists">
      <q-collapsible icon="record_voice_over" sublabel="Voice options">
       <q-select
        filter
        inset
        autofocus-filter
        filter-placeholder="search"
        placeholder="Voice"
        v-model="voiceLang"
        class="col-xs-8 col-md-8 q-ml-sm q-mt-sm"
        :options="voiceList"
        stack-label="Voice"
      />
      <div class="row"><div class="col-md-3 q-mt-lg q-ml-sm"> Speech Speed </div> <q-slider v-model="rate" :min="0" :max="2" :step="0.1" :style="{'width':'200px'}" snap label-always color="grey-8" class="col-md-7"></q-slider></div>
      </q-collapsible>
    </span>
    <output-options :inputScript="inputScript" :outputScript="outputScript" :postOptionsInput="postOptions" :sourcePreserveInput="sourcePreserve" :showscriptName="false"
       :convertText="convertText" :hideSourcePreserve="false"
        @input="convertOutputOptions($event)" ></output-options>

      <q-btn-group class="q-ma-sm" >
            <q-btn label="Text" @click="mode = 'text'" :color="mode == 'text' ? 'grey-8': ''"/>
            <q-btn label="Sentence" @click="mode = 'sentence'" :color="mode == 'sentence' ? 'grey-8': ''" />
            <q-btn label="Word" @click="mode = 'word'" :color="mode == 'word' ? 'grey-8': ''" />
            <q-btn label="Tooltip" @click="mode = 'tooltip'" :color="mode == 'tooltip' ? 'grey-8': ''"/>
      </q-btn-group>

    <div
      ref="brahmiText"
      class="text-output col-xs-12 col-md-12 q-pa-md q-pr-lg bg-grey-1 "
      >
       <div>
       <q-btn @click="speakText(textInput, rate, voiceLang)" icon="record_voice_over" flat compact v-if="mode == 'text' && convertText != '' && voiceExists"></q-btn>
       <span :class="getOutputClass(outputScript, postOptions, convertText)" :style="{'font-size': fontSize + '%'}"
        v-html="sanitize(convertText)" v-if="mode == 'text'"></span>
      </div>

      <render-text :source="inputScript" :text="textInput" :options="{script: outputScript, sourcePreserve: sourcePreserve, postOptions: postOptions, preOptions:preOptions }" :voiceName="voiceLang" :mode="mode" :rate="rate" class="q-ml-ml q-mt-sm" v-if="mode != 'text'"
      :style="{'font-size': fontSize + '%'}"
      />

    </div>
    <output-notice :inputScript="inputScript" :outputScript="outputScript" :postOptions="postOptions"
     :convertText="convertText" :inputText="textInput"></output-notice>
    </div>
    </div>
  <transition
    enter-active-class="animated fadeIn"
    leave-active-class="animated fadeOut"
    appear
  >
    <div class="q-ma-lg q-body-1 print-hide" id="scrollend">
      Please report any bugs found in <a href="https://github.com/virtualvinodh/uccharaka/issues">Github</a>.
    </div>
  </transition>
  <a :href="brahmiImg" ref="imgDownload" :style="{'display': 'none'}" download="text.png"><button>Download</button></a>
<q-page-sticky position="top-right" :offset="[18, 18]" v-show="scrollExists" class="print-hide">
    <span><q-btn round color="dark" @click="scrolldown" icon="arrow_downward" v-show="!scrolled"/><q-tooltip>Scroll down</q-tooltip> </span>
  </q-page-sticky>
  <q-page-sticky position="bottom-right" :offset="[18, 18]" v-back-to-top>
    <span><q-btn round color="dark" @click="scrollup" icon="arrow_upward"  class="print-hide"/><q-tooltip>Scroll Up</q-tooltip> </span>
  </q-page-sticky>
  </q-page>
</template>

<style>
</style>

<script>
import {QProgress, QTab, QTabs, QTooltip, QEditor, QRadio, QBtn, QField, QBtnToggle, QToggle, QInput, QSelect, QOptionGroup, QAlert, QSpinnerComment, QPageSticky, QUploader, QCollapsible, QBtnGroup, QSlider} from 'quasar'
import sanitizeHtml from 'sanitize-html'
import html2canvas from 'html2canvas'
import Transliterate from '../components/Transliterate'
import InputOptions from '../components/InputOptions'
import OutputOptions from '../components/OutputOptions'
import InputNotice from '../components/InputNotice'
import OutputNotice from '../components/OutputNotice'
import OutputButtons from '../components/OutputButtons'
import ConverterMenu from '../components/converterMenu'
import RenderText from '../components/RenderText'

import scrollTo from 'vue-scrollto'
import { ScriptMixin } from '../mixins/ScriptMixin'

import ClipboardJS from 'clipboard'

var clipboard = new ClipboardJS('.btn2')
console.log(clipboard)

var _ = require('underscore')
const isOnline = require('is-online')

export default {
  name: 'PageIndex',
  mixins: [ScriptMixin],
  meta: {
    // meta tags
    meta: {
      description: { name: 'description', content: 'Aksharamukha aims to provide script conversion or transliteration between various scripts within the Indic cultural sphere. These include historic scripts, contemporary Brahmi-derived/inspired scripts, scripts invented for minority Indian languages, scripts that have co-existed with Indic scripts (like Avestan) or linguistically related scripts like Old Persian.' },
      keywords: { name: 'keywords', content: 'scripts, writing systems, transliteration, unicode, conversion, indic' }
    },

    // <noscript> tags
    noscript: {
      default: 'Aksharamukha aims to provide script conversion between various scripts within the Indic cultural sphere. These include historic scripts, contemporary Brahmi-derived/inspired scripts, scripts invented for minority Indian languages, scripts that have co-existed with Indic scripts (like Avestan) or linguistically related scripts like Old Persian. It also specifically provides lossless transliteration between the main Indian scripts (along with Sinhala). Apart from the simple mapping of characters, Askharamukha also attempts to implement various script/language-specific orthographic conventions (where known) such as vowel lengths, gemination and nasalization. It also provides several customization options to fine-tune and get the desired orthography. Aksharamukha as of now supports 78 scripts and 7 romanization methods. The scripts supported are: Ahom, Ariyaka, Assamese, Avestan, Balinese, Batak Karo, Batak Mandailing, Batak Pakpak, Batak Toba, Batak Simalungun, Bengali, Brahmi, Bhaiksuki, Buginese (Lontara), Buhid, Burmese (Myanmar), Chakma, Cham, Devanagari, Dogra, Grantha, Grantha (Pandya), Gujarati, Hanunoo, Javanese, Kaithi, Kannada, Khamti Shan, Kharoshthi, Khmer (Cambodian), Khojki, Khom Thai, Khudawadi, Lao, Lao (Pali), Lepcha, Limbu, Malayalam, Mahajani, Meetei Mayek (Manipuri), Modi, Mon, Multani, Newa (Nepal Bhasa), Old Persian, Oriya, PhagsPa, Punjabi (Gurmukhi), Ranjana (Lantsa), Rejang, Santali (Ol Chiki), Saurashtra, Siddham, Shan, Sharada, Sinhala, Sora Sompeng, Sundanese, Syloti Nagari, Tagbanwa, Tagalog, Tai Laing, Tai Tham (Lanna), Takri, Tamil, Tamil (Extended), Tamil Brahmi, Telugu, Thaana (Dhivehi), Thai, Tibetan, Tirhuta (Maithili), Urdu, Vatteluttu, Warang Citi, Zanabazar Square, Cyrillic (Russian), IPA, The Romanization Formats supported are: Harvard-Kyoto, ITRANS, Velthuis, IAST, ISO, Titus, Roman (Readable)'
    }
  },
  components: {
    RenderText,
    QSlider,
    QBtnGroup,
    QTab,
    QProgress,
    QTabs,
    QAlert,
    QEditor,
    QRadio,
    QBtn,
    QField,
    QBtnToggle,
    QToggle,
    QInput,
    QSelect,
    QCollapsible,
    QSpinnerComment,
    QOptionGroup,
    QTooltip,
    Transliterate,
    InputOptions,
    OutputOptions,
    InputNotice,
    OutputNotice,
    OutputButtons,
    QPageSticky,
    QUploader,
    ConverterMenu
  },
  data () {
    return {
      mode: 'text',
      voiceLang: '',
      textInput: '',
      checkifOnline: true,
      imageFile: '',
      displayButton: false,
      beta: true,
      model: [],
      scrolled: false,
      inputScript: '',
      outputScript: '',
      postOptions: [],
      preOptions: [],
      sourcePreserve: 'Medium',
      options: {},
      convertText: '',
      brahmiImg: '',
      fontSize: 100,
      dash: _,
      loading: false,
      inputPast: '',
      outputPast: '',
      throttled: _.debounce(this.convert, 300),
      postOptionsScript: {},
      preOptionsScript: {},
      scrollExists: false,
      postOptionsSourcePreserve: [[], false],
      rate: 0.75,
      refresh: 0
    }
  },
  mounted () {
    this.checkOnline()

    if (localStorage.sourcePreserve) {
      this.sourcePreserve = JSON.parse(localStorage.sourcePreserve)
    }
    if (localStorage.inputScript) {
      this.inputScript = localStorage.inputScript
    }
    if (localStorage.mode) {
      console.log('mode is', localStorage.mode)
      this.mode = localStorage.mode
    }
    if (localStorage.inputPast) {
      this.inputPast = localStorage.inputPast
    }
    if (localStorage.outputScript) {
      this.outputScript = localStorage.outputScript
    }
    if (localStorage.outputPast) {
      this.outputPast = localStorage.outputPast
    }
    if (localStorage.postOptionsScriptIndex) {
      this.postOptionsScript = JSON.parse(localStorage.postOptionsScriptIndex)

      if (typeof this.postOptionsScript[this.outputScript] === 'undefined') {
        this.postOptionsScript[this.outputScript] = []
      }
      this.$set(this, 'postOptions', this.postOptionsScript[this.outputScript])
    }
    if (localStorage.preOptionsScriptIndex) {
      this.preOptionsScript = JSON.parse(localStorage.preOptionsScriptIndex)

      if (typeof this.preOptionsScript[this.inputScript] === 'undefined') {
        this.preOptionsScript[this.inputScript] = []
      }
      this.$set(this, 'preOptions', this.preOptionsScript[this.inputScript])
    }

    if (typeof this.$route.query.target !== 'undefined') {
      this.outputScript = this.$route.query.target
    }

    if (typeof this.$route.query.text !== 'undefined') {
      this.textInput = this.$route.query.text
      this.convert()
    }

    if (window.innerWidth > document.body.clientWidth) {
      this.scrollExists = true
    } else {
      this.scrollExists = false
    }

    this.postOptionsSourcePreserve = [this.postOptions, this.sourcePreserve]
    setTimeout(() => {
      this.refresh++
      if (this.voiceExists) {
        this.voiceLang = this.voiceList[0].value
      }
    }, 1000)
  },
  updated: function () {
    if (window.innerWidth > document.body.clientWidth) {
      this.scrollExists = true
    } else {
      this.scrollExists = false
    }
  },
  computed: {
    voiceList: function () {
      console.log(this.refresh)
      return this.getVoiceList(this.inputScript)
    },
    voiceExists: function () {
      return this.voiceList.length > 0
    }
  },
  watch: {
    sourcePreserve (newV, oldV) {
      localStorage.sourcePreserve = JSON.stringify(newV)
    },
    mode (newV, oldV) {
      localStorage.mode = this.mode
    },
    inputScript (newScript, oldScript) {
      if (oldScript !== '') {
        this.inputPast = oldScript
        localStorage.inputPast = oldScript
      }
      localStorage.inputScript = newScript
    },
    outputScript (newScript, oldScript) {
      if (oldScript !== '') {
        this.outputPast = oldScript
        localStorage.outputPast = oldScript
      }
      localStorage.outputScript = newScript
    },
    postOptions (newOpt, oldOpt) {
      this.postOptionsScript[this.outputScript] = newOpt
      localStorage.postOptionsScriptIndex = JSON.stringify(this.postOptionsScript)

      if (typeof this.postOptionsScript[this.outputScript] === 'undefined') {
        this.postOptionsScript[this.outputScript] = []
      }

      this.$set(this, 'postOptions', this.postOptionsScript[this.outputScript])
    },
    preOptions (newOpt, oldOpt) {
      this.preOptionsScript[this.inputScript] = newOpt
      localStorage.preOptionsScriptIndex = JSON.stringify(this.preOptionsScript)

      if (typeof this.preOptionsScript[this.inputScript] === 'undefined') {
        this.preOptionsScript[this.inputScript] = []
      }

      this.$set(this, 'preOptions', this.preOptionsScript[this.inputScript])
    }
  },
  methods: {
    convertOutputOptions: function (event) {
      this.postOptions = event[0]
      this.sourcePreserve = event[1]
      this.convert()
    },
    retryPage: function () {
      this.checkOnline()

      if (this.checkifOnline) {
        document.location.reload(true)
        this.convert()
      }
    },
    checkOnline: async function () {
      this.checkifOnline = await isOnline()
    },
    scrolldown: function () {
      scrollTo.scrollTo('#scrollend', 1000)
      this.scrolled = true
    },
    scrollup: function () {
      scrollTo.scrollTo('.q-toolbar-title', 1000)
      this.scrolled = false
    },
    updateHist: function () {
      this.inputScript = this.inputPast
      this.updateInput()
    },
    updateInput: function () {
      if (typeof this.preOptionsScript[this.inputScript] === 'undefined') {
        this.preOptionsScript[this.inputScript] = []
      }
      this.$set(this, 'preOptions', this.preOptionsScript[this.inputScript])
      if (this.voiceExists) {
        this.voiceLang = this.voiceList[0].value
      } else {
        this.voiceLang = null
      }

      this.convert()
    },
    updateHistOut: function () {
      this.outputScript = this.outputPast
      this.updateOuput()
    },
    updateOuput: function () {
      if (typeof this.postOptionsScript[this.outputScript] === 'undefined') {
        this.postOptionsScript[this.outputScript] = []
      }
      this.$set(this, 'postOptions', this.postOptionsScript[this.outputScript])

      if (this.inputScript === 'Oriya' && this.outputScript === 'Bengali') {
        this.$set(this, 'postOptions', ['khandatabatova'])
      }

      this.convert()
    },
    copy: function () {
      this.$q.notify({
        type: 'info',
        message: 'Copied',
        position: 'center',
        timeout: 200
      })
    },
    copySource: function () {
      this.$q.notify({
        type: 'info',
        message: 'Copied',
        position: 'center',
        timeout: 200
      })
    },
    sanitize: function (html) {
      return sanitizeHtml(html)
    },
    printDocument: function () {
      // manually hide the side menu while printing and bring it back when printing is complete
      window.print()
      this.$q.notify({
        type: 'info',
        message: 'Consider hiding the side-menu before attempting to print by clicking on the icon next to the logo.',
        position: 'center',
        timeout: 5000
      })
    },
    downloadImage: function () {
      var dhis = this
      if (dhis.$q.platform.is.cordova) {
        var params = {data: dhis.brahmiImg, prefix: 'aksharamukha_', format: 'PNG', quality: 100, mediaScanner: true}
        window.imageSaver.saveBase64Image(params,
          function (filePath) {
            console.log('File saved on ' + filePath)
            dhis.$q.notify({
              type: 'info',
              message: 'The image has been saved in your gallery. Please check there.',
              position: 'center',
              timeout: 5000
            })
          },
          function (msg) {
            console.error(msg)
          }
        )
      } else {
        dhis.$refs.imgDownload.click()
      }
    },
    shareCordovaText: function () {
      var options = {
        message: this.convertText,
        subject: this.convertText, // fi. for email
        chooserTitle: 'Pick an app' // Android only, you can override the default share sheet title
      }

      var onSuccess = function (result) {
        console.log('Share completed? ' + result.completed)
        console.log('Shared to app: ' + result.app)
      }

      var onError = function (msg) {
        console.log('Sharing failed with message: ' + msg)
      }

      window.plugins.socialsharing.shareWithOptions(options, onSuccess, onError)
    },
    convert: async function () {
      this.convertText += ' . . . '

      // this.runCode()

      if (this.$q.platform.is.cordova) {
        this.checkOnline()
      }

      if (this.textInput === '' || this.inputScript === '' || this.outputScript === '' ||
        this.inputScript === 'undefined' || this.outputScript === 'undefined') {
        this.convertText = ''
        return
      }
      this.loading = true

      console.log('Source Preserve usage is ' + this.sourcePreserve)
      var data = {
        source: this.inputScript,
        target: this.outputScript,
        text: this.textInput,
        accuracy: this.sourcePreserve,
        postOptions: this.postOptions,
        preOptions: this.preOptions
      }
      var dhis = this

      this.apiCall.post('/convert', data)
        .then(function (response) {
          dhis.convertText = response.data
          dhis.loading = false
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    imageConvert: function (func) {
      var node = this.$refs.brahmiText
      console.log(node)
      var dhis = this
      this.$q.notify({
        type: 'info',
        message: 'Snapshot being generated',
        position: 'center',
        timeout: 200
      })

      html2canvas(node).then(function (canvas) {
        var image = new Image()
        image.src = canvas.toDataURL('image/png', 1)
        dhis.brahmiImg = image.src
        image.onload = function () {
          dhis.brahmiImg = image.src

          var image2 = new Image()
          var cropped = dhis.removeWhite(image)
          image2.src = cropped
          dhis.brahmiImg = cropped

          image2.onload = func
        }
      })
    },
    removeWhite: function (imageObject) {
      var imgWidth = imageObject.width
      var imgHeight = imageObject.height
      var canvas = document.createElement('canvas')
      canvas.setAttribute('width', imgWidth)
      canvas.setAttribute('height', imgHeight)
      var context = canvas.getContext('2d')
      context.drawImage(imageObject, 0, 0)

      var imageData = context.getImageData(0, 0, imgWidth, imgHeight)
      var data = imageData.data
      var getRBG = function (x, y) {
        var offset = imgWidth * y + x
        return {
          red: data[offset * 4],
          green: data[offset * 4 + 1],
          blue: data[offset * 4 + 2],
          opacity: data[offset * 4 + 3]
        }
      }
      var isWhite = function (rgb) {
        // many images contain noise, as the white is not a pure #fff white
        return rgb.red > 200 && rgb.green > 200 && rgb.blue > 200
      }
      var scanY = function (fromTop) {
        var offset = fromTop ? 1 : -1

        // loop through each row
        for (var y = fromTop ? 0 : imgHeight - 1; fromTop ? (y < imgHeight) : (y > -1); y += offset) {
        // loop through each column
          for (var x = 0; x < imgWidth; x++) {
            var rgb = getRBG(x, y)
            if (!isWhite(rgb)) {
              if (fromTop) {
                return y
              } else {
                return Math.min(y + 1, imgHeight - 1)
              }
            }
          }
        }
        return null // all image is white
      }
      var scanX = function (fromLeft) {
        var offset = fromLeft ? 1 : -1
        // loop through each column
        for (var x = fromLeft ? 0 : imgWidth - 1; fromLeft ? (x < imgWidth) : (x > -1); x += offset) {
          // loop through each row
          for (var y = 0; y < imgHeight; y++) {
            var rgb = getRBG(x, y)
            if (!isWhite(rgb)) {
              if (fromLeft) {
                return x
              } else {
                return Math.min(x + 1, imgWidth - 1)
              }
            }
          }
        }
        return null // all image is white
      }

      var cropTop = scanY(true) - 20
      var cropBottom = scanY(false) + 20
      var cropLeft = scanX(true) - 20
      var cropRight = scanX(false) + 20
      var cropWidth = cropRight - cropLeft
      var cropHeight = cropBottom - cropTop

      canvas.setAttribute('width', cropWidth)
      canvas.setAttribute('height', cropHeight)
      // finally crop the guy
      canvas.getContext('2d').drawImage(imageObject,
        cropLeft, cropTop, cropWidth, cropHeight,
        0, 0, cropWidth, cropHeight)

      return canvas.toDataURL()
    }
  }
}
</script>

<style scoped>
.float-div {
  display: inline-block;
  float: left;
}
.notice {
  color: gray;
  font-size: 12px;
}
.text-output {
  min-height: 230px;
}
</style>
