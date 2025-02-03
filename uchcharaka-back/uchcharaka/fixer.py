from . import helper
from uchcharaka.ScriptMap.MainIndic import Urdu, Malayalam,Sinhala
import re

class Fixer:
    def __init__(self, src, tgt, preoptions=[], postptions=[]):
        self.src = src
        self.tgt = tgt
        self.postoptions = preoptions
        self.preoptions = postptions

    # Fixing the Indic Ouput for the standard corrections
    # Indic Fix are mandatory corrections to the immediate ouput.
    def fix(self, Strng):
        vir = helper.CrunchList('ViramaMap', self.tgt)[0]

        Strng = Strng.replace(vir + '_', vir)

        try:
            fixerFunction = "Fix"+self.tgt
            for suffix in helper.suffixes:
                fixerFunction = fixerFunction.replace(suffix, '')
            Strng = getattr(self, fixerFunction)(Strng)
        except Exception as e:
            pass
            print(e)

        Strng = Strng.replace('\u02BD','')

        return Strng

    def FixKannada(self, Strng):
        #fix Transcribe transcription
        Strng = Strng.replace('\u0CA8\u0CCD\u0CB8\u0CCD\u0C95\u0CCD\u0CB0', \
                              '\u0CA8\u0CCD\u0CB8\u0CCD\u200C\u0C95\u0CCD\u0CB0')

        #fix scry
        Strng = Strng.replace('\u0CCD\u0C95\u0CCD\u0CB0\u0CC8', '\u0CCD\u200C\u0C95\u0CCD\u0CB0\u0CC8')

        return Strng

    def FixTamil(self, Strng):
        ListVS = '(' + '|'.join(helper.CrunchSymbols(helper.VowelSigns,self.tgt)) + ')'

        Strng = re.sub('(·)'+ListVS, r'\2\1', Strng)

        return Strng

    def FixTamilPhonetic(self, Strng):
        VedicSign = ['॑', '॒', '᳚']
        TamilDiacritic = ['ʼ', 'ˮ', '꞉']#, '²', '³', '⁴', '₂', '₃', '₄']

        for x in TamilDiacritic:
            for y in VedicSign:
                Strng = Strng.replace(x + y, y + x)

        return Strng

    # Urdu - Shadda, Final E
    def FixUrdu(self, Strng):
        # .replace(u'\u064E','')

        #print('I am here in Fixing Urdu')

        Strng = Strng.replace('\u02BD','')

        vir = helper.CrunchSymbols(helper.VowelSigns,self.tgt)[0]

        ConUnAsp = [helper.CrunchList('ConsonantMap', self.tgt)[x] for x in [0,2,5,7,10,12,15,17,20,22,4,9,14,19,24]+list(range(25,33))] # Add SemiVowels & Nukta Consonants
        ConUnAsp = ConUnAsp + helper.CrunchList('SouthConsonantMap',self.tgt) + helper.CrunchList('NuktaConsonantMap',self.tgt)

        ## Add word-final E, Short A sign

        ShortVowels = '|'.join(['\u0652','\u064E','\u0650','\u064F'])
        a = '\u064E'
        ya = '\u06CC'
        va  = '\u0648'
        yaBig = '\u06D2'
        Aa = Urdu.VowelSignMap[0]

        #Strng = Strng.replace(u'\u064E'+ya,ya)
        #Strng = Strng.replace(u'\u064E'+va,va)

        ## Fixing Hamza

        ListVS = '(' + '|'.join(helper.CrunchSymbols(helper.VowelSigns,self.tgt)) + ')'
        ListV = '(' + '|'.join(helper.CrunchSymbols(helper.Vowels,self.tgt)) + ')'
        ListVSA = '(' + '|'.join(helper.CrunchSymbols(helper.VowelSigns,self.tgt)+[a]) + ')'

        ListC = '(' + '|'.join(helper.CrunchSymbols(helper.Consonants,self.tgt)) + ')'
        # Fix NunGhunna
        Strng = re.sub('(\u06BA\u02BD?)' + ListC, '\u0646\u0658' + r'\2', Strng)

        hamzaFull = "\u0621"
        hamzaChair = "\u0626"

        Strng = re.sub(ListVS + ListV, r'\1' + hamzaFull + r'\2', Strng)
        Strng = re.sub(ListV + ListV, r'\1' + hamzaFull + r'\2', Strng)
        Strng = re.sub('('+a+')' + ListV +'(?!' + ListVSA + ')'   , r'\1' + hamzaFull + r'\2', Strng)

        Strng = re.sub('('+a+')'+'('+ShortVowels+')',r'\2',Strng)
        Strng = re.sub('(?<!'+Aa+')'+'('+a+')'+'('+va+'|'+ya+')'+'(?!'+ ShortVowels +')',r'\2',Strng)
        ListC = '|'.join(helper.CrunchSymbols(helper.Consonants,self.tgt)).replace(a,'')
        Ayoga = '|'.join(Urdu.AyogavahaMap[0] + Urdu.AyogavahaMap[1])

        Strng = Strng.replace(ya,yaBig)
        Strng = re.sub('('+yaBig+')'+'(?='+'|'.join(ConUnAsp)+ShortVowels+')',ya,Strng)
        Strng = re.sub('('+yaBig+')'+'('+ListC+')',ya+r'\2',Strng)
        Strng = re.sub('('+yaBig+')'+'('+Ayoga+')',ya+r'\2',Strng)

        Strng = Strng.replace('\u0650'+yaBig,'\u0650'+ya)

        #Strng = Strng.replace(a+Urdu.VowelSignMap[0],Urdu.VowelSignMap[0]) ## remove a sign from consonants

        ## ye ## yezu ## Fix this

        ## Adding Gemination of Consonant

        ConAsp   = [helper.CrunchList('ConsonantMap', self.tgt)[x] for x in [1,3,6,8,11,13,16,18,21,23]]
        ConUnAsp_a =  [x.replace('\u064e','') for x in ConUnAsp]

        Strng = re.sub('('+'|'.join(ConUnAsp_a)+')'+'('+vir+')'+r'\1',r'\1'+helper.Gemination[self.tgt],Strng)

        ## Move Shadda to the ha do=chasmee
        ## katthu -> کَتھُّ
        Strng = re.sub('(.)(ّ)(\u06BE)', r'\1\3\2', Strng)

        ## Fix

        Strng = Strng.replace('ےے', 'یے')
        Strng = Strng.replace('ےی', 'یی')
        Strng = Strng.replace('ےْ', 'یْ')

        #http://www.columbia.edu/~mk2580/urdu_section/handouts/hamza.pdf

        # Hamza on ya
        Strng = Strng.replace('ءاِی','\u0626\u0650\u06CC')
        Strng = Strng.replace('ءاے', 'ئے')

        Strng = Strng.replace('ءای', 'ئی')

        # Hamza on waw
        Strng = Strng.replace('ءاو','ؤ') #o
        Strng = Strng.replace('ءاُو', '\u0624\u064F') #long u

        Strng = Strng.replace('ءاُ', '\u0624\u064F') #short u

        # kau/ kaU

        Strng = re.sub('('+hamzaFull+')(اُو)', r'\1'+'\u0624\u064F', Strng)
        Strng = re.sub('('+hamzaFull+')(اُ)', r'\1'+'\u0624\u064F', Strng)

        Strng = re.sub('('+hamzaFull+')(او)', r'\1'+'\u0624', Strng)

        # Hamza on ya for short i
        Strng = Strng.replace('ءاِ', '\u0626\u0650')
        Strng = Strng.replace('ئِءآ', '\u0626\u0650\u0627')

        Strng = re.sub('('+hamzaFull+')(\u0627\u0650)', r'\1'+'\u0626\u0650', Strng)

        # for gae kae etc
        Strng = re.sub('('+hamzaFull+')(ا)(ے|ی)', r'\1'+'\u0626' + r'\3', Strng)

        ## Fix Double Hamza to Single Hamza

        Strng = Strng.replace('ئِئ', 'ئِ')
        Strng = Strng.replace('ئِؤ', 'ئِو')

        ## Fix Retroflex with combining characters
        Strng = Strng.replace('ࣇ', 'لؕ')

        if self.tgt == 'Shahmukhi':
            #aspirated nasals and liquids
            Strng = re.sub('(ن|م|ی|ر|ل|و)(\u0652)(ہ)',r'\1'+'\u06BE', Strng)

        # Fix word-final ha

        Strng = self.PersoArabicPuntuation(Strng)

        return Strng

    def PersoArabicPuntuation(self, Strng):
        # Punctuation
        for x,y in zip([',','?',';'],['،','؟','؛']):
            Strng = Strng.replace(x,y)
        Strng = Strng.replace(".", "۔")

        return Strng

    def FixSinhala(self, Strng):
        Strng = self.SinhalaDefaultConjuncts(Strng)

        Strng = Strng.replace("\u0DA2\u0DCA\u0DA4","\u0DA5")
        Strng = Strng.replace("(අ)(අ)","(ආ)")

        return Strng

    def FixMalayalam(self, Strng):
        Strng = self.MalayalamChillu(Strng)

        vir = Malayalam.ViramaMap[0]
        Strng = re.sub('('+vir+')'+ '(ര̣)', r'\1' + '\u200C' + r'\2', Strng)

        return Strng

    def SinhalaDefaultConjuncts(self, Strng):
        vir = Sinhala.ViramaMap[0]
        YR = '|'.join(Sinhala.ConsonantMap[25:27])

        Strng = re.sub('('+vir+')'+'('+YR+')',r'\1'+'\u200D'+r'\2',Strng)
        Strng = re.sub('('+YR[2]+')'+'('+vir+')'+'('+'\u200D'+')'+'('+YR[0]+')',r'\1\3\2\3\4',Strng)

        Strng = Strng.replace(Sinhala.ConsonantMap[7]+Sinhala.ViramaMap[0]+Sinhala.ConsonantMap[9],'\u0DA5')
        Strng = Strng.replace(Sinhala.ConsonantMap[0]+vir+Sinhala.ConsonantMap[30],Sinhala.ConsonantMap[0]+vir+'\u200D'+Sinhala.ConsonantMap[30])

        ## KSHA

        Strng = Strng.replace('ර‍්‍ය', 'ර්ය')
        Strng = Strng.replace('ර්‍ර', 'ර්ර')

        return Strng

    def MalayalamChillu(self, Strng):
        Chillus=['\u0D7A','\u0D7B','\u0D7C','\u0D7D','\u0D7E', 'ഩ‍്']

        ListC = '(' + '|'.join(helper.CrunchSymbols(helper.CharactersNV,self.tgt) + ['ഽ']) + ')'

        vir = Malayalam.ViramaMap[0]
        ConVir =[
                Malayalam.ConsonantMap[14]+vir,
                Malayalam.ConsonantMap[19]+vir,
                Malayalam.ConsonantMap[26]+vir,
                Malayalam.ConsonantMap[27]+vir,
                Malayalam.SouthConsonantMap[0]+vir,
                'ഩ്'
                ]

        ## may be include ha ?
        CList = [
                Malayalam.ConsonantMap[10:15]+Malayalam.ConsonantMap[24:26]+Malayalam.ConsonantMap[28:29],
                Malayalam.ConsonantMap[15:20]+Malayalam.ConsonantMap[24:27]+Malayalam.ConsonantMap[28:29]+['റ'],
                Malayalam.ConsonantMap[25:27],
                Malayalam.ConsonantMap[20:21] + Malayalam.ConsonantMap[24:26] + Malayalam.ConsonantMap[27:29],
                Malayalam.SouthConsonantMap[0:1]+Malayalam.ConsonantMap[25:27],
                Malayalam.ConsonantMap[15:20]+Malayalam.ConsonantMap[24:27]+Malayalam.ConsonantMap[28:29]+['റ']
                ]

        for i in range(len(Chillus)):
            #print '(?<!'+'['+vir+''.join(Chillus)+']'+')'+'('+ConVir[i]+')'+'(?!['+''.join(CList[i])+'])'
            Strng = re.sub(ListC + helper.VedicSvaras + '('+ConVir[i]+')'+'(?!['+''.join(CList[i])+'])',r'\1\2' + Chillus[i],Strng)
            Strng = re.sub(ListC + helper.VedicSvaras + '('+ConVir[i]+')'+'(?=(['+''.join(CList[i])+'])' + vir + r'\4' + ')',r'\1\2' + Chillus[i],Strng)

        ## remove _ appearing due to the preserve chillu option
        Strng = re.sub('(?<!ത്)ˍ', '', Strng)

        return Strng