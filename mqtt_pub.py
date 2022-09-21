from mqtt_base import create_mqtt_client, on_message
# with this callback you can see if your publish was successful

def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

def on_message(client, userdata, msg):
    print("heyyyyyyyyyyyyyyyyyyyyyyyyy")
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

client = create_mqtt_client()
client.on_message = on_message
client.on_publish = on_publish

# a single publish, this can also be done in loops, etc.
client.publish("data/123456", payload='hot', qos=1)

# loop_forever for simplicity, here you need to stop the loop manually
# you can also use loop_start and loop_stop
client.loop_forever()