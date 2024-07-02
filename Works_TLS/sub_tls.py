#!/usr/bin/env python
import ssl
import time
import paho.mqtt.client as mqtt
from settings import HOSTNAME, USERNAME, PASSWORD, PORT


def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected with result code " + str(reason_code))
    client.subscribe("#")


def on_message(client, userdata, msg):
    print("Yes! " + str(msg.payload.decode("utf-8")))
    #client.disconnect()


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.username_pw_set(USERNAME, PASSWORD)
client.tls_set("TLS/server.pem", "TLS/mqtt-client-cert.pem",
               "TLS/mqtt-client-key-pass.pem", tls_version=ssl.PROTOCOL_TLSv1_2)
client.connect(HOSTNAME, int(PORT), 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()

# def on_connect(client, userdata, flags, rc):
#     print("Connected with result code " + str(rc))
#     client.subscribe("sdk/test/python", qos=1)
#     print("after subscriber")


# def on_message(client, userdata, msg):
#     print("hey O a, here")
#     print("Yes! " + str(msg.payload.decode("utf-8")))
#     #client.disconnect()
#
#
# awshost = "a2d1i5z2u9xn1w-ats.iot.eu-central-1.amazonaws.com"
# awsport = 8883
#
# caPath =  "/home/tamta/Documents/mqtt-Hive-Paho/connect_device_package/root_CA.crt" # Root certificate authority, comes from AWS with a long, long name
# certPath = "/home/tamta/Documents/mqtt-Hive-Paho/connect_device_package/JETSON_ORING_BOGOTA-cert.pem"
# keyPath = "/home/tamta/Documents/mqtt-Hive-Paho/connect_device_package/JETSON_ORING_BOGOTA-private.key"
# print("certificatessss")
#
# client = mqtt.Client("basicPubSub")
# client.tls_set(caPath,
#                    certfile=certPath,
#                    keyfile=keyPath,
#                    cert_reqs=ssl.CERT_REQUIRED,
#                    tls_version=ssl.PROTOCOL_TLSv1_2,
#                    ciphers=None)
# client.connect(awshost, awsport, keepalive=120)
#
# client.on_connect = on_connect
# client.on_message = on_message
#
# client.loop_forever()

