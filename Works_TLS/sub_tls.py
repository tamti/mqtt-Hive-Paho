#!/usr/bin/env python
import ssl
import time
import paho.mqtt.client as mqtt
from settings import HOSTNAME, USERNAME, PASSWORD, PORT
# !/usr/bin/env python3
# This is the Subscriber

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("#")


def on_message(client, userdata, msg):
    print("Yes! " + str(msg.payload.decode("utf-8")))
    #client.disconnect()


client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set("TLS/server.pem", "TLS/mqtt-client-cert.pem",
               "TLS/yourkey-without-pass.pem", tls_version=ssl.PROTOCOL_TLSv1_2)
client.connect(HOSTNAME, int(PORT), 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
