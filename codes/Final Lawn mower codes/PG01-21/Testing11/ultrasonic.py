import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIGL = 23 
ECHOL = 24

TRIGR = 17
ECHOR = 21

TRIGM = 25
ECHOM = 26
print("Distance Measurement In Progress")

GPIO.setup(TRIGL,GPIO.OUT)
GPIO.setup(ECHOL,GPIO.IN)

GPIO.setup(TRIGR,GPIO.OUT)
GPIO.setup(ECHOR,GPIO.IN)

GPIO.setup(TRIGM,GPIO.OUT)
GPIO.setup(ECHOM,GPIO.IN)
try:
    while True:

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
        
           
        
       
        
except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    gpio.cleanup()