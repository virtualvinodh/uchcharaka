<template>
  <q-layout view="hHr Lpr fFf">
    <q-window-resize-observable @resize="onResize" />
    <q-layout-header class="print-hide">
      <q-toolbar
        color="dark"
      >
        <q-btn
          flat
          dense
          round
          aria-label="Menu"
          @click.native="leftDrawerOpen = !leftDrawerOpen"
        >
          <q-icon name="menu" />

        </q-btn>

        <q-btn
          round
          size="lg"
          text-color="white"
          color="#5D8D89"
          to ="/transcriber"
        >
         <!-- <span class="khraoshthi-title">𐨐  </span> -->
         <span class="IPA" :style="{'font-size': '200%'}">ʁ̐</span>
       </q-btn>
        <q-toolbar-title>
          Uchcharaka <br/>
          <span><transliterate text="Transcriber" src="en-uk" :tgt="scriptRandom" sourcePreserve="Medium">
            </transliterate>             <q-tooltip>{{scriptRandom}}</q-tooltip> </span>
        </q-toolbar-title>
      </q-toolbar>
    </q-layout-header>

    <q-layout-drawer
      ref="drawer"
      v-model="leftDrawerOpen"
      side="left"
      :width="230"
      :content-class="$q.theme === 'mat' ? 'bg-grey-2' : null"
      class=""
    >
      <q-list
        no-border
        link
        inset-delimiter
      >

        <q-item to="/transcriber">
          <q-item-side icon="translate"/>
          <q-item-main label="Transcriptor"/>
        </q-item>
        <q-collapsible icon="book" label="Sample Texts"  >
            <q-item :to="'/texts/' + text.path" v-for="text in texts" :key="text.path">
              <q-item-main :label="text.name"/>
            </q-item>
        </q-collapsible>
        <hr/>
        <q-item to="/pronunciation">
          <q-item-side icon="speaker" />
          <q-item-main label="Pronunciation"/>
        </q-item>
        <q-item to="/notes">
          <q-item-side icon="comment" />
          <q-item-main label="Notes"/>
        </q-item>
        <q-item to="/python">
          <q-item-side icon="computer" />
          <q-item-main label="Python"/>
        </q-item>
         <q-item to="/about">
          <q-item-side icon="info" />
          <q-item-main label="About"/>
        </q-item>
      </q-list>
      <br/>
    </q-layout-drawer>
    <q-page-container class="page">
      <span v-if="false">
      <div :class="$q.platform.is.mobile ? 'alert2': 'alert'" v-if="visibleAlert && !$q.platform.is.mobile">
      <br/>
      <q-alert
          color="grey-7"
          icon="favorite"
          appear
          :actions="[{ label: 'Dismiss', handler: hideAlert }]"
          class="q-mb-sm"
        > Like Uchcharaka? Consider <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=LRY7AE7SXDHTN&source=url">supporting</a> it! </q-alert>
      </div>
    </span>
      <router-view/>
    </q-page-container>
    <q-layout-footer v-show="showFooter" class="print-hide">
        <q-toolbar color="tertiary" class="footer-quote">
          © 2024 <a href="http://www.virtualvinodh.com">Vinodh Rajan</a>&nbsp;&nbsp;&nbsp;vinodh@virtualvinodh.com. This software is released under GNU GPL 3.0 license.
          <q-btn
          round
          size="md"
          text-color="white"
          color="dark"
          class="print-only q-ml-sm q-mr-sm"
        >
          </q-btn>
          <div class="print-only">
            Uccharaka <br/>
            https://uchcharaka.aksharamukha.com
          </div>
        </q-toolbar>
    </q-layout-footer>

  </q-layout>
</template>

<script>
import { openURL, QLayoutFooter, QTooltip, QWindowResizeObservable, QCollapsible, QAlert, QTab, QTabs } from 'quasar'
import Transliterate from '../components/Transliterate'
import SocialSharing from 'vue-social-sharing'
import {ScriptMixin} from '../mixins/ScriptMixin'

export default {
  name: 'LayoutDefault',
  mixins: [ScriptMixin],
  components: {
    QLayoutFooter,
    QAlert,
    QTooltip,
    Transliterate,
    QWindowResizeObservable,
    QCollapsible,
    SocialSharing,
    QTab,
    QTabs
  },
  data () {
    return {
      leftDrawerOpen: true,
      hideAndroid: false,
      showFooter: true,
      randomScript: '',
      visibleAlert: true,
      texts: [
        {
          name: 'English (US)',
          path: 'en-us'
        },
        {
          name: 'English (UK)',
          path: 'en-gb'
        },
        {
          name: 'Spanish (Spain)',
          path: 'es'
        },
        {
          name: 'Spanish (Latin America)',
          path: 'es-419'
        },
        {
          name: 'Italian',
          path: 'it'
        },
        {
          name: 'Portuguese (Portugal)',
          path: 'pt-pt'
        },
        {
          name: 'Portuguese (Brazil)',
          path: 'pt-br'
        },
        {
          name: 'French',
          path: 'fr'
        },
        {
          name: 'German',
          path: 'de'
        }
      ]
    }
  },
  created: function () {
    this.randomScript = this.scriptRandom
  },
  mounted: function () {
    if (localStorage.visibleAlert) {
      this.visibleAlert = JSON.parse(localStorage.visibleAlert)
    }
    if (localStorage.hideAndroid) {
      this.hideAndroid = JSON.parse(localStorage.hideAndroid)
    }
  },
  methods: {
    openURL,
    hideAndroidHand: function () {
      this.hideAndroid = true
      localStorage.hideAndroid = JSON.stringify(this.hideAndroid)
    },
    hideAlert: function () {
      this.visibleAlert = false
      localStorage.visibleAlert = JSON.stringify(this.visibleAlert)
    },
    onResize: function (size) {
      if (size.width < 992) {
        this.showFooter = false
      } else {
        this.showFooter = true
      }
    }
  }
}
</script>

<style>
.alert {
  width: 460px;
}

.alert a:link {
  color:white;
}

.alert a:visited {
  color:white;
}

.alert2 a:link {
  color:white;
}

.alert2 a:visited {
  color:white;
}

.donate {
  display: inline-block;
}

.footer-img {
  height: 20px;
}
.footer-quote {
  font-size: 12px;
}
.page {
  margin-left: 10px;
}
.footer-quote {
  text-align: right;
  float:center;
}
.quotef {
  float: center;
}
.demo1 {
    color: white;
    background-color: #424242;
    text-shadow: 0px 1px 0px rgba(0,0,0,.5);
}
.social {
  text-align: center;
}
.q-body-1 {
  line-height: 1.75em;
}

.title-ka {
  font-size: 25px;
  margin-top: 20px;
  margin-left: 5px;
}

@import url('../statics/fonts.css');

</style>
