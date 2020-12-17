#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from autominy_msgs.msg import Speed
from autominy_msgs.msg import NormalizedSteeringCommand
from autominy_msgs.msg import SpeedCommand
from nav_msgs.msg import Odometry
from autominy_msgs.msg import SteeringFeedback

def driver():
    steer_pub = rospy.Publisher('/actuators/steering_normalized', NormalizedSteeringCommand, queue_size=10)
    speed_pub = rospy.Publisher('/actuators/speed', SpeedCommand, queue_size=10)
    steer_msg = NormalizedSteeringCommand()
    steer_msg.value = 1.0
    steer_pub.publish(steer_msg)
    speed_msg = SpeedCommand()
    speed_msg.value = 0.3
    speed_pub.publish(speed_msg)
    rospy.sleep(1)
    speed_msg = SpeedCommand()
    speed_msg.value = 0.0
    speed_pub.publish(speed_msg)


if __name__ == '__main__':
    try:
        rospy.init_node('drive1sec', anonymous=True)
        driver()
    except rospy.ROSInterruptException:
        pass
