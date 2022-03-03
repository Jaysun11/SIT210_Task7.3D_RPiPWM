import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

TRIGGER = 16
ECHO    = 18
buzzerpin = 12

GPIO.setup(TRIGGER,GPIO.OUT)  
GPIO.setup(ECHO,GPIO.IN)     
GPIO.setup(buzzerpin, GPIO.OUT)


GPIO.output(TRIGGER, False)

buzzer = GPIO.PWM(buzzerpin, 1000) 
buzzer.start(10)


while True:

    # Allow module to settle
    time.sleep(1)

    # Send 10us pulse to trigger
    GPIO.output(TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(TRIGGER, False)
    start = time.time()

    while GPIO.input(ECHO)==0:
      start = time.time()

    while GPIO.input(ECHO)==1:
      stop = time.time()


    timeTaken = stop-start

    distanceThereAndBack = timeTaken * 34300

    distance = distanceThereAndBack / 2
    
    buzzer.ChangeFrequency(5000/distance)

    print(distance)
   

