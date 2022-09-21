import time
import paho.mqtt.client as paho
from paho import mqtt

# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNECT received with code %s." % rc)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))


# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set("Gary-N1", "Gary2022")
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect("ac4df6d047ab4c6597964247a94d87ea.s1.eu.hivemq.cloud", 8883)

client.on_message = on_message
client.on_publish = on_publish

# a single publish, this can also be done in loops, etc.
client.publish("data/123456", payload={"origin": "Robot", "content": {"robot_id": 123456, "battery": 67,  "position": [1, 2], "status": 'up'}}, qos=1)

# loop_forever for simplicity, here you need to stop the loop manually
# you can also use loop_start and loop_stop
client.loop_forever()