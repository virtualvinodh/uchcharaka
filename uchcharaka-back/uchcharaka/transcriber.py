import re
from . import helper
import espeak_py as espeak
from . import transliterator as tr

class Transcriber:
    def __init__(self, src, tgt, accuracy='medium', preoptions=[], postoptions=[]):
        self.src = src

        scriptList = helper.IndicScripts + helper.LatinScripts
        scriptListLower = list(map(lambda x: x.lower(), scriptList))

        # speical processing for Tamil
        if 'removeDifferentiation' in postoptions and 'Tamil' in tgt:
            accuracy = 'Low'

        #Tamil Medium --> TamilMedium
        if tgt not in helper.inaccurate_scripts:
            tgt = tgt + accuracy.title()

        if tgt.lower() in scriptListLower:
            self.tgt = [script_id for script_id in scriptList if tgt.lower() == script_id.lower()][0]
        else:
            raise Exception(f"Target script: {tgt} not supported")

        self.accuracy = accuracy.lower()

        #introduce postprocessing for non-accurate transcriptions
        if self.accuracy != 'high':
            postoptions = postoptions + [self.tgt]

        self.postoptions = postoptions

        # simplify Dipththongs in English for non-accurate transcriptions
        if (self.accuracy != 'high' or self.tgt in helper.inaccurate_scripts)\
            and 'en' in self.src and 'showDiphthongs' not in self.postoptions:
            preoptions = ['monophthongize'] + preoptions

        self.preoptions = preoptions

    def transcribe(self, Strng):
        # transcribe to IPA only if source is not IPA
        if self.src != 'IPA':
            try:
                ipa_transcription = espeak.text_to_phonemes(Strng, self.src)
            except Exception as e:
                ipa_transcription = ''
                print(e)
                print(espeak.list_languages())
        else:
            ipa_transcription = Strng

        ipa_transcription = self.IPAFixer(ipa_transcription)

        # introduce Aspiration if selected
        if 'AspirateStops' in self.preoptions:
            ipa_transcription = self.AspirateStops(ipa_transcription)
            self.preoptions.remove('AspirateStops')

        # use explicit dental t,d for romance languages
        if 'es' in self.src or 'fr' in self.src or 'pt' in self.src or 'it' in self.src:
            ipa_transcription = re.sub('t(?![ʃs])', 't̪', ipa_transcription)
            ipa_transcription = re.sub('d(?![ʒz])', 'd̪', ipa_transcription)

        # remove stress by default
        if 'showstress' not in self.postoptions:
            ipa_transcription = ipa_transcription.replace('ˈ', '').replace('ˌ', '')
            #self.preoptions.remove('showstress')

        if 'IPA' in self.tgt:
            return ipa_transcription
        else:
            transliterator = tr.Transliterator('IPA', self.tgt, \
                                            self.preoptions, self.postoptions)

            tgt_transcription = transliterator.convert(ipa_transcription)

        return tgt_transcription

    def AspirateStops(self, Strng):
        c = '|'.join(helper.CrunchSymbols(helper.Consonants,'IPA'))
        v = '|'.join(helper.CrunchSymbols(helper.Vowels,'IPA'))

        Strng = re.sub('(\s)([pkt])(?=ˈ('+v+'))', r'\1\2'+'ʰ', Strng)
        Strng = re.sub('^([pkt])(?=ˈ('+v+'))', r'\1'+'ʰ', Strng)
        Strng = re.sub('('+v+')([pkt])(?=ˈ('+v+'))', r'\1\2'+'ʰ', Strng)

        return Strng

    def IPAFixer(self, Strng):
        Strng = Strng.replace('ᵻ', 'ɨ')
        c = '|'.join(helper.CrunchSymbols(helper.Consonants,'IPA'))

        #duplicate consonants p: => pp
        Strng = re.sub('(' + c + ')' +'(ː)', r'\1\1', Strng)


        return Strng