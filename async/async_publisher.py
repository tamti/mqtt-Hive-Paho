# #!/usr/bin/env python
import ssl
import time
import paho.mqtt.client as mqtt
# from ..settings import HOSTNAME, USERNAME, PASSWORD, PORT

client = mqtt.Client()
client.username_pw_set("Gary-N1", "Gary2022")
client.tls_set("TLS/server.pem", "TLS/mqtt-client-cert.pem", "TLS/mqtt-client-key.pem", tls_version=ssl.PROTOCOL_TLSv1_2)
client.connect_async("46.101.167.112", int("8883"), 60)
i=0
while (i<9):
    client.publish("None/Robot/RAYA_SIMULATION/RobotData", "Hello world!")
    i=i+1
client.disconnect()