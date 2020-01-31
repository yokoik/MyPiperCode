#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import datetime
Date_Time = datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")

MQTTHOST = "3.14.70.236"
#USERNAME = "example@github"
#PASSWORD = "password"


# 3.1.1用のClientを作成します
client = mqtt.Client(protocol=mqtt.MQTTv311)
# ユーザー名とパスワードを設定します
#client.username_pw_set(user, password)

# 接続します
client.connect(MQTTHOST, port=1883, keepalive=60)

Topic0 = "Date_Time"

# Publishします
client.publish(Topic0, Date_Time)


# そのままだとすぐにプロセスが終了してしまいますので、Publishし終わるまで待ちます
import time
time.sleep(0.05)
