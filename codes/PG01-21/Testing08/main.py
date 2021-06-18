import RPi.GPIO as GPIO          
import time

GPIO.setmode(GPIO.BCM)
temp1=1

TRIG = 23 
ECHO = 24

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

in1 = 4
in2 = 13
ena = 16

in3 = 18
in4 = 19
enb = 20

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(ena,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
m1=GPIO.PWM(ena,1000)

m1.start(25)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
m2=GPIO.PWM(enb,1000)

m2.start(25)
    
def exe_motor(x):
    global temp1,in1,in2,in3,in4,ena,enb
    if x=='r':
        print("run")
        if(temp1==1):
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
         GPIO.output(in3,GPIO.HIGH)
         GPIO.output(in4,GPIO.LOW)
         print("forward")
         x='z'
        else:
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.HIGH)
         GPIO.output(in3,GPIO.LOW)
         GPIO.output(in4,GPIO.HIGH)
         print("backward")
         x='z'


    elif x=='s':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        x='z'

    elif x=='f':
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='b':
        print("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        temp1=0
        x='z'
    
    elif x=='lt':
        if(temp1==1):
            print("Forward left")
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
            x='z'
        else:
            print("Backward left")
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
            x='z'
        
    elif x=='rt':
        if(temp1==1):
            print("Forward right")
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in4,GPIO.LOW)
            x='z'
        else:
            print("Backward right")
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)
            x='z'

    elif x=='l':
        print("low")
        m1.ChangeDutyCycle(25)
        m2.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        print("medium")
        m1.ChangeDutyCycle(50)
        m2.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        print("high")
        m1.ChangeDutyCycle(100)
        m2.ChangeDutyCycle(100)
        x='z'
    
    elif x=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
    
def exe_ultrasonic():
    global TRIG,ECHO
    GPIO.output(TRIG, False)
    print("Waiting For Sensor To Settle")
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
      pulse_start = time.time()

    while GPIO.input(ECHO)==1:
      pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    print ("Distance:",distance,"cm")
    
    return distance





while(True):
    distance=exe_ultrasonic()
    print("To quit press 'e' :")

    if distance <= 15:
        exe_motor('s')
        exe_motor('e')
        break
        
    else:
        exe_motor('r')
        x=input()
        exe_motor(x)
        
        

    
    