#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from autominy_msgs.msg import Speed, SteeringAngle, SpeedCommand, NormalizedSteeringCommand
from nav_msgs.msg import Odometry
import numpy
import math

goal_theta = 0


class OdoMeasurer():
    def __init__(self):
        self.initial_pose = True
        self.initial_steering = True
        self.initial_x = 0
        self.initial_y = 0
        self.theta = 0 
        self.speed = 0
        #ceiling_cam_sub = rospy.Subscriber('/communication/gps/7', Odometry, self.ceiling_callback)
        odom_sub = rospy.Subscriber('/sensors/localization/filtered_map', Odometry, self.odom_callback)
        steering_angle_sub = rospy.Subscriber('/sensors/steering', SteeringAngle, self.steering_callback)
        speed_sub = rospy.Subscriber('/sensors/speed', Speed, self.speed_callback)

    def ceiling_callback(self,data):
        self.initial_x = data.pose.pose.position.x
        self.initial_y = data.pose.pose.position.y
        #eher 2*math.acos...?
        self.theta = 2 * math.acos(data.pose.pose.orientation.w)

    def odom_callback(self,data):
        #eher 2*math.acos...?
        self.theta = 2 * math.acos(data.pose.pose.orientation.w)
    
    def steering_callback(self,data):
        self.steering= data.value

    def speed_callback(self,data):
        self.speed= data.value






rospy.init_node('my_odometry', anonymous=True)
#odom_pub = rospy.Publisher('/my_odom', Odometry, queue_size=100 )
speed_pub = rospy.Publisher('/actuators/speed', SpeedCommand, queue_size=10)
steering_pub = rospy.Publisher('/actuators/speed', SpeedCommand, queue_size=10)
pub_steering = rospy.Publisher("/actuators/steering_normalized",NormalizedSteeringCommand,queue_size=100)


direction = 0

odo = OdoMeasurer()
rospy.sleep(1)

speed_command = SpeedCommand()
speed_command.value = 0.2


r = rospy.Rate(100)
while not rospy.is_shutdown():

    theta = odo.theta
    print(theta)
    if theta < math.pi:
        direction = 1  # steer to the right
    else:
        direction = -1  # steer to left

    if theta < math.pi:
        error = theta
    else:
        error = 2 * math.pi - theta

    steering_angle = (error / math.pi) * direction

    pub_steering.publish(value=steering_angle)
    speed_pub.publish(value=0.2)
    
    
    r.sleep()



rospy.spin()


