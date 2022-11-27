import asyncio
import asyncio_mqtt as aiomqtt
import ssl


tls_params = aiomqtt.TLSParameters(
    ca_certs="TLS/server.pem",
    certfile="TLS/mqtt-client-cert.pem",
    keyfile="TLS/yourkey-without-pass.pem",
    cert_reqs=ssl.CERT_REQUIRED,
    tls_version=ssl.PROTOCOL_TLSv1_2,
    ciphers=None,
)


import asyncio
import asyncio_mqtt as aiomqtt


async def listen():
    async with aiomqtt.Client("IP", 8883, username="username", password="password",
                              tls_params=tls_params) as client:
        async with client.unfiltered_messages() as messages:
            await client.subscribe("None/Robot/RAYA_SIMULATION/RobotData")
            async for message in messages:
                print(message.payload)


async def main():
    # Wait for messages in (unawaited) asyncio task
    loop = asyncio.get_event_loop()
    task = loop.create_task(listen())
    # This will still run!
    print("Magic!")
    # If you don't await the task here the program will simply finish.
    # However, if you're using an async web framework you usually don't have to await
    # the task, as the framework runs in an endless loop.
    await task


asyncio.run(main())




