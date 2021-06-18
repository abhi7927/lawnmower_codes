import time
import RPi.GPIO as GPIO 

class test:
    def __init__(self):
        self.a=1
        
    def test_fun(self, val):
        time.sleep(val)
        print("HELLO")
        self.obj1=slave()
        self.obj1.slave_fun(2)
        print("Object created after 3seconds" )


class slave:
    def __init__(self):
        self.a=1
        
    def slave_fun(self, val):
        time.sleep(val)
        print("HELLO")
        
        print("Object created")
    
a1 = test()
a1.test_fun(1)