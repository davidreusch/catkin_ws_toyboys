#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from autominy_msgs.msg import Speed
from autominy_msgs.msg import NormalizedSteeringCommand
from autominy_msgs.msg import SpeedCommand
from nav_msgs.msg import Odometry
from autominy_msgs.msg import SteeringFeedback
import numpy
import math
#from drive1sec import driver

class takePoints():
    def __init__(self):
        self.steering_val = 0
        self.x = 0
        self.y = 0
        ceiling_cam_sub = rospy.Subscriber('/communication/gps/7', Odometry, self.ceiling_callback)
        steering_angle_sub = rospy.Subscriber('/sensors/arduino/steering_angle', SteeringFeedback, self.steering_callback)

    def ceiling_callback(self,data):
        self.x = data.pose.pose.position.x
        self.y = data.pose.pose.position.y
        #print(self.x, self.y)
    
    def steering_callback(self,data):
        self.steering_val = data.value

def driver(steer_pub, speed_pub):
    steer_msg = NormalizedSteeringCommand()
    steer_msg.value = -1.0
    steer_pub.publish(steer_msg)
    speed_msg = SpeedCommand()
    speed_msg.value = 0.3
    speed_pub.publish(speed_msg)
    rospy.sleep(2.5)
    speed_msg.value = 0.0
    speed_pub.publish(speed_msg)

if __name__ == '__main__':
    try:
        rospy.init_node('measurement', anonymous=True)
        steer_pub = rospy.Publisher('/actuators/steering_normalized', NormalizedSteeringCommand, queue_size=10)
        speed_pub = rospy.Publisher('/actuators/speed', SpeedCommand, queue_size=10)
        points = takePoints()


        rospy.sleep(4)
        x1 = points.x
        y1 = points.y
        print(x1, y1,points.steering_val)
        driver(steer_pub,speed_pub)
        #points = takePoints()
        rospy.sleep(1)
        x2 = points.x
        y2 = points.y
        print(x2, y2,points.steering_val)
        driver(steer_pub,speed_pub)
        #points = takePoints()
        rospy.sleep(1)
        x3 = points.x
        y3 = points.y
        print(x3, y3, points.steering_val)

        a = numpy.float64([[1, -x1, -y1], [1, -x2, -y2], [1, -x3, -y3]])
        b = numpy.float64([-(x1*x1 + y1*y1), -(x2*x2 + y2*y2),-(x3*x3 + y3*y3)])
        res = numpy.linalg.solve(a, b)
        xm = res[1] / 2
        ym = res[2] / 2
        r = math.sqrt((xm*xm + ym*ym - res[0]))
        #r = ((xm - x1)**2 + (ym-y1)**2)**(1/2)
        print("xm: ",xm,"ym: ", ym, "radius: ", r)


        
        rospy.spin()
        
    except rospy.ROSInterruptException:
        pass
