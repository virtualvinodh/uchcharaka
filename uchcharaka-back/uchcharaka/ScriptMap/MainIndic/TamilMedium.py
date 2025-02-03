from .Tamil import *

ConsonantMap = ConsonantMap[:]
ConsonantMap[29] = ConsonantMap[30]

SouthConsonantMap = SouthConsonantMap[:]
SouthConsonantMap[2] = ConsonantMap[26]

ModernVowelMap = [
                 'ஏ॑',
                 'ஆ॒॑',
                 ]

ModernVowelSignMap =[
                    'ே॑',
                    'ா॒॑',
                    ]

IPAVowelMap = [
                  'அ',
                  'அ',

                  'அ',
                  'ஆ',
                  'ஆ',
                  'ஆ',

                  'இ',
                  'இ',

                  'உ',
                  'உ',
                  'ஊ',

                  'எ',
                  'எ',
                  'எர்॒',
                  'ஏர்॒',

                  'ஆ॒᳚',
                  'ஆ॒॑',

                  'ஒ',
                  'ஓ',
                  'ஒ',
                  'ஓ'
                  ]

NuktaConsonantMap =  [
                     'க',
                     'ஃக²',
                     'க³',
                     'ஃஜ',
                     'ட⁴',
                     'ட⁴',
                     'ஃப',
                     'ய'
                     ]

IPAVowelSignMap = [
                  '\u02BD',
                  '\u02BD',

                  '\u02BD',
                  'ா',
                  'ா',
                  'ா',

                  'ி',
                  'ி',

                  'ு',
                  'ு',
                  'ூ',

                  'ெ',
                  'ெ',
                  'ெர்॒',
                  'ேர்॒',

                  'ா॒᳚',
                  'ா॒॑',

                  'ொ',
                  'ோ',
                  'ொ',
                  'ோ'
                ]

IPAConsonantMap =[
                     'ட',
                     'ட²',
                     'ட³',
                     'வ·',
                     'வ',
                     'த·',
                     'த³·',
                     'ர',
                     'ஷ·',
                     'வ',
                     'ய்ஜ',
                     'ய',
                     'ஹ்ர',
                     'ஹ',
                     'ஶ·'
                      ]