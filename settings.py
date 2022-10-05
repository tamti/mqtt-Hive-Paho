import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv('MQTT_USERNAME')
PASSWORD = os.getenv('PASSWORD')
HOSTNAME = os.getenv('HOSTNAME')
PORT = os.getenv('PORT')
