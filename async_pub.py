import asyncio
import asyncio_mqtt as aiomqtt
import ssl
from paho import mqtt
from settings import HOSTNAME, PORT, USERNAME, PASSWORD

async def publish_humidity(client):
    await client.publish("humidity/outside", payload=0.38)


async def publish_temperature(client):
    await client.publish("temperature/outside", payload=28.3)

awshost = "a2d1i5z2u9xn1w-ats.iot.eu-central-1.amazonaws.com"
awsport = 8883

caPath =  "/home/tamta/Documents/mqtt-Hive-Paho/connect_device_package/root_CA.crt" # Root certificate authority, comes from AWS with a long, long name
certPath = "/home/tamta/Documents/mqtt-Hive-Paho/connect_device_package/JETSON_ORING_BOGOTA-cert.pem"
keyPath = "/home/tamta/Documents/mqtt-Hive-Paho/connect_device_package/JETSON_ORING_BOGOTA-private.key"
print("certificatessss")
self.mqttc.tls_set(caPath,
                   certfile=certPath,
                   keyfile=keyPath,
                   cert_reqs=ssl.CERT_REQUIRED,
                   tls_version=ssl.PROTOCOL_TLSv1_2,
                   ciphers=None)

async def main():
    sslSettings = ssl.SSLContext(mqtt.client.ssl.PROTOCOL_TLS)
    async with aiomqtt.Client(hostname=HOSTNAME, port=int(PORT), username=USERNAME,
                              password=PASSWORD, tls_context=sslSettings) as client:
        print("Hey I am here")
        await publish_humidity(client)
        await publish_temperature(client)


asyncio.run(main())
