#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy, time
from std_srvs.srv import Trigger, TriggerResponse
from raspimouse_ros_2.msg import MotorFreqs
from sensor_msgs.msg import Joy


class JoyTwist(object):
    def __init__(self):
        self._joy_sub = rospy.Subscriber('/joy', Joy, self.joy_callback, queue_size=1)
        self.motor_pub = rospy.Publisher('/motor_raw', MotorFreqs, queue_size=1)

        self.level = 0

        self.accel = [349, 392, 440, 466, 523, 587, 622, 698, 784]
        self.durat = [0.6, 0.3, 0.3, 0.2, 0.2, 0.2, 0.2, 0.2, 3.0]

    def limitter(self, lvl):
        if lvl < 0:    return 0
        if lvl >= 9:    return 8
        return lvl

    def joy_callback(self, joy_msg):
        self.level = self.limitter(self.level)

        m = MotorFreqs()
        if joy_msg.buttons[0] == 1:
            m.left_hz = self.accel[self.level]
            m.right_hz = self.accel[self.level]
            self.motor_pub.publish(m)
        else:
            self.level = 0
            m.left_hz = 0
            m.right_hz = 0
            self.motor_pub.publish(m)
            return

        time.sleep(self.durat[self.level])
        self.level += 1


if __name__ == '__main__':
    rospy.wait_for_service('/motor_on')
    rospy.wait_for_service('/motor_off')
    rospy.on_shutdown(rospy.ServiceProxy('/motor_off', Trigger).call)
    rospy.ServiceProxy('/motor_on', Trigger).call()
    rospy.init_node('logicool_cmd_vel')
    logicool_cmd_vel = JoyTwist()
    rospy.spin()
