import asyncio
import asyncio_mqtt as aiomqtt
import ssl
from paho import mqtt
from settings import HOSTNAME, PASSWORD, PORT, USERNAME
async def main():
    sslSettings = ssl.SSLContext(mqtt.client.ssl.PROTOCOL_TLS)
    async with aiomqtt.Client(hostname=HOSTNAME, port=int(PORT), username=USERNAME,
                              password=PASSWORD, tls_context = sslSettings) as client:
        #async with client.messages() as messages:
        async with client.unfiltered_messages() as messages:
            await client.subscribe("#")
            async for message in messages:
                print(message.payload)


asyncio.run(main())