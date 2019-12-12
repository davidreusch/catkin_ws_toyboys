#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from autominy_msgs.msg import Speed, SteeringAngle, SpeedCommand, NormalizedSteeringCommand
from nav_msgs.msg import Odometry
import numpy
import math
import tf

goal_theta = 0


class OdoMeasurer():
    def __init__(self):
        self.initial_pose = True
        self.initial_steering = True
        self.initial_x = 0
        self.initial_y = 0
        self.theta = 0 
        self.speed = 0
        ceiling_cam_sub = rospy.Subscriber('/communication/gps/5', Odometry, self.ceiling_callback)
#        odom_sub = rospy.Subscriber('/sensors/localization/filtered_map', Odometry, self.odom_callback)
        steering_angle_sub = rospy.Subscriber('/sensors/steering', SteeringAngle, self.steering_callback)
        speed_sub = rospy.Subscriber('/sensors/speed', Speed, self.speed_callback)

    def ceiling_callback(self,data):
#        self.initial_x = data.pose.pose.position.x
#        self.initial_y = data.pose.pose.position.y
        #eher 2*math.acos...?
        self.theta = tf.transformations.euler_from_quaternion([data.pose.pose.orientation.w,data.pose.pose.orientation.x,data.pose.pose.orientation.y,data.pose.pose.orientation.z])[0]

    def odom_callback(self,data):
        #eher 2*math.acos...?
        self.theta = 2 * math.acos(data.pose.pose.orientation.w)
    
    def steering_callback(self,data):
        self.steering= data.value

    def speed_callback(self,data):
        self.speed= data.value




def ferror(wanted_angle,theta):
    return abs(wanted_angle - abs(theta))

def fsteering(wanted_angle, theta):

    error = 0
    if wanted_angle == 0:
        error = (theta / math.pi) 
    elif wanted_angle == math.pi:
        if theta < 0:
            error = (math.pi + theta) / math.pi
        else:
            error = (math.pi - theta) / -math.pi
    return error



rospy.init_node('my_odometry', anonymous=True)
#odom_pub = rospy.Publisher('/my_odom', Odometry, queue_size=100 )
speed_pub = rospy.Publisher('/actuators/speed', SpeedCommand, queue_size=10)
steering_pub = rospy.Publisher('/actuators/speed', SpeedCommand, queue_size=10)
pub_steering = rospy.Publisher("/actuators/steering_normalized",NormalizedSteeringCommand,queue_size=100)


direction = 0

odo = OdoMeasurer()
rospy.sleep(1)

r = rospy.Rate(100)
Kp = 0.9
wanted_angle = 0
theta = odo.theta
old_error = ferror(wanted_angle, theta)
t = 0
while not rospy.is_shutdown():

    theta = odo.theta
    print(theta)
    
    error = ferror(wanted_angle, theta)
    steering_angle = Kp * fsteering(wanted_angle, theta)


    pub_steering.publish(value=steering_angle)
    speed_pub.publish(value=0.2)
    
    if (t % 5 == 0):
        m = - (old_error - error)
        old_error = error
        print(m)


    
    t = (t+1) % 1000
    
    r.sleep()

speed_pub.publish(value=0)


rospy.spin()


