# -*- coding: utf-8 -*-

from . import GeneralMap as GM
import re
import espeak_py as espeak
from inspect import getmembers, isfunction

def PreProcess(Strng,Source,Target,postoptions,preoptions):
    if Source != 'IPA':
        Strng = espeak.text_to_phonemes(Strng, Source)

    if Target != 'IPA':
        Approx = [
                ('ʊ','u'),
                ('eɪ', 'e͡ɪ'), ('ou', 'o͡u'), ('aɪ', 'a\u0361ɪ')
                ]

        for x, y in Approx:
            Strng = Strng.replace(x, y)

        #Strng = Strng.replace('ˈ', '').replace("ˌ", "")

        if 'es' in Source or 'fr' in Source:
            Strng = re.sub('t(?!ʃ)', 't̪', Strng)
            Strng = re.sub('d(?!ʒ)', 'd̪', Strng)

    C = '|'.join(GM.CrunchSymbols(GM.Consonants,'IPA'))
    Diac = '|'.join(['ˈ', 'ˌ'])

    Strng = re.sub('('+C+')'+'('+Diac+')',r'\2\1',Strng)

    return Strng

def RomanPreFix(Strng,Source):
    DepV = '\u1E7F'
    Asp = '\u02B0'

    Vir = GM.CrunchList("ViramaMap", Source)[0]
    Nuk = GM.CrunchList("NuktaMap", Source)[0]
    VowelA = GM.CrunchSymbols(['VowelMap'],Source)[0]

    ListV = '|'.join(GM.CrunchSymbols(GM.VowelSigns,Source))
    ListC = '|'.join(GM.CrunchSymbols(GM.Consonants,Source))

    Strng = re.sub('('+ListC+')'+'(?!'+ListV+'|'+VowelA+')',r'\1'+DepV+Vir,Strng)

    Strng = re.sub('('+ListC+'|'+Nuk+')'+'('+ListV+')',r'\1'+DepV+r'\2',Strng)

    Strng = re.sub('(?<='+ListC+')'+'('+VowelA+')',r'',Strng)

    return Strng

