#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_srvs.srv import Trigger, TriggerResponse
from sensor_msgs.msg import Joy

class JoyTwist(object):
    def __init__(self):
        self._joy_sub = rospy.Subscriber('/joy', Joy, self.joy_callback, queue_size=1)
        self._twist_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

        self.level = 1

    def limitter(self, lvl):
	if lvl <= 0:	return 1
	if lvl >= 5: 	return 4
	return lvl

    def joy_callback(self, joy_msg):
        if joy_msg.buttons[7] == 1: self.level += 1
        if joy_msg.buttons[6] == 1: self.level -= 1

	self.level = self.limitter(self.level)

        if joy_msg.buttons[0] == 1:
            twist = Twist()
            twist.linear.x = joy_msg.axes[1] * 0.2 * self.level
            twist.angular.z = joy_msg.axes[0] * 3.14/4 * self.level
            self._twist_pub.publish(twist)
#        elif joy_msg.buttons[2] == 1: # B dash
#            twist = Twist()
#            twist.linear.x = joy_msg.axes[1] * 0.4
#            twist.angular.z = joy_msg.axes[0] * 3.14/2
#            self._twist_pub.publish(twist)
	elif joy_msg.axes[1] > 0.5:  # analog controller (experiment)
            twist = Twist()
            twist.linear.x = joy_msg.axes[3] * 0.2
            twist.angular.z = joy_msg.axes[2] * 3.14/2
            self._twist_pub.publish(twist)


if __name__ == '__main__':
    rospy.wait_for_service('/motor_on')
    rospy.wait_for_service('/motor_off')
    rospy.on_shutdown(rospy.ServiceProxy('/motor_off', Trigger).call)
    rospy.ServiceProxy('/motor_on', Trigger).call()
    rospy.init_node('logicool_cmd_vel')
    logicool_cmd_vel = JoyTwist()
    rospy.spin()
