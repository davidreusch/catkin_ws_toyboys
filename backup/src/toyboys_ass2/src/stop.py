#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from autominy_msgs.msg import Speed
from autominy_msgs.msg import NormalizedSteeringCommand
from autominy_msgs.msg import SpeedCommand

def talker():
    steer_pub = rospy.Publisher('/actuators/steering_normalized', NormalizedSteeringCommand, queue_size=10)
    speed_pub = rospy.Publisher('/actuators/speed', SpeedCommand, queue_size=10)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        steer_msg = NormalizedSteeringCommand()
        steer_msg.value = 0.0
        steer_pub.publish(steer_msg)
        speed_msg = SpeedCommand()
        speed_msg.value = 0.0
        speed_pub.publish(speed_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
