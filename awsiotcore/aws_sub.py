#!/usr/bin/python

# this source is part of my Hackster.io project:  https://www.hackster.io/mariocannistra/radio-astronomy-with-rtl-sdr-raspberrypi-and-amazon-aws-iot-45b617

# use this program to test the AWS IoT certificates received by the author
# to participate to the spectrogram sharing initiative on AWS cloud

# this program will subscribe and show all the messages sent by its companion
# awsiotpub.py using the AWS IoT hub

import paho.mqtt.client as paho
import os
import socket
import ssl

def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc) )
    client.subscribe("sdk/test/python" , qos=1)
    print("after subscriber")

def on_message(client, userdata, msg):
    print("topic: "+msg.topic)
    print("payload: "+str(msg.payload))


mqttc = paho.Client("tamta")
mqttc.on_connect = on_connect
mqttc.on_message = on_message
#mqttc.on_log = on_log

awshost = "a2d1i5z2u9xn1w-ats.iot.eu-central-1.amazonaws.com"
awsport = 8883

caPath =  "/home/tamta/Documents/mqtt-Hive-Paho/connect_device_package/root_CA.crt" # Root certificate authority, comes from AWS with a long, long name
certPath = "/home/tamta/Documents/mqtt-Hive-Paho/connect_device_package/JETSON_ORING_BOGOTA-cert.pem"
keyPath = "/home/tamta/Documents/mqtt-Hive-Paho/connect_device_package/JETSON_ORING_BOGOTA-private.key"

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

mqttc.connect(awshost, awsport, keepalive=60)

mqttc.loop_forever()