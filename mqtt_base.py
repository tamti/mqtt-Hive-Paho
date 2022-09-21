
import paho.mqtt.client as paho
from paho import mqtt

# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNECT received with code %s." % rc)

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# print which topic was subscribed to
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def create_mqtt_colient():
    client = paho.Client(client_id="clientId-njsdrUzSHj", userdata=None, protocol=paho.MQTTv5)
    client.on_connect = on_connect
    # enable TLS for secure connection
    client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
    # set username and password
    client.username_pw_set("Gary-N1", "Gary2022")
    # connect to HiveMQ Cloud on port 8883 (default for MQTT)
    client.connect("ac4df6d047ab4c6597964247a94d87ea.s1.eu.hivemq.cloud", 8883)
    return client
