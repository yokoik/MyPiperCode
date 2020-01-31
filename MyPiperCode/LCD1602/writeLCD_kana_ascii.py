#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('/home/pi/Adafruit-Raspberry-Pi-Python-Code-legacy/Adafruit_CharLCD') 
from Adafruit_CharLCD import Adafruit_CharLCD
 
text1 = u'ｺﾝﾆﾁﾜ!'
text2 = u'RasberryPi ﾃﾞｽ'
 
text1 = text1.encode('shift-jis')
text2 = text2.encode('shift-jis')
 
try:
  lcd = Adafruit_CharLCD()
  lcd.clear()
 
  lcd.message(text1)
  lcd.message('\n')
  lcd.message(text2)
finally:
  print 'cleanup'
  lcd.GPIO.cleanup()

