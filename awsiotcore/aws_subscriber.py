# mqtt_subscriber.py
import asyncio
import ssl
import aiomqtt
class Sub_mqtt(object):

    def __init__(self, topic="sdk/test/python"):
        self.aws_tls_params = aiomqtt.TLSParameters(
            ca_certs="connect_device_package/root_CA.crt",
            certfile="connect_device_package/JETSON_ORING_BOGOTA-cert.pem",
            keyfile="connect_device_package/JETSON_ORING_BOGOTA-private.key",
            cert_reqs=ssl.CERT_REQUIRED,
            tls_version=ssl.PROTOCOL_TLSv1_2,
            ciphers=None
        )
        self.topic = topic
        self.tls_context = None  # Use if additional TLS configuration is needed

    async def on_message(self, client, userdata, message):
        print(f"Received message: {message.payload.decode()} on topic {message.topic}")

    async def subscribe(self):
        try:
            async with aiomqtt.Client('a2d1i5z2u9xn1w-ats.iot.eu-central-1.amazonaws.com', 8883,
                                      tls_params=self.aws_tls_params, tls_context=self.tls_context, client_id='PubSub') as aws_client:
                await aws_client.subscribe(self.topic, qos=1)
                aws_client.on_message = self.on_message
                print(f"Subscribed to {self.topic}")
                
                # Keep the subscriber running
                while True:
                    await asyncio.sleep(1)
        except Exception as e:
            print(f"Failed to subscribe: {e}")

if __name__ == "__main__":
    sub_mqtt = Sub_mqtt()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(sub_mqtt.subscribe())
