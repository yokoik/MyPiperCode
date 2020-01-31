#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt

# file reade
with open('Temp.txt', 'r') as f:
	IN_Temp = f.readline()
f.closed

with open('Humi.txt', 'r') as f:
	IN_Humi = f.readline()
f.closed

with open('Press.txt', 'r') as f:
	IN_Press = f.readline()
f.closed

MQTTHOST = "3.14.70.236"
#USERNAME = "example@github"
#PASSWORD = "password"


# 3.1.1�p��Client���쐬���܂�
client = mqtt.Client(protocol=mqtt.MQTTv311)
# ���[�U�[���ƃp�X���[�h��ݒ肵�܂�
#client.username_pw_set(user, password)

# �ڑ����܂�
client.connect(MQTTHOST, port=1883, keepalive=60)

Topic1 = "IN_Temp"
Topic2 = "IN_Humi"
Topic3 = "IN_Press"

# Publish���܂�
client.publish(Topic1, IN_Temp)
client.publish(Topic2, IN_Humi)
client.publish(Topic3, IN_Press)

# ���̂܂܂��Ƃ����Ƀv���Z�X���I�����Ă��܂��܂��̂ŁAPublish���I���܂ő҂��܂�
import time
time.sleep(0.05)
