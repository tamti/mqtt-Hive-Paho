import asyncio
import asyncio_mqtt as aiomqtt
import ssl
from paho import mqtt
settings.py

async def publish_humidity(client):
    await client.publish("humidity/outside", payload=0.38)


async def publish_temperature(client):
    await client.publish("temperature/outside", payload=28.3)


async def main():
    sslSettings = ssl.SSLContext(mqtt.client.ssl.PROTOCOL_TLS)
    async with aiomqtt.Client(hostname=HOSTNAME, port=int(PORT), username=USERNAME,
                              password=PASSWORD, tls_context=sslSettings) as client:
        print("Hey I am here")
        await publish_humidity(client)
        await publish_temperature(client)


asyncio.run(main())
