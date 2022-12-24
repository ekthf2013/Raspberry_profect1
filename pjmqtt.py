# publisher

import time
import paho.mqtt.client as mqtt
import pj # 초음파 센서 입력 모듈 임포트

def on_connect(client, userdata, flag, rc):
        client.subscribe("led", qos = 0)

def on_message(client, userdata, msg) :
        msg = int(msg.payload);
        print(msg)
        pj.controlLED(msg) # msg는 0 또는 1의 정수

broker_ip = "localhost" # 현재 이 컴퓨터를 브로커로 설정

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_ip, 1883)
client.loop_start()

while(True):
    temperature_ = pj.getTemperature()
    client.publish("temperature", temperature_, qos=0)
    Humidity = pj.getHumidity()
    client.publish("humidity", Humidity, qos=0)
    time.sleep(2)

client.loop_stop()
client.disconnect()