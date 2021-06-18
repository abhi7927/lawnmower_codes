import RPi.GPIO as GPIO          
import time

GPIO.setmode(GPIO.BCM)
temp1=1

TRIGL = 23 
ECHOL = 24

TRIGR = 17
ECHOR = 21

TRIGM = 25
ECHOM = 26

GPIO.setup(TRIGL,GPIO.OUT)
GPIO.setup(ECHOL,GPIO.IN)

GPIO.setup(TRIGR,GPIO.OUT)
GPIO.setup(ECHOR,GPIO.IN)

GPIO.setup(TRIGM,GPIO.OUT)
GPIO.setup(ECHOM,GPIO.IN)

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
    GPIO.output(TRIGL, False)
    GPIO.output(TRIGR, False)
    GPIO.output(TRIGM, False)
    time.sleep(2)

    GPIO.output(TRIGL, True)
    time.sleep(0.00001)
    GPIO.output(TRIGL, False)
    
    while GPIO.input(ECHOL)==0:
        pulse_start_L = time.time()

    while GPIO.input(ECHOL)==1:
        pulse_end_L = time.time()
        
    pulse_duration_L = pulse_end_L - pulse_start_L
      
    distanceL = pulse_duration_L * 17150

    distanceL= round(distanceL, 2)
    print ("Left Distance:",distanceL,"cm\n")





    
    GPIO.output(TRIGM, False)
    time.sleep(2)

    
    GPIO.output(TRIGM, True)
    time.sleep(0.00001)
    GPIO.output(TRIGM, False)
    
    while GPIO.input(ECHOM)==0:
        pulse_start_M = time.time()

    while GPIO.input(ECHOM)==1:
        pulse_end_M = time.time()
    pulse_duration_M = pulse_end_M - pulse_start_M
    
    distanceM = pulse_duration_M * 17150

    distanceM = round(distanceM, 2)
    print ("Middle Distance:",distanceM,"cm\n")
    
    
    
    
    
    

    GPIO.output(TRIGR, False)
    time.sleep(2)

    GPIO.output(TRIGR, True)
    time.sleep(0.00001)
    GPIO.output(TRIGR, False)       
    while GPIO.input(ECHOR)==0:
        pulse_start_R = time.time()

    while GPIO.input(ECHOR)==1:
        pulse_end_R = time.time()

    pulse_duration_R = pulse_end_R - pulse_start_R
    distanceR = pulse_duration_R * 17150

    distanceR = round(distanceR, 2)
    print ("Right Distance:",distanceR,"cm\n")
    return distanceL, distanceM, distanceR
    
while(True):
    distanceL, distanceM, distanceR = exe_ultrasonic()
    print("To quit press 'e' :")
    
    exe_motor('r')
    exe_motor('h')
    

    if distanceL <=10 or distanceM <=10 or distanceR <=10:
        exe_motor('s')
        
    if distanceL 
    
    
    
    

        

    
    