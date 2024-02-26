import datetime
import sys
from Adafruit_IO import MQTTClient
import time, random
from simple_ai import *
from uart import *

AIO_FEED_ID = ["nutnhan1", "nutnhan2"]
AIO_USERNAME = ""
AIO_KEY = ""

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_ID:
        client.subscribe(AIO_FEED_ID)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " ,feed id: " + feed_id)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()


counter = 5
sensor_type = 1
counter_ai = 5
ai_result = ""
previous_result = ""
while True:
    # counter = counter - 1
    # if counter <= 0 :
    #     counter = 5
    #     print("Random data is publising...")
    #     print(datetime.datetime.now())
    #     print("Sensor",sensor_type)
    #     if sensor_type == 1:
    #         print("Temperture...")
    #         temp = random.randint(10,20)
    #         client.publish("cambien2", temp)
    #         sensor_type = 2
    #     elif sensor_type == 2:
    #         print("Humidity...")
    #         humi = random.randint(50,70)
    #         client.publish("cambien3",humi)
    #         sensor_type = 3
    #     elif sensor_type == 3:
    #         print("Light...")
    #         light = random.randint(100, 500)
    #         client.publish("cambien1", light)
    #         sensor_type = 1

    counter_ai -= 1
    if counter_ai <= 0:
        counter_ai = 5
        previous_result = ai_result
        ai_result = image_detector()
        if previous_result != ai_result:
            client.publish("ai",ai_result)

    readSerial(client)
    time.sleep(1)
    pass