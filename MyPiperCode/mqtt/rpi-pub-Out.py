#coding: utf-8

import paho.mqtt.client as mqtt
import ssl

# file reade
with open('Pass.txt', 'r') as f:
	password = f.readline()
f.closed

with open('Temp.txt', 'r') as f:
	Out_Temp = f.readline()
f.closed

with open('Humi.txt', 'r') as f:
	Out_Humi = f.readline()
f.closed

with open('Press.txt', 'r') as f:
	Out_Press = f.readline()
f.closed

# mqtt setting
host = 'hairdresser.cloudmqtt.com'
port = 27817
Topic1 = "Out_Temp"
Topic2 = "Out_Humi"
Topic3 = "Out_Press"

### パスワード認証を使用する時に使用する
username = 'cyyminhw'
#password = 'mqtt'

#print Out_Temp
#print Out_Humi
#print Out_Press

def on_connect(client, userdata, flags, respons_code):
    """broker接続時のcallback関数
    """
    print('status {0}'.format(respons_code))
    #client.publish(topic, message)
	client.publish(Topic1, Out_Temp)
	client.publish(Topic2, Out_Humi)
	client.publish(Topic3, Out_Press)

def on_publish(client, userdata, mid):
    """メッセージをpublishした後のcallback関数
    """
    client.disconnect()

if __name__ == '__main__':
    ### インスタンス作成時にprotocol v3.1.1を指定
    client = mqtt.Client(protocol=mqtt.MQTTv311)
    ### パスワード認証を使用する時に使用する
    client.username_pw_set(username, password)
    ### SSL
    #client.tls_set(cacert,
    #    certfile = clientCert,
    #    keyfile = clientKey,
    #    tls_version = ssl.PROTOCOL_TLSv1_2)
    #client.tls_insecure_set(True)

    ### callback function
    client.on_connect = on_connect
    client.on_publish = on_publish

    client.connect(host, port=port, keepalive=60)
    client.loop_forever()