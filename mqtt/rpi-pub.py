#!/usr/bin/env python3

import paho.mqtt.client as mqtt


###### Edit variables to your environment #######
broker_address = "test.mosquitto.org"     #MQTT broker_address
Topic1 = "Out_Temp"
Topic2 = "Out_Humi"
Topic3 = "Out_Press"
Msg1 = "Greetings from RPi !!!"
Msg2 = "Greetings from RPi !!!"
Msg3 = "Greetings from RPi !!!"

# publish MQTT
print("creating new instance")
client = mqtt.Client("pub2") #create new instance

print("connecting to broker: %s" % broker_address)
client.connect(broker_address) #connect to broker

print("Publishing message: %s to topic: %s" % (Msg, Topic))
client.publish(Topic1,Msg1)
client.publish(Topic2,Msg2)
client.publish(Topic3,Msg3)

#################
## Alternatively you can send a single message without creating an instance
##print "sending now"
##mqtt.single(Topic, Msg, hostname=broker_address)
