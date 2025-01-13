import re
from . import helper, preprocessor, postprocessor, fixer
from functools import cmp_to_key

class Transliterator:
    def __init__(self, src, tgt, preoptions=[], postoptions=[]):

        self.src = src
        self.tgt = tgt
        self.postoptions = postoptions
        self.preoptions = preoptions

        self.preprocessor = preprocessor.Preprocessor(self.src, self.tgt, self.preoptions, self.postoptions)
        self.postprocessor = postprocessor.PostProcessor(self.src, self.tgt, self.preoptions, self.postoptions)
        self.fixer = fixer.Fixer(self.src, self.tgt, self.preoptions, self.postoptions)

    def convert(self, txt):
        txt = self.preprocessor.preprocess(txt)
        transliteration = self.convertScript(txt)
        transliteration = self.postprocessor.postprocess(transliteration)

        return transliteration

    def convertInter(self, Strng):
        ScriptAll = helper.Vowels+helper.Consonants+helper.CombiningSigns+helper.Numerals+helper.Signs+helper.Aytham
        SourceScript = helper.CrunchSymbols(ScriptAll,self.src)
        TargetScript = helper.CrunchSymbols(ScriptAll,helper.Inter)
        ScriptMapAll = sorted(zip(SourceScript,TargetScript),key=cmp_to_key(helper.lenSort))

        for x,y in ScriptMapAll:
            Strng = Strng.replace(x,y)

        return Strng

    # Conversion Module
    def convertScript(self, Strng):
        charPairs=[];
        Schwa = '\uF000'
        DepV = '\u1E7F'

        Strng = self.convertInter(Strng)
        Source = helper.Inter
        Strng = self.indianize_inter(Strng)

        Strng = Strng.replace("ṿ×_","ṿ")
        Strng = Strng.replace("ṿ×_","ṿ")

        ha = helper.CrunchSymbols(helper.Consonants,Source)[32]
        charPairs=[]

        for charList in helper.ScriptAll:
            # Crunch all related characters into a list
            TargetScript = helper.CrunchSymbols(helper.retCharList(charList),self.tgt)
            if charList == 'VowelSigns':
                # Add DepVSign to all VowelSigns to differentiate from Independent Vowels
                SourceScript = [DepV+x for x in helper.CrunchSymbols(helper.VowelSigns,Source)]
            else:
                SourceScript = helper.CrunchSymbols(helper.retCharList(charList),Source)
            # Create a Tuple for the conversion pair
            ScriptMap = list(zip(SourceScript,TargetScript))
            # Sort the mapping in descending order. Longer Characters are to be replaced first. ऍˇ > ऍ
            ScriptMap.sort(reverse=True);
            charPairs= charPairs + ScriptMap

        charPairs = sorted(charPairs,key=cmp_to_key(helper.lenSort))

        # Perform replacement sequentially for each character group
        for x,y in charPairs:
            #print(x, '-->', y)
            Strng = Strng.replace(x,y)
            #print(Strng)

        ## a_i => a<dev>i<dev> ; a_u = a<dev>u<dev>
        Strng=Strng.replace('_' + helper.CrunchSymbols(helper.Vowels,self.tgt)[2],  helper.CrunchSymbols(helper.Vowels,self.tgt)[2])
        Strng=Strng.replace('_' + helper.CrunchSymbols(helper.Vowels,self.tgt)[4],  helper.CrunchSymbols(helper.Vowels,self.tgt)[4])

        ## Joiners Vir + ZWJ
        vir = helper.CrunchList('ViramaMap', self.tgt)[0]
        Strng = Strng.replace(vir + "[]", "\u200D" + vir)

        if Source in ['Inter']:
            Strng = Strng.replace('\u00D7', vir) # special explicit Virama

        # Apply Fixes on the Output based on the Script
        Strng = self.fixer.fix(Strng)

        Strng = self.remove_temp_markers(Strng)

        return Strng

    ## This is the processing that's done immediately after calling the convert() function
    ## But before the post-processing steps
    ## removes extranous/artificial diacritics introduced
    def remove_temp_markers(self, Strng):
        Strng = Strng.replace("\uF001", "").replace("\u05CC", "").\
            replace("ʻʻ", "").replace('\u05CD', '').replace('\u02C2', '') ## remove token characters for specialized processing

        return Strng

    def indianize_inter(self, Strng):
        DepV = '\u1E7F'
        Asp = '\u02B0'

        Vir = helper.CrunchList("ViramaMap", 'Inter')[0]
        Nuk = helper.CrunchList("NuktaMap", 'Inter')[0]
        VowelA = helper.CrunchSymbols(['VowelMap'], 'Inter')[0]

        ListV = '|'.join(helper.CrunchSymbols(helper.VowelSigns, 'Inter'))
        ListC = '|'.join(helper.CrunchSymbols(helper.Consonants, 'Inter'))

        Strng = re.sub('('+ListC+')'+'(?!'+ListV+'|'+VowelA+')',r'\1'+DepV+Vir,Strng)

        Strng = re.sub('('+ListC+'|'+Nuk+')'+'('+ListV+')',r'\1'+DepV+r'\2',Strng)

        Strng = re.sub('(?<='+ListC+')'+'('+VowelA+')',r'',Strng)

        return Strng

