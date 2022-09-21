from paho import mqtt
from mqtt_base import create_mqtt_colient
# with this callback you can see if your publish was successful

def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


client = create_mqtt_colient()
client.on_message = on_message
client.on_publish = on_publish

# a single publish, this can also be done in loops, etc.
client.publish("data/123456", payload='{"origin": "Robot", "content": {"robot_id": 123456, '
                                      '"battery": 67,  "position": [1, 2], "status": "up"}}', qos=1)

# loop_forever for simplicity, here you need to stop the loop manually
# you can also use loop_start and loop_stop
client.loop_forever()