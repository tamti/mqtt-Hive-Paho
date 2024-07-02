# from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
# import asyncio
# import time
#
# def on_message_received(topic, payload, **kwargs):
#     print("Received message from topic '{}': ")
#     global received_count
#     received_count += 1
#     # if received_count == args.count:
#     #     received_all_event.set()
#
# def customcall(topic):
#     print("Received message from topic '{}'".format(topic))
#
# myMQTTClient = AWSIoTMQTTClient("basicPubSub")
# myMQTTClient.configureEndpoint("a2d1i5z2u9xn1w-ats.iot.eu-central-1.amazonaws.com", 8883)
# myMQTTClient.configureCredentials("/home/tamta/Documents/mqtt-Hive-Paho/connect_device_package/root_CA.crt",
#                                   "/home/tamta/Documents/mqtt-Hive-Paho/connect_device_package/JETSON_ORING_BOGOTA-private.key",
#                                   "/home/tamta/Documents/mqtt-Hive-Paho/connect_device_package/JETSON_ORING_BOGOTA-cert.pem"
#                                   )
# # myMQTTClient.connectAsync()
# # print("connect")
# # print("sybscribing start.....\n\n\n")
# # myMQTTClient.subscribe("myTopic", 0, on_message_received)
# # print("finishh itt ....   \n\n\n")
# # #time.sleep(2)
#
# # Connect and subscribe to AWS IoT
# myMQTTClient.connect()
# print("after connect")
# myMQTTClient.subscribe("/asd", 1, on_message_received)
# time.sleep(1)
# print("after sleeep")
# # Publish to the same topic in a loop forever
# while True:
#     myMQTTClient.publish("/asd", "Hola AWS!!!", 0)
#     time.sleep(1)

#myMQTTClient.unsubscribe("myTopic")
#myMQTTClient.disconnect()

import paho.mqtt.client as paho
import os
import socket
import ssl
from time import sleep
from random import uniform
import json

import logging
# from settings import HOSTNAME, USERNAME, PASSWORD, PORT

logging.basicConfig(level=logging.INFO)


# Refactored original source - https://github.com/mariocannistra/python-paho-mqtt-for-aws-iot

class PubSub(object):

    def __init__(self, listener=False, topic="sdk/test/python"):
        self.connect = False
        self.listener = listener
        self.topic = topic
        self.logger = logging.getLogger(repr(self))

    def __on_connect(self, client, userdata, flags, rc):
        self.connect = True
        if self.listener:
            self.mqttc.subscribe(self.topic, qos=1)
        self.logger.debug("{0}".format(rc))

    def __on_message(self, client, userdata, msg):
        self.logger.info("{0}, {1} - {2}".format(userdata, msg.topic, msg.payload))

    def __on_log(self, client, userdata, level, buf):
        self.logger.debug("{0}, {1}, {2}, {3}".format(client, userdata, level, buf))

    def bootstrap_mqtt(self):
        self.mqttc = paho.Client("basicPubSub")
        self.mqttc.on_connect = self.__on_connect
        self.mqttc.on_message = self.__on_message
        self.mqttc.on_log = self.__on_log
        awshost = "a2d1i5z2u9xn1w-ats.iot.eu-central-1.amazonaws.com"
        awsport = 8883

        caPath =  "/home/tamta/Documents/mqtt-Hive-Paho/connect_device_package/root_CA.crt" # Root certificate authority, comes from AWS with a long, long name
        certPath = "/home/tamta/Documents/mqtt-Hive-Paho/connect_device_package/JETSON_ORING_BOGOTA-cert.pem"
        keyPath = "/home/tamta/Documents/mqtt-Hive-Paho/connect_device_package/JETSON_ORING_BOGOTA-private.key"
        # print("certificatessss")
        self.mqttc.tls_set(caPath,
                           certfile=certPath,
                           keyfile=keyPath,
                           cert_reqs=ssl.CERT_REQUIRED,
                           tls_version=ssl.PROTOCOL_TLSv1_2,
                           ciphers=None)
        result_of_connection = self.mqttc.connect(awshost, awsport, keepalive=120)

        # self.mqttc.username_pw_set(USERNAME, PASSWORD)
        # self.mqttc.tls_set("TLS/server.pem", "TLS/mqtt-client-cert.pem",
        #                "TLS/yourkey-without-pass.pem", tls_version=ssl.PROTOCOL_TLSv1_2)
        # print(HOSTNAME)
        # result_of_connection = self.mqttc.connect(HOSTNAME, int(PORT), 60)
        print("SEEEMS it connect  " + str(result_of_connection))
        if result_of_connection == 0:
            self.connect = True
        return self

    def start(self):
        self.mqttc.loop_start()

        while True:
            sleep(2)
            if self.connect == True:
                self.mqttc.publish(self.topic, json.dumps({"message": "Hello first one"}), qos=1)
            else:
                self.logger.debug("Attempting to connect.")


if __name__ == '__main__':
    PubSub(listener=True, topic="sdk/test/python").bootstrap_mqtt().start()