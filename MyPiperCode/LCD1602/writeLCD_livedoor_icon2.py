#!/usr/local/bin/python
# -*- coding: utf-8 -*-

#import sys
#sys.path.append('/home/pi/Adafruit-Raspberry-Pi-Python-Code-legacy/Adafruit_CharLCD') 
#from Adafruit_CharLCD import Adafruit_CharLCD

import requests
import json

url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
locale = {'city': '110010'}
data = requests.get(url, params = locale).json()

print(data)
tenkiNo = [u'ハレ',u'ハレトキドキクモリ',u'ハレトキドキアメ',u'ハレトキドキユキ',u'ハレノチクモリ',u'ハレノチアメ',u'ハレノチユキ',u'クモリ',u'クモリトキドキハレ',u'クモリトキドキアメ',u'クモリトキドキユキ',u'クモリノチハレ',u'クモリノチアメ',u'クモリノチユキ',u'アメ',u'アメトキドキハレ',u'アメトキドキクモリ',u'アメトキドキユキ',u'アメノチハレ',u'アメノチクモリ',u'アメノチユキ',u'ツヨイアメ',u'ユキ',u'ユキトキドキクハレ',u'ユキトキドキクモリ',u'ユキトキドキアメ',u'ユキノチハレ',u'ユキノチクモリ',u'ユキノチアメ',u'ツヨイユキ']
try:
  lcd = Adafruit_CharLCD()
  lcd.clear()

#for weather in data['forecasts'][0:2]:
#	tenki = int(weather['image']['url'][37:-4])-1
#	text = tenkiNo[tenki]
#	lcd.message(text)
#	lcd.message('\n')
 
#try:
#  lcd = Adafruit_CharLCD()
#  lcd.clear()
 
#  lcd.message(text1)
#  lcd.message('\n')
#  lcd.message(text2)
  #lcd.message('\n')
  #lcd.message(text3)

#finally:
#  print 'cleanup'
#  lcd.GPIO.cleanup()