import ssl
from paho import mqtt
import paho.mqtt.client as paho
import paho.mqtt.publish as publish

from settings import HOSTNAME, USERNAME, PASSWORD, PORT

# create a set of 2 test messages that will be published at the same time
msgs = [{'topic': "RobotData/battery", 'payload': "87%"}, ("RobotData/position", "[1;1]", 0, False)]

# use TLS for secure connection with HiveMQ Cloud
sslSettings = ssl.SSLContext(mqtt.client.ssl.PROTOCOL_TLS)

# put in your cluster credentials and hostname
auth = {'username': USERNAME, 'password': PASSWORD}
publish.multiple(msgs, hostname=HOSTNAME, port=int(PORT), auth=auth,
                 tls=sslSettings, protocol=paho.MQTTv31)

