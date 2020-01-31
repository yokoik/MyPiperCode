#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setenv import user, password
import paho.mqtt.client as mqtt

# file reade
with open('Temp.txt', 'r') as f:
	Out_Temp = f.readline()
f.closed

with open('Humi.txt', 'r') as f:
	Out_Humi = f.readline()
f.closed

with open('Press.txt', 'r') as f:
	Out_Press = f.readline()
f.closed

MQTTHOST = "hairdresser.cloudmqtt.com"
#USERNAME = "example@github"
#PASSWORD = "password"


# 3.1.1�p��Client���쐬���܂�
client = mqtt.Client(protocol=mqtt.MQTTv311)
# ���[�U�[���ƃp�X���[�h��ݒ肵�܂�
client.username_pw_set(user, password)

# �ڑ����܂�
client.connect(MQTTHOST, port=17817, keepalive=60)

Topic1 = "Out_Temp"
Topic2 = "Out_Humi"
Topic3 = "Out_Press"

# Publish���܂�
client.publish(Topic1, Out_Temp)
client.publish(Topic2, Out_Humi)
client.publish(Topic3, Out_Press)

# ���̂܂܂��Ƃ����Ƀv���Z�X���I�����Ă��܂��܂��̂ŁAPublish���I���܂ő҂��܂�
import time
time.sleep(0.05)
