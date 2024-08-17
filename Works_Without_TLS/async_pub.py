import asyncio
import aiomqtt
import ssl
from settings import HOSTNAME, PASSWORD, PORT, USERNAME

async def publish_message(topic: str, message: str):
    ssl_settings = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_settings.check_hostname = False
    ssl_settings.verify_mode = ssl.CERT_NONE  # Adjust for production use

    try:
        async with aiomqtt.Client(
            hostname=HOSTNAME,
            port=int(PORT),
            username=USERNAME,
            password=PASSWORD,
            tls_context=ssl_settings
        ) as client:
            await client.publish(topic, message)
            print(f"Message '{message}' published to topic '{topic}'")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
async def main():
    topic = "test/topic"
    message = "Hello, MQTT!"
    await publish_message(topic, message)

asyncio.run(main())