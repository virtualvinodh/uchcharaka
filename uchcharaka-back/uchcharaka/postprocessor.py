# -*- coding: utf-8 -*-

from . import helper
from uchcharaka.ScriptMap.MainIndic import Malayalam,Sinhala
import re

class PostProcessor:
    def __init__(self, src, tgt, preoptions=[], postoptions=[], defaults=True):
        self.src = src
        self.tgt = tgt
        if defaults:
            self.postoptions = self.get_default_postprocesses() + postoptions
        else:
            self.postoptions = postoptions
        self.preoptions = preoptions
        self.defaults = defaults

    def get_default_postprocesses(self):
        Options = []
        if 'Telugu' in self.tgt:
            Options = ['NasalToAnusvara','MToAnusvara']

        elif 'Kannada' in self.tgt:
            Options = ['NasalToAnusvara','MToAnusvara']

        elif 'Malayalam' in self.tgt:
            Options = ['MalayalamAnusvaraNasal', 'MToAnusvara']

        elif 'Tamil' in self.tgt:
            Options = ['TamilNaToNNa']

        elif 'Devanagari' in self.tgt:
             Options = ['NasalToAnusvara', 'removeWordEndVirama']

        if ('Devanagari' in self.tgt or 'Telugu' in self.tgt \
            or 'Kannada' in self.tgt) and ('High' not in self.tgt):
            Options += ['nganjaApprox']

        return Options

    def postprocess(self,Strng):
        try:
            for options in self.postoptions:
                Strng = getattr(self, options)(Strng)
        except AttributeError as e:
            pass
            #print('vinodh', e)

        Strng = self.default_postprocess(Strng)

        # Shifting Vowel Signs and Diacritics
        # க²ா ->  கா²
        Strng = self.ShiftDiacritics(Strng)

        return Strng

    ## This is processing that's done after the post-processing steps
    def default_postprocess(self, Strng):
        Strng = Strng.replace('\u034F', '') ## remove token characters for specialized processing
        return Strng

    #Shift Diacritics after vowel signs
    def ShiftDiacritics(self, Strng):
        VS = '|'.join(helper.CrunchSymbols(helper.VowelSigns,self.tgt))
        Diac = '|'.join(helper.Diacritics)
        VedicSign = ''.join(['॑', '॒', '᳚'])
        chandraAnu = '([' + helper.CrunchList('AyogavahaMap',self.tgt)[0] + \
            helper.CrunchList('AyogavahaMap',self.tgt)[1] + '])'
        Strng = re.sub('('+Diac+')'+'('+VS+')',r'\2\1',Strng)

        if 'Tamil' in self.tgt:
            Strng = Strng.replace( '³்', '்³',)
            VedicSign = ['॑', '॒', '᳚']

            for x in helper.TamilDiacritics:
                for y in VedicSign:
                    Strng = Strng.replace(x + y, y + x)

        if 'Malayalam' in self.tgt:
            dot = '(\u0323)'
            #Strng = re.sub(dot + '(\u03dc)', r'\2\1', Strng)
            Strng = re.sub(dot + '(['+VedicSign+']+)', r'\2\1', Strng)
            Strng = re.sub(dot + chandraAnu, r'\2\1', Strng)

        if 'Telugu' in self.tgt or 'Devanagari' in self.tgt or 'Malayalam' in self.tgt:
            Strng = re.sub('(['+VedicSign+']+)'+chandraAnu, r'\2\1', Strng)
        if 'Malayalam' in self.tgt:
            Strng = re.sub('(\u0323)([\u0D3B\u0d3C])'+chandraAnu, r'\2\3\1', Strng)
        if 'TamilPhonetic' in self.tgt:
            Strng = re.sub('(\u033C)([\u1DEE\u1DDC\u036D])',r'\2\1', Strng)

        return Strng

    def gdbDifferentiationTamilPhonetic(self, Strng):
        Strng = re.sub('[\u1DDC\u1DEE\u036D]', '', Strng)

        return Strng

    def gdbDifferentiationTamil(self, Strng):
        Strng = re.sub('[ᵏᵗᵖ]', '', Strng)

        return Strng

    def removeDifferentiation(self, Strng):
        Strng = Strng.replace('ஜᷦ', 'ஃஜ').replace('பᷫ', 'ஃப')

        for dia in helper.Diacritics:
            Strng = Strng.replace(dia, '')

        return Strng

    def removeNuktaTelugu(self, Strng):
        Strng = Strng.replace('\u0C3C', '')
        return Strng

    def removeWordEndVirama(self, Strng):
        if 'showWordEndVirama' not in self.postoptions:
            vir = '\u094D'

            Strng = self.showFinalSchwa(Strng)

            Strng = re.sub(f'({vir})(?=(\s))', '', Strng)
            Strng = re.sub(f'({vir})$', '', Strng)

            print('getting called')

        return Strng

    def showFinalSchwa(self, Strng):
        ListC = '('+"|".join(sorted(helper.CrunchSymbols(helper.Consonants,self.tgt))) + ')'
        ListVS = '('+"|".join(sorted(helper.CrunchSymbols(helper.VowelSigns,self.tgt))) + ')'

        Strng = re.sub(f'{ListC}(\s)(?!{ListVS})', r'\1'+'ऽ '+r'\2', Strng)
        Strng = re.sub(f'{ListC}$(?!{ListVS})', r'\1'+'ऽ', Strng)

        return Strng

    def nganjaApprox(self, Strng):
        vir =  helper.CrunchList('ViramaMap', self.tgt)[0]
        nga =  helper.CrunchList('ConsonantMap', self.tgt)[4]
        anu =  helper.CrunchList('AyogavahaMap', self.tgt)[1]
        ga =   helper.CrunchList('ConsonantMap', self.tgt)[2]

        nja = helper.CrunchList('ConsonantMap', self.tgt)[9]
        na = helper.CrunchList('ConsonantMap', self.tgt)[19]
        ya = helper.CrunchList('ConsonantMap', self.tgt)[25]

        if 'Devanagari' in self.src:
            Strng = Strng.replace(nga+vir, anu+ga+vir)
        else:
            Strng = Strng.replace(nga, anu+ga)

        Strng = Strng.replace(nja, na+vir+ya)

        return Strng

    #show Schwa
    def ShowSchwaHindi(self, Strng):
        from . import PreProcess as PreP
        Strng = PreP.RemoveSchwaHindi(Strng, True)
        return Strng

    def KannadaNormalCandrabindu(self, Strng):
        Strng = Strng.replace('\u0C80', '\u0C81')

        return Strng

    def TeluguRemoveNukta(self, Strng):
        Strng = Strng.replace('\u0C3C', '')

        return Strng

    def removeDiacritics(self, Strng):
        diacritics = ['\u0331', '\u0306', '\u0323', '\u035F', '\u0324', '\u035F', '\u0307', '\u0301', '\u0303', '\u0310', '\u0306', '\u0302', '\u0304']

        for dia in diacritics:
            Strng = Strng.replace(dia, '')

        vowelDia = ['а̄', 'ӣ', 'ӯ', 'ӗ']
        vowel = ['\u0430', '\u0438', '\u0443', '\u044D']

        for x, y in zip(vowelDia, vowel):
            Strng = Strng.replace(x, y)

        return Strng

    def DevanagariACandra(self, Strng):
        Strng = Strng.replace('ऍ', 'ॲ')

        return Strng

    def dotReph(self, Strng):
        ListC = '('+"|".join(sorted(helper.CrunchSymbols(helper.Consonants,"Malayalam"))) + ')'

        Strng = re.sub('(?<!്)' + 'ർ' + ListC,'ൎ' + r'\1', Strng)
        Strng = re.sub('(?<!്)' +'ര്' + ListC,'ൎ' + r'\1', Strng)

        return Strng

    def TamilNaToNNa(self, Strng):
        na = helper.CrunchList('ConsonantMap', self.tgt)[19]
        nna = helper.CrunchList('SouthConsonantMap', self.tgt)[3]
        vir = helper.CrunchList('ViramaMap', self.tgt)[0]
        ta = helper.CrunchList('ConsonantMap', self.tgt)[15]

        ListV = '|'.join(helper.CrunchSymbols(helper.Vowels+helper.VowelSigns+helper.Consonants,self.tgt)+[helper.CrunchList('SignMap', self.tgt)[0].replace('(','\(').replace(')','\)')])

        Strng = re.sub('('+ListV+')'+ helper.VedicSvaras + '('+na+')' + '(?!' + vir + ta + ')',r'\1\2'+nna,Strng)
        Strng = re.sub('('+ListV+')'+ helper.VedicSvaras + '('+na+')' + '(?!' + vir + ta + ')',r'\1\2'+nna,Strng)

        Strng = re.sub('(²|³|⁴)'+ helper.VedicSvaras + '('+na+')' + '(?!' + vir + ta + ')',r'\1\2'+nna,Strng)
        Strng = re.sub('(²|³|⁴)'+ helper.VedicSvaras + '('+na+')' + '(?!' + vir + ta + ')',r'\1\2'+nna,Strng)

        #Strng = re.sub('(²|³|⁴)'+'('+na+')',r'\1'+nna,Strng)

        #Strng = re.sub('(\s)(ன)', r'\1' + 'ந', Strng)
        #Strng = re.sub('(\.)(ன)', r'\1' + 'ந', Strng)
        #Strng = re.sub('^ன', 'ந', Strng)

        Strng = re.sub("(?<=ஶ்ரீ)(ன)(?!" + vir + ")", "ந", Strng)

        return Strng

    # കൽന് കത്ല് ക്ഷേത്ര് കൻല് - Check this

    def InsertGeminationSign(self, Strng): #Fix this
        vir = helper.CrunchSymbols(helper.VowelSigns,self.tgt)[0]
        ConUnAsp = [helper.CrunchList('ConsonantMap', self.tgt)[x] for x in [0,2,5,7,10,12,15,17,20,22,4,9,14,19,24,25,26,27,28,29,30,31,32]]
        ConUnAsp = ConUnAsp + helper.CrunchList('SouthConsonantMap',self.tgt) + helper.CrunchList('NuktaConsonantMap',self.tgt)
        ConAsp   = [helper.CrunchList('ConsonantMap', self.tgt)[x] for x in [1,3,6,8,11,13,16,18,21,23]]
        ConOthrs = [helper.CrunchList('ConsonantMap', self.tgt)[x] for x in [0,2,5,7,10,12,15,17,20,22,4,9,14,19,24]]

        Strng = re.sub('('+'|'.join(ConUnAsp)+')'+'('+vir+')'+r'\1',helper.Gemination[self.tgt]+r'\1',Strng)

        for i in range(len(ConAsp)):
            Strng = re.sub('('+ConUnAsp[i]+')'+'('+vir+')'+'('+ConAsp[i]+')',helper.Gemination[self.tgt]+r'\3',Strng)

        return Strng

    def ReverseGeminationSign(self, Strng): #Fix this
        vir = helper.CrunchSymbols(helper.VowelSigns,self.tgt)[0]
        ConUnAsp = [helper.CrunchList('ConsonantMap', self.tgt)[x] for x in [0,2,5,7,10,12,15,17,20,22,4,9,14,19,24,25,26,27,28,29,30,31,32]]
        ConUnAsp = ConUnAsp + helper.CrunchList('SouthConsonantMap',self.tgt) + helper.CrunchList('NuktaConsonantMap',self.tgt)
        ConAsp   = [helper.CrunchList('ConsonantMap', self.tgt)[x] for x in [1,3,6,8,11,13,16,18,21,23]]
        ConOthrs = [helper.CrunchList('ConsonantMap', self.tgt)[x] for x in [0,2,5,7,10,12,15,17,20,22,4,9,14,19,24]]

        if self.tgt == 'Gurmukhi':
            Strng = Strng.replace('ੱਸ਼਼', 'ਸ਼਼੍ਸ਼਼')

        Strng = re.sub('(' + helper.Gemination[self.tgt] + ')' + '('+'|'.join(ConUnAsp)+')', r'\2' + vir + r'\2', Strng)

        for i in range(len(ConAsp)):
            Strng = re.sub('(' + helper.Gemination[self.tgt] + ')' + '(' + ConAsp [i] +')', ConUnAsp[i] + vir + r'\2', Strng)

        return Strng

    def NasalToAnusvara(self, Strng):
        ListN = [helper.CrunchSymbols(helper.Consonants, self.tgt)[x] for x in [4,19, 9,19,14,19,19,24]]
        ListC = [
                '|'.join(helper.CrunchList('ConsonantMap', self.tgt)[0:4]),
                '|'.join(helper.CrunchList('ConsonantMap', self.tgt)[0:4]), # to fix ಚಿನ್ಕ್ವ಼ೆ
                '|'.join(helper.CrunchList('ConsonantMap', self.tgt)[5:9]),
                '|'.join(helper.CrunchList('ConsonantMap', self.tgt)[5:9]), # to fix ಪನ್ಚ್
                '|'.join(helper.CrunchList('ConsonantMap', self.tgt)[10:14]),
                '|'.join(helper.CrunchList('ConsonantMap', self.tgt)[10:14]), # To fix ಐಲನ್ಡ್ -> ಐಲಂಡ್
                '|'.join(helper.CrunchList('ConsonantMap', self.tgt)[15:19]),
                '|'.join(helper.CrunchList('ConsonantMap', self.tgt)[20:24]),
                ]
        ListCAll = '(' + '|'.join(helper.CrunchSymbols(helper.Characters, self.tgt)) + ')'

        vir = helper.CrunchSymbols(helper.VowelSigns,self.tgt)[0]
        Anu = helper.CrunchSymbols(helper.CombiningSigns,self.tgt)[1]

        for i in range(len(ListN)):
            #print '('+ListN[i]+')'+'('+vir+')'+'('+ListC[i]+')'
            Strng = re.sub(ListCAll + helper.VedicSvaras + '(?<!' + vir + ')' + '('+ListN[i]+')' +'('+vir+')'+'('+ListC[i]+')',r'\1\2'+Anu+r'\5',Strng)
            Strng = re.sub(ListCAll + helper.VedicSvaras + '(?<!' + vir + ')' + '('+ListN[i]+')' +'('+vir+')'+'('+ListC[i]+')',r'\1\2'+Anu+r'\5',Strng)

        for svara in helper.VedicSvarasList:
            Strng = Strng.replace(svara + Anu, Anu + svara)

        ## So that candrao/candra + anusvara does not get confused by candrabindu
        ## replace anusvara with candrabindu
        ## टॅं -> टॅँ
        if 'Devanagari' in self.tgt:
            Strng = re.sub('([ऑऍॲॅै])(ं)', r'\1'+'ँ', Strng)
        elif 'Kannada' in self.tgt:
            Strng = re.sub('(' + 'ಂ)('+ helper.VedicSvaras +'?)(ಜ಼' + ')' , r'\3' + 'ನ್' + r'\4', Strng)
        elif 'Telugu' in self.tgt:
            Strng = re.sub('(' + 'ం)('+ helper.VedicSvaras +'?)(జ఼' + ')' , r'\3' + 'న్' + r'\4', Strng)

        return Strng

    def AnusvaraToNasal(self, Strng):
        nukta = helper.CrunchList('NuktaMap', self.tgt)[0]

        ListN = [helper.CrunchSymbols(helper.Consonants, self.tgt)[x] for x in [4,9,14,19,24]]
        ListC = [
                '|'.join(helper.CrunchList('ConsonantMap', self.tgt)[0:4]),
                '|'.join(helper.CrunchList('ConsonantMap', self.tgt)[5:9]),
                '|'.join(helper.CrunchList('ConsonantMap', self.tgt)[10:14]),
                '|'.join(helper.CrunchList('ConsonantMap', self.tgt)[15:19]),
                '|'.join(helper.CrunchList('ConsonantMap', self.tgt)[20:24]),
                ]
        vir = helper.CrunchSymbols(helper.VowelSigns,self.tgt)[0]
        Anu = helper.CrunchSymbols(helper.CombiningSigns,self.tgt)[1]

        for i in range(len(ListN)):
            Strng = re.sub('('+Anu+')'+ helper.VedicSvaras + '('+ListC[i]+')(?!' + nukta + ')',ListN[i]+vir+r'\2\3',Strng)

            if self.tgt == "Tamil":
                Strng = re.sub('(ம்)'+ helper.VedicSvaras + '(ʼ)' + '('+ListC[i]+')',ListN[i]+vir+r'\2\4',Strng)

        return Strng

    def MalayalamAnusvaraNasal(self, Strng):
        ListCAll = '(' + '|'.join(helper.CrunchSymbols(helper.Characters, self.tgt)) + ')'

        ListNNasal = [Malayalam.ConsonantMap[x] for x in [4,9,14,19,24]]
        ListCNasal = [
                '|'.join(Malayalam.ConsonantMap[0:1]),
                '|'.join(Malayalam.ConsonantMap[5:8]),
                '|'.join(Malayalam.ConsonantMap[10:14]),
                '|'.join(Malayalam.ConsonantMap[15:19]),
                '|'.join(Malayalam.ConsonantMap[20:21]),
                ]

        ListNAnu = [Malayalam.ConsonantMap[x] for x in [4,24]]
        ListCAnu = [
                '|'.join(Malayalam.ConsonantMap[1:4]),
                '|'.join(Malayalam.ConsonantMap[21:24]),
                ]

        vir = Malayalam.ViramaMap[0]
        Anu = Malayalam.AyogavahaMap[1]

        Chillus=['\u0D7A','\u0D7B','\u0D7C','\u0D7D','\u0D7E', 'ഩ‍്']

        for i in range(len(ListNNasal)):
            Strng = re.sub('('+Anu+')'+'('+ListCNasal[i]+')',ListNNasal[i]+vir+r'\2',Strng)

        for i in range(len(ListNAnu)):
            Strng = re.sub(ListCAll + helper.VedicSvaras + '(?<!' + vir + ')'+'(?<![' + ".".join(Chillus) + '])(?<!' + vir +')' + '('+ListNAnu[i]+')'+'('+vir+')'+'('+ListCAnu[i]+')',r'\1\2'+Anu+r'\5',Strng)

        return Strng

    ## Check Namna, ramya -> Malayalam; fix
    def MToAnusvara(self, Strng):
        M = helper.CrunchList('ConsonantMap', self.tgt)[24] + helper.CrunchList('ViramaMap',self.tgt)[0]
        vir = helper.CrunchList('ViramaMap',self.tgt)[0]
        Anusvara = helper.CrunchList('AyogavahaMap',self.tgt)[1]
        ListC = '|'.join(helper.CrunchSymbols(helper.Characters, self.tgt))

        Chillus= '|'.join([vir, '\u0D7A','\u0D7B','\u0D7C','\u0D7D','\u0D7E'])

        ListCAll = '(' + '|'.join(helper.CrunchSymbols(helper.Characters, self.tgt)) + ')'

        Strng = re.sub(ListCAll + helper.VedicSvaras + '(?<!' + vir + ')'+'('+M+')'+'(?!'+ListC+')',r'\1\2'+Anusvara,Strng)

        for svara in helper.VedicSvarasList:
            Strng = Strng.replace(svara + Anusvara, Anusvara + svara)

        #Strng = Strng.replace(M,Anusvara)

        return Strng

    def RemoveDiacritics(self, Strng):
        for x in helper.DiacriticsRemovable:
            Strng = Strng.replace(x,'')

        return Strng

    def RemoveDiacriticsTamil(self, Strng):
        for x in helper.DiacriticsRemovableTamil:
            Strng = Strng.replace(x,'')

        return Strng

    def TamilSubScript(self, Strng):
        SuperScript = ['\u00B9', '\u00B2', '\u00B3','\u2074']
        SubScript = ['\u2081','\u2082','\u2083','\u2084']

        for x,y in zip(SuperScript,SubScript):
            Strng = Strng.replace(x,y)

        return Strng

    def SinhalaConjuncts(self, Strng):
        ListC = Sinhala.ConsonantMap + [Sinhala.SouthConsonantMap[0]]
        vir = Sinhala.ViramaMap[0]
        ZWJ ="\u200D"

        conjoining =[(0, 28), (2, 18), (9, 5), (10, 11), (15, 16), (15, 28), (17, 18), (17, 28), (19, 16), (19, 17), (19, 18), (19, 28) ]

        for x, y in conjoining:
            Strng = Strng.replace(ListC[x] + vir + ListC[y], ListC[x] + vir + ZWJ + ListC[y])

        for x in ListC:
            Strng = Strng.replace(ListC[26] + vir + x, ListC[26] + vir + ZWJ + x)

        for x in ListC:
            for y in ListC:
                Strng = Strng.replace(x + vir + y, x + ZWJ + vir + y)

        Strng = Strng.replace('ර‍්‍ය', 'ර්‍ය')

        return Strng

    def UrduAlternateUU(self, Strng):
        Strng = Strng.replace("\\u064F\\u0648","\u0648\u0657")

        return Strng

    def UrduRemoveShortVowels(self, Strng):
        ShortVowels = ['\u0652','\u064E','\u0650','\u064F', '\u0658']

        for vow in ShortVowels:
            Strng = Strng.replace(vow,"")

        return Strng

    def showstress(self, Strng):
        return Strng

