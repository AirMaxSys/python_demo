#!/usr/bin/env python

from googletrans import Translator

# lang
def whatLang(str):
  la =  Translator().detect(str).lang
  if(la == 'en'):
    la = "zh-CN"
  elif(la == 'zh-CN'):
    la = "en"
  return la

def translateLang(str):
  l = ret = ''
  l = whatLang(str)
  ret = Translator().translate(str, dest=l).text
  return ret

