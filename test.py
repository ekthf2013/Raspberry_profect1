import time
import RPi.GPIO as GPIO
from adafruit_htu21d import HTU21D
import busio

sda = 2 # GPIO 핀 번호, sda라고 이름이 보이는 핀
scl = 3 # GPIO 핀 번호, scl이라고 이름이 보이는 핀
i2c = busio.I2C(scl, sda)
sensor = HTU21D(i2c) # HTU21D 장치를 제어하는 객체 리턴
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def getTemperature() :
        return float(sensor.temperature) # HTU21D 장치로부터 온도 값 읽기

def getHumidity() :    
        return float(sensor.relative_humidity) # HTU21D 장치로부터 습도 값 읽기

# LED 점등을 위한 전역 변수 선언 및 초기화
led = 5 # 핀 번호 GPIO6 의미
GPIO.setup(led, GPIO.OUT) # GPIO 6번 핀을 출력 선으로 지정.

def controlLED(onOff): # led 번호의 핀에 onOff(0/1) 값 출력하는 함수
    GPIO.output(led, onOff)

#def controlSOUND(Onoff):
    #GPIO.output(buzzer, True)
    #time.sleep(1)