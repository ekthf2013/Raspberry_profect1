import time
import RPi.GPIO as GPIO
import Adafruit_MCP3008
import pj

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led2 = 6 # 핀 번호 GPIO6 의미 (흰색)
GPIO.setup(led2, GPIO.OUT) # GPIO 6번 핀을 출력 선으로 지정.
led = 5 # 핀 번호 GPIO6 의미 (노란색)
GPIO.setup(led, GPIO.OUT) # GPIO 6번 핀을 출력 선으로 지정

mcp = Adafruit_MCP3008.MCP3008(clk=11, cs=8, miso=9, mosi=10)

trig=20
echo=16
buzzer=12 #부저
GPIO.setup(buzzer, GPIO.OUT) # 출력 설정
p = GPIO.PWM(buzzer, 100)
scale = [ 261, 294, 329, 349, 392, 440, 493, 523 ]
list = [0,0,4,4,5,5,4,3,3,2,2,1,1,0] #작은별 노래

#sda=2 #온습도 센서
#scl=3 #온습도 센서
#i2c=busio.I2C(scl,sda) #온습도 센서
#sensor=HTU21D(i2c) #온습도 센서
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
GPIO.output(trig,False)

def ledOnOff(led,onOff): #LED를 키고 끄는 것을 위한 함수
    GPIO.output(led,onOff)

def measureDistance(trig, echo): #거리 측정을 위한 함수
    time.sleep(0.5)
    GPIO.output(trig,True)
    GPIO.output(trig,False)
    while(GPIO.input(echo)==0):
        pass
    pulse_start=time.time()
    while(GPIO.input(echo)==1):
        pass
    pulse_end=time.time()
    pulse_duration=pulse_end-pulse_start #거리계산을 위한 찍고 돌아오는데 걸리는 시간계산
    return 340*100/2*pulse_duration #거리 계산

#def getTemperature(): #온도측정을 위한 함수
    #return float(sensor.temperature)

onOff = 1 # 1은 디지털 출력 값. 1 = 5V
Onoff = 0 # 0은 디지털 출력을 멈추게 함

try:
    while True:
        distance = measureDistance(trig, echo)
        print("온도는 %4.1d" %pj.sensor.temperature)
        if(distance < 15.0 and mcp.read_adc(0) < 100): #거리가 10보다 작을 때
            ledOnOff(led2, onOff) # led가 연결된 핀에 1의 디지털 값 출력
            ledOnOff(led, onOff)
            if (pj.sensor.temperature>=47):
                p.start(100) # pwm 시작
                p.ChangeDutyCycle(90) # dutycycle 변경
                for i in range(len(list)): #len() => 길이 추출
                    p.ChangeFrequency(scale[list[i]]) #주파수 변경
                    if (i+1)%7 == 0: # 7번째 음 박자 변경
                        time.sleep(1)
                    else :
                        time.sleep(0.5)
                p.stop()
        elif(distance < 15.0 and mcp.read_adc(0) >= 100):
            ledOnOff(led2, onOff) # led가 연결된 핀에 1의 디지털 값 출력
            ledOnOff(led, Onoff)
            if (pj.sensor.temperature>=47):
                p.start(100) # pwm 시작
                p.ChangeDutyCycle(90) # dutycycle 변경
                for i in range(len(list)): #len() => 길이 추출
                    p.ChangeFrequency(scale[list[i]]) #주파수 변경
                    if (i+1)%7 == 0: # 7번째 음 박자 변경
                        time.sleep(1)
                    else :
                        time.sleep(0.5)            
                p.stop()   
        elif(distance >= 15.0 and mcp.read_adc(0) < 100):
            ledOnOff(led2, Onoff) # led가 연결된 핀에 1의 디지털 값 출력
            ledOnOff(led, onOff)
            if (pj.sensor.temperature>=47):
                p.start(100) # pwm 시작
                p.ChangeDutyCycle(90) # dutycycle 변경
                for i in range(len(list)): #len() => 길이 추출
                    p.ChangeFrequency(scale[list[i]]) #주파수 변경
                    if (i+1)%7 == 0: # 7번째 음 박자 변경
                        time.sleep(1)
                    else :
                        time.sleep(0.5)
                p.stop()                           
        elif(distance >= 15.0 and mcp.read_adc(0) >= 100): #거리가 20보다 클 때
            ledOnOff(led2,Onoff) # led가 연결된 핀에 0의 디지털 값 출력
            ledOnOff(led, Onoff)
            if (pj.sensor.temperature>=47):
                p.start(100) # pwm 시작
                p.ChangeDutyCycle(90) # dutycycle 변경
                for i in range(len(list)): #len() => 길이 추출
                    p.ChangeFrequency(scale[list[i]]) #주파수 변경
                    if (i+1)%7 == 0: # 7번째 음 박자 변경
                        time.sleep(1)
                    else :
                        time.sleep(0.5)   
                p.stop()       
finally:
    GPIO.cleanup()