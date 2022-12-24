import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
buzzer = 12
button = 21
scale = [ 261, 294, 329, 349, 392, 440, 493, 523 ]
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(button, GPIO.IN, GPIO.PUD_DOWN)
btnStatus = 0
p = GPIO.PWM(buzzer, 100)

def soundOnOff(buzzer, onOff):
    p.start(100) # pwm 시작
    p.ChangeDutyCycle(90) # dutycycle 변경
    for i in range(len(list)): #len() => 길이 추출
        p.ChangeFrequency(scale[list[i]]) #주파수 변경
        if (i+1)%7 == 0: # 7번째 음 박자 변경
          time.sleep(1)
        else :
          time.sleep(0.5)

def buttonPressed(pin):
    global btnStatus
    btnStatus = 0 if btnStatus ==1 else 1
    soundOnOff(buzzer, btnStatus)

while True:
    if GPIO.input(button) == 1:
        p.stop()
    else:
        p.start(100)
        time.sleep(100)

# 핀 21에 올라가는 에지가 발견되면 buttonPressed 를 호출하도록 지정
# 200ms 사에 발생한 에지는 무시
print("스위치를 누르면 LED가 On되고 다시 누르면 Off됩니다.")
while True :
    pass