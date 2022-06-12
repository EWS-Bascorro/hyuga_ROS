#!/usr/bin/env python3
# Author : Ahmad Didik Setiyadi
import time
from adafruit_servokit import ServoKit # https://github.com/adafruit/Adafruit_CircuitPython_ServoKit

class GroupBulkWrite:
    def __init__(self, servo_count, i2c_address):
        self.ids = servo_count
        self.address = i2c_address
        self.id_pos = list(range(self.ids))
        
        self.servo = ServoKit(channels=16) # PCA9685Module
        #Parameters
        self.MIN_PWM = 1000
        self.MAX_PWM = 2000
        self.MIN_ANGLE = 0
        self.MAX_ANGLE = 180

        #init
        self.init()

    def init(self):
        for i in range(self.ids):
            self.servo.set_pulse_with_range(self.MIN_PWM, self.MAX_PWM)
            time.sleep(0.1)
        print("Servo initialized")
    
    def addParam(self, id, angle):
        self.id_pos[id] = angle

    def txPcaket(self):
        for id in range(self.ids):
            self.servo[id].angle = self.id_pos[id]
            time.sleep(0.01)



