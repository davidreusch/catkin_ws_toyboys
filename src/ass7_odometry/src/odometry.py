#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from autominy_msgs.msg import Speed, SteeringAngle
from nav_msgs.msg import Odometry
import numpy
import math

class OdoMeasurer():
    def __init__(self):
        self.initial_pose = True
        self.initial_steering = True
        self.initial_x = 0
        self.initial_y = 0
        self.initial_theta = 0 
        self.speed = 0
        #ceiling_cam_sub = rospy.Subscriber('/communication/gps/7', Odometry, self.ceiling_callback)
        odom_sub = rospy.Subscriber('/sensors/localization/filtered_map', Odometry, self.odom_callback)
        steering_angle_sub = rospy.Subscriber('/sensors/steering', SteeringAngle, self.steering_callback)
        speed_sub = rospy.Subscriber('/sensors/speed', Speed, self.speed_callback)

    def odom_callback(self,data):
        if self.initial_pose:
            self.initial_x = data.pose.pose.position.x
            self.initial_y = data.pose.pose.position.y
            self.initial_theta = math.acos(data.pose.pose.orientation.w)

            self.initial_pose = False

    def ceiling_callback(self,data):
        self.x = data.pose.pose.position.x
        self.y = data.pose.pose.position.y
        #print(self.x, self.y)
    
    def steering_callback(self,data):
        self.steering= data.value

    def speed_callback(self,data):
        self.speed= data.value






rospy.init_node('my_odometry', anonymous=True)
odom_pub = rospy.Publisher('/my_odom', Odometry, queue_size=100 )
#speed_pub = rospy.Publisher('/actuators/speed', SpeedCommand, queue_size=10)


odo = OdoMeasurer()
rospy.sleep(1)

last_x = odo.initial_x
last_y = odo.initial_y
last_theta = odo.initial_theta

l = 0.27

r = rospy.Rate(100)
while not rospy.is_shutdown():
    v = odo.speed
    new_x = last_x + 0.01 * v * math.cos(last_theta)
    new_y = last_y + 0.01 * v * math.sin(last_theta)
    new_theta = last_theta + 0.01 *  (v / l) * math.tan(odo.steering)
    msg = Odometry()
    msg.header.frame_id = "map"
    msg.child_frame_id = "base_link"
    msg.pose.pose.position.x = new_x
    msg.pose.pose.position.y = new_y
    msg.pose.pose.position.z = 1
    msg.pose.pose.orientation.w = math.cos(new_theta / 2)
    msg.pose.pose.orientation.z = math.sin(new_theta / 2)
    odom_pub.publish(msg)
    last_x = new_x
    last_y = new_y
    last_theta = new_theta
    
    r.sleep()



rospy.spin()


