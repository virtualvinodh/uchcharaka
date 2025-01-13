<template>
  <q-page padding>
    <h5> Python package</h5>
    <br/><br/><p>Uchcharaka requires espeak-ng to be installed and available in the system path. Please install <a href="https://github.com/espeak-ng/espeak-ng">eSpeak NG</a> in your system before installing Uchcharaka.</p>
    <h5> How to Use </h5> <br/>
    <p class="q-body-1">Install, Aksharamukha from pip </p>

    <span class="code">pip install uccharaka</span><br/><br/>

    <span class="code">from uccharaka import transcriber as tr</span> <br/> <br/>

    <hr/>
    <span class="code">transcriber = tr.Transcriber(language, script, accuracy='medium', preoptions = [], postoptions = [])</span><br/>
    <span class="code">transcriber.transcribe(text)</span>
    <br/><br/>
    <table class="q-body-1">
      <tr>
        <td><b>Parameter</b></td>
        <td><b>Description</b></td>
      </tr>
    <tr>
        <td>language</td>
        <td>Language code of the supported language</td>
    </tr>
    <tr>
        <td>script</td>
        <td>Script identifier of the target script</td>
    </tr>
    <tr>
        <td>accuracy</td>
        <td>'low', 'medium' or 'high'</td>
    </tr>
    <tr>
        <td>text</td>
        <td>The text to be transcribed. </td>
    </tr>
    <tr>
        <td>preoptions</td>
        <td>Various options that are relevant to the input text. An array of strings, the strings being the various options.</td>
    </tr>
    <tr>
        <td>postoptions</td>
        <td>Various options that customize the transliteration output. An array of strings, the strings being the various options.</td>
    </tr>
    </table> <br/>
    <p class="q-body-1">All the language and script identifiers and the various flags for Pre- and Post-Options are listed in detail <router-link to='/documentation'>here</router-link> along with their descriptions.</p>
    <hr/> <br/>

    <span class="code">
       from uchcharaka import transcriber as tr <br/><br/>
       transcriber = tr.Transcriber('en-gb', 'Kannada') <br/>
       tr.transcribe('I am here')<br/><br/>
       transcriber = tr.Transcriber('en-gb', 'Kannada', accuracy='High') <br/>
       tr.transcribe('I am here')<br/><br/>
       transcriber = tr.Transcriber('en-gb', 'Tamil', accuracy='low', postoptions=['plainConsonants']) <br/>
       tr.transcribe('The table is not yet packed')<br/><br/>
    </span> <br/> <br/>

  </q-page>
</template>

<script>
import { QTooltip, QPageSticky } from 'quasar'
import { ScriptMixin } from '../mixins/ScriptMixin'
import Transliterate from '../components/Transliterate'

export default {
  // name: 'PageName',
  mixins: [ScriptMixin],
  components: {
    QTooltip,
    Transliterate,
    QPageSticky
  },
  data () {
    return {
    }
  }
}
</script>

<style scoped>
h6 {
  margin-bottom: -10px;
}
h5 {
  margin-bottom: -10px;
}
table, td {
  border: 0.5px solid;
  border-collapse: collapse;
}
td {
  padding: 10px;
}
.code {
  font-family: Courier New;
}
</style>
