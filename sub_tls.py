#!/usr/bin/env python
import ssl
import time
import paho.mqtt.client as mqtt
from settings import HOSTNAME, USERNAME, PASSWORD, PORT

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("topic/test")


def on_message(client, userdata, msg):
    if msg.payload.decode() == "Hello world!":
        print("Yes! " + str(msg.payload.decode("utf-8")))
        #client.disconnect()


client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set("TSL/server.pem", "TSL/mqtt-client-cert.pem",
               "TSL/mqtt-client-key.pem", tls_version=ssl.PROTOCOL_TLSv1_2)
client.connect(HOSTNAME, int(PORT), 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()