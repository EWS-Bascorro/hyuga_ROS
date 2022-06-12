#!/usr/bin/env python3

import rospy, rospkg
from sdk.group_bulk_write import GroupBulkWrite
from servo_controller.msg import ServoPosList

rospy.init_node('servo_control_node')

servo_handler1 = GroupBulkWrite(16, 0x40) # PCA9685Module
servo_handler2 = GroupBulkWrite(4, 0x41) # PCA9685Module

def servo_callback(data):
    for id in range(len(data.servo_pos)):
        servo_handler1.addParam(id, data.servo_pos[id])
        if (id > 15): # PCA9685Module only has 16 channels
            servo_handler2.addParam(id-16, data.servo_pos[id])
    servo_handler1.txPacket()
    servo_handler2.txPacket()

if __name__ == '__main__':
    rospy.loginfo("Servo control node started")
    rospy.Subscriber("/servo_pos_list", ServoPosList, servo_callback)
    rate = rospy.Rate(60) # 60hz
    rospy.spin()
    rospy.loginfo("Servo control node stopped")