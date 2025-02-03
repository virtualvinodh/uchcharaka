# -*- coding: utf-8 -*-

### Introduce Nasal to Anusvara for scripts lacking nasal letters but having Anusvara/Chandrabindu

import importlib, string
import re
from functools import reduce

# Crunch Symbols

# Sort Functions
def lenSort(x,y):
    if(len(x[0]) > len(y[0])):
        return -1
    else:
        return 0

def ScriptPath(Script):
    if Script in IndicScripts:
        return 'uchcharaka.ScriptMap.MainIndic.'+Script
    elif Script in LatinScripts:
        return 'uchcharaka.ScriptMap.Roman.'+Script

def retCharList(charList):
    return globals()[charList]

def CrunchSymbols(Part,Script):
    ModScript = importlib.import_module(ScriptPath(Script))
    return reduce(lambda x,y : x+y,[getattr(ModScript,Var) for Var in Part])

def CrunchList(List,Script):
    try:
      ModScript = importlib.import_module(ScriptPath(Script))
    except:
      import logging
      logging.exception('The script ' + Script + ' cannot be found')
      return ''

    return getattr(ModScript,List)

#Introduce in all Latin Conversions
def EscapeChar(Strng):
    punct = "".join(['\\'+x for x in string.punctuation])

    return re.sub('('+punct+')',r'\\'+r'\1',Strng)

# Collection of Symbols
VedicSvaras = '('+ '|'.join(['᳚', '॑', '॒']) + ')?'
VedicSvarasList = ['᳚', '॑', '॒']

Vowels = ['VowelMap','SouthVowelMap','ModernVowelMap','SinhalaVowelMap', 'IPAVowelMap']
VowelSignsNV = ['VowelSignMap','SouthVowelSignMap','ModernVowelSignMap','SinhalaVowelSignMap', 'IPAVowelSignMap']
VowelSigns = ['ViramaMap','VowelSignMap','SouthVowelSignMap','ModernVowelSignMap','SinhalaVowelSignMap', 'IPAVowelSignMap']
CombiningSigns = ['AyogavahaMap','NuktaMap']
Consonants = ['ConsonantMap','SouthConsonantMap','NuktaConsonantMap','SinhalaConsonantMap', 'IPAConsonantMap']

Signs = ['SignMap']
Numerals = ['NumeralMap']
Aytham =['Aytham']
om = ['OmMap']
virama = ['ViramaMap']

Inter = "Inter"

Characters = Vowels + VowelSigns + CombiningSigns + Consonants
CharactersNV = Vowels + VowelSignsNV + CombiningSigns + Consonants

Diacritics = ['ʽ', '\u00B7', '\u00B9','\u00B2','\u00B3','\u2074','\u2081','\u2082','\u2083','\u2084', '\u1DDC', '\u1DDA', '\u036d', '\u0369', '\u1DEE', '\u1DE8', '\u1DE3', '\u1DF1', '\u1DEB', '\u1de6', '\u0368\u036A', '\u036D\u036A', '\u1DD9', '\u0368', '\u036F', '\u1DDB', '\u0323', '\u036A']
DiacriticsRemovable = ['ʼ', 'ˇ', 'ˆ', '˘', '\u00B7']
DiacriticsRemovableTamil = ['ˇ', 'ˆ', '˘', '\u00B7']

ScriptAll = ['Aytham', 'Signs', 'CombiningSigns', 'VowelSigns', 'Vowels', 'Consonants', 'Numerals']

inaccurate_scripts = ['IPA', 'Brahmi', 'Grantha', 'Sharada', 'Urdu', 'Sinhala']

IndicScriptsBase = [
               'Devanagari',
               'Telugu',
               'Kannada',
               'Malayalam',
               'TamilPhonetic',
               'Tamil',
               'Sinhala',
               'Urdu'
               ]

suffixes = ['Low', 'Medium', 'High']
IndicScripts = [f"{script}{suffix}" for script in IndicScriptsBase for suffix in suffixes] + IndicScriptsBase

LatinScripts = ['Inter','IPA']

Gemination =  {
               'Urdu': '\u0651'
              }

def add_additional_chars(script_char_map, file_script):
    pass