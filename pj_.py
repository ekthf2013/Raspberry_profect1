import time
import RPi.GPIO as GPIO
import Adafruit_MCP3008

GPIO.setmode(GPIO.BCM) # BCM 모드로 작동
GPIO.setwarnings(False) # 경고글이 출력되지 않게 설정

mcp = Adafruit_MCP3008.MCP3008(clk=11, cs=8, miso=9, mosi=10)

trig = 20
echo = 16
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.output(trig, False)
def ledOnOff(led, onOff_): # led 번호의 핀에 onOff(1) 값 출력하는 함수
	GPIO.output(led, onOff_)
def ledOnOff(led, Onoff_): # led 번호의 핀에 onOff(0) 값 출력하는 함수
	GPIO.output(led, Onoff_)

def measure_Distance(trig, echo):
	time.sleep(0.5)
	GPIO.output(trig, True) # 신호 1
	#time.sleep(0.00001) # 짧은 시간을 나타내기 위함
	GPIO.output(trig, False) # 신호가 1-> 0으로 떨어질 때 초음파발생
	while(GPIO.input(echo) == 0):
		pass
	pulse_start = time.time() # echo 신호가 1인 경우, 초음파 발사된 순간
	while(GPIO.input(echo) == 1):
		pass
	pulse_end = time.time() # 초음파 신호가 도착한 순간
	# echo 신호가 1->0으로 되면 보낸 초음파 수신 완료
	pulse_duration = pulse_end - pulse_start
	return 340*100/2*pulse_duration
led2 = 6 # 핀 번호 GPIO6 의미 (흰색)

GPIO.setup(led2, GPIO.OUT) # GPIO 6번 핀을 출력 선으로 지정.

onOff = 1 # 1은 디지털 출력 값. 1 = 5V
Onoff = 0 # 0은 디지털 출력을 멈추게 함

while True :
	distance = measure_Distance(trig, echo) 
	if(distance < 15.0): #거리가 10보다 작을 때
		ledOnOff(led2, onOff) # led가 연결된 핀에 1의 디지털 값 출력
		#ledOnOff(led1, Onoff) # led1가 연결된 핀에 1의 디지털 값 출력
	else: #거리가 20보다 클 때
		ledOnOff(led2,Onoff) # led가 연결된 핀에 0의 디지털 값 출력
		#ledOnOff(led1,Onoff) # led1가 연결된 핀에 0의 디지털 값 출력
