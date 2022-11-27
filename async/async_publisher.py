
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


async def main():
    async with aiomqtt.Client("IP", 8883, username="usename", password="password",
                              tls_params=tls_params) as client:
        print("connect")
        await client.publish("None/Robot/RAYA_SIMULATION/RobotData", payload=0.38)
        i=0
        while i<9:
            await client.publish("None/Robot/RAYA_SIMULATION/RobotData", "Hello world!")
            i = i +1
        print("publish")

asyncio.run(main())

