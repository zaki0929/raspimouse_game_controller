#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from geometry_msgs.msg import Twist
from std_srvs.srv import Trigger, TriggerResponse
from sensor_msgs.msg import Joy


class JoyTwist(object):
    def __init__(self):
        self._joy_sub = rospy.Subscriber('/joy', Joy, self.joy_callback, queue_size=1)
        self._twist_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

    def joy_callback(self, joy_msg):
        twist = Twist()
        if joy_msg.buttons[0] == 1:
            twist.linear.x = joy_msg.axes[7] * 0.2
            twist.angular.z = joy_msg.axes[6] * 3.14 / 4
        else:
            twist.linear.x = 0
            twist.angular.z = 0
        self._twist_pub.publish(twist)


if __name__ == '__main__':
    rospy.wait_for_service('/motor_on')
    rospy.wait_for_service('/motor_off')
    rospy.on_shutdown(rospy.ServiceProxy('/motor_off', Trigger).call)
    rospy.ServiceProxy('/motor_on', Trigger).call()
    rospy.init_node('ps4_cmd_vel')
    ps4_cmd_vel = JoyTwist()
    rospy.spin()
