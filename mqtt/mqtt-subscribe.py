#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setenv import user, password
import paho.mqtt.client as mqtt
import datetime
import time

MQTTHOST = "hairdresser.cloudmqtt.com"
#USERNAME = "example@github"
#PASSWORD = "password"

# create client for 3.1.1
client = mqtt.Client(protocol=mqtt.MQTTv311)
# set user and password
client.username_pw_set(user, password)

# connect
client.connect(MQTTHOST, port=17817, keepalive=60)

Topic1 = "Out_Temp"
Topic2 = "Out_Humi"
Topic3 = "Out_Press"
Topic4 = "IN_Temp"
Topic5 = "IN_Humi"
Topic6 = "IN_Press"

# Subscribe
client.subscribe(Topic1)
def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))
	Out_Temp = msg.payload
time.sleep(4) # wait
client.discnnect()
client.subscribe(Topic2)
def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))
	Out_Humi = msg.payload
time.sleep(4) # wait
client.discnnect()
client.subscribe(Topic3)
def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))
	Out_Press = msg.payload
time.sleep(4) # wait
client.discnnect()
client.subscribe(Topic4)
def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))
	IN_Temp = msg.payload
time.sleep(4) # wait
client.discnnect()
client.subscribe(Topic5)
def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))
	IN_Humi = msg.payload
time.sleep(4) # wait
client.discnnect()
client.subscribe(Topic6)
def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))
	IN_Press = msg.payload
time.sleep(4) # wait
client.discnnect()
# roop in
#client.loop_forever()

# date
date1 = datetime.datetime.now()
date1 = str(date1)
# print(date1.replace('-', '/'))
date2 = date1.replace('-', '/')

# file write Out
with open('/home/ubuntu/denpa-gardening/sensor_data/sensor_date_Out.csv', 'a') as f:
    print(date2, file=f)
    print(',', file=f)
    print(Out_Temp, file=f)
    print(',', file=f)
    print(Out_Humi, file=f)
    print(',', file=f)
    print(Out_Press, file=f)
    print('\n', file=f)
f.closed

# file write IN
with open('/home/ubuntu/denpa-gardening/sensor_data/sensor_date_IN.csv', 'a') as f:
    print(date2, file=f)
    print(',', file=f)
    print(IN_Temp, file=f)
    print(',', file=f)
    print(IN_Humi, file=f)
    print(',', file=f)
    print(IN_Press, file=f)
    print('\n', file=f)
f.closed

