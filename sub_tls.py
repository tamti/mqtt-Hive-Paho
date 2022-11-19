#!/usr/bin/env python
import ssl
import time
import paho.mqtt.client as mqtt
from settings import HOSTNAME, USERNAME, PASSWORD, PORT

topic = "T/GettingStarted/pubsub"


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)


client = mqtt.Client("mqttclient" )
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set("server.pem", "mqtt-client-cert.pem", "mqtt-client-key.pem", tls_version=ssl.PROTOCOL_TLSv1_2)
client.tls_insecure_set(False)
client.connect(HOSTNAME, int(PORT), 60)


print("Subscribing to topic", topic)
client.on_message = on_message
client.subscribe(topic, qos=1)

client.loop_forever()

# client.loop_stop()
#
# print("Goodbye!")
