# -*- coding: utf-8 -*-

import re
from . import helper

class Preprocessor:
    def __init__(self, src, tgt, preoptions=[], postoptions=[], defaults=True):
        self.src = src
        self.tgt = tgt
        self.postoptions = postoptions
        self.preoptions = preoptions
        self.defaults = defaults

    def preprocess(self, Strng):
        Strng = self.default_preprocess(Strng)

        try:
            for option in self.preoptions:
                Strng = getattr(self, option)(Strng)
        except Exception as e:
            pass
            #print(e)

        return Strng

    def default_preprocess(self, Strng):
        if self.tgt in helper.IndicScripts:
            Strng = self.ipa_indic_preprocess(Strng)

        return Strng

    def ipa_indic_preprocess(self, Strng):
        ties = [
                #('ʊ','u'),
                ('eɪ', 'e͡ɪ'), ('ou', 'o͡u'), ('oʊ', 'o͡ʊ'), ('aɪ', 'a\u0361ɪ'), ('aʊ','a\u0361ʊ'),
                ('əʊ', 'ə\u0361ʊ')
                ]

        #introduce ties for Tamil for Dipthongs
        for x, y in ties:
            Strng = Strng.replace(x, y)

        #remove the ties if not Tamil or IPA
        if 'Tamil' not in self.tgt and 'IPA' not in self.tgt:
            Strng = Strng.replace('\u0361', '')

        # move stress mark before the consonant p'o -> 'po
        C = '|'.join(helper.CrunchSymbols(helper.Consonants,'IPA'))
        Diac = '|'.join(['ˈ', 'ˌ'])

        Strng = re.sub('(('+C+')+)'+'('+Diac+')',r'\3\1',Strng)

        return Strng

    def monophthongize(self, Strng):
        eRep = [('eɪ', 'eː') ]
        oRep = [('əʊ', 'oː'), ('oʊ','oː')]
        aiRep = [('aɪ', 'əɪ')]
        auRep = [('aʊ', 'əʊ')]

        if 'Devanagari' in self.tgt and 'High' not in self.tgt:
            patterns = eRep + oRep
        else:
            patterns = eRep + oRep + aiRep + auRep

        for x, y in patterns:
            # if the tie optionally appears
            Strng = re.sub(x[0]+'\u0361?'+x[1],y, Strng)

        return Strng

