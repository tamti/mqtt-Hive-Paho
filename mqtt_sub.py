from mqtt_base import create_mqtt_client
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# def on_message(client, userdata, msg):
#     print(msg)
#     #parse_data_from_robot(msg.topic, msg.qos, msg.payload)

def on_message(client, userdata, msg):
    print("heyyyyyyyyyyyyyyy")
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
def parse_data_from_robot(topic : str, qos: int, payload: dict):
    try:
        robot_id = payload['content']['robot_id']
        battery_level = payload['content']['battery']
        position = payload['content']['position']
        status = payload['content']['status']

        print('Received information from topic ' + topic + '\n with qos is ' + str(qos) + '\n ' +
              'User will receive information from Robot with Id ' + str(robot_id) + '\n' + "battery percent is " +
              str(battery_level) + '\n position is ' + str(position) + '\n status  is ' + str(status))
    except Exception as e:
        print("during parsing throw exception with message  " + str(e))


client = create_mqtt_client()
# setting callbacks, use separate functions like above for better visibility
client.on_subscribe = on_subscribe
client.on_message = on_message

# subscribe to all topics of encyclopedia by using the wildcard "#"
client.subscribe("data/#", qos=1)

# loop_forever for simplicity, here you need to stop the loop manually
# you can also use loop_start and loop_stop
client.loop_forever()