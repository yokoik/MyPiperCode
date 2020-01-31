#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import datetime
Date_Time = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")

MQTTHOST = "3.14.70.236"
#USERNAME = "example@github"
#PASSWORD = "password"


# 3.1.1�p��Client���쐬���܂�
client = mqtt.Client(protocol=mqtt.MQTTv311)
# ���[�U�[���ƃp�X���[�h��ݒ肵�܂�
#client.username_pw_set(user, password)

# �ڑ����܂�
client.connect(MQTTHOST, port=1883, keepalive=60)

Topic0 = "Date_Time"

# Publish���܂�
client.publish(Topic0, Date_Time)


# ���̂܂܂��Ƃ����Ƀv���Z�X���I�����Ă��܂��܂��̂ŁAPublish���I���܂ő҂��܂�
import time
time.sleep(0.05)
