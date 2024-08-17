import asyncio
import aiomqtt
from paho import mqtt
import ssl
from settings import HOSTNAME, PASSWORD, PORT, USERNAME

async def main():
    ssl_settings = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_settings.check_hostname = False
    ssl_settings.verify_mode = ssl.CERT_NONE  # This should be adjusted for production use

    try:
        async with aiomqtt.Client(
            hostname=HOSTNAME,
            port=int(PORT),
            username=USERNAME,
            password=PASSWORD,
            tls_context=ssl_settings
        ) as client:
            await client.subscribe('#')
            async for message in client.messages:
                    print(f"Received message: {message.payload.decode()} on topic {message.topic}")
    except Exception as e:
        print("An error occurred: " + str(e))

asyncio.run(main())
