#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('/home/pi/Adafruit-Raspberry-Pi-Python-Code-legacy/Adafruit_CharLCD') 
from Adafruit_CharLCD import Adafruit_CharLCD

import requests
import json

url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
locale = {'city': '400010'}
data = requests.get(url, params = locale).json()

text1 = data['forecasts'][0]['date']
text2 = 'hello'
text3 = 'goodby'
 
try:
  lcd = Adafruit_CharLCD()
  lcd.clear()
 
  lcd.message(text1)
  lcd.message('\n')
  lcd.message(text2)
  #lcd.message('\n')
  #lcd.message(text3)

finally:
  print 'cleanup'
  lcd.GPIO.cleanup()

