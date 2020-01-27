#!/usr/bin/env python
import numpy
from scipy.interpolate import CubicSpline
import rospy
from std_msgs.msg import Float64
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point, PointStamped
from nav_msgs.msg import Odometry
from autominy_msgs.msg import SteeringAngle
import tf
from matplotlib import pyplot as plt
import sys
import random
from math import atan2


class Measurer():
    def __init__(self):
        self.initial_pose = True
        self.initial_steering = True
        self.theta = 0
        self.position = Point(x=0, y=0, z=0)
        self.steer_to = 0
        #ceiling_cam_sub = rospy.Subscriber('/communication/gps/6', Odometry, self.ceiling_callback)
        ceiling_cam_sub = rospy.Subscriber('/sensors/localization/filtered_map', Odometry, self.ceiling_callback)
        steering_angle_sub = rospy.Subscriber('/sensors/steering', SteeringAngle, self.steering_callback)
        lookahead_sub = rospy.Subscriber("/lookahead", Point, self.lookahead_callback)

    def ceiling_callback(self,data):
        self.theta = tf.transformations.euler_from_quaternion([data.pose.pose.orientation.w,data.pose.pose.orientation.x,data.pose.pose.orientation.y,data.pose.pose.orientation.z])[0]
        self.position = data.pose.pose.position

    def steering_callback(self,data):
        self.steering= data.value

    def lookahead_callback(self, data):
        self.la_point =  data
        self.steer_to_angle()

    def steer_to_angle(self):
        diff_vec = self.la_point.x - self.position.x, self.la_point.y - self.position.y
        self.steer_to = atan2(*diff_vec)






rospy.init_node("steer_to", anonymous=True)

pub = rospy.Publisher("/angle", Float64, queue_size=100)

mes = Measurer()

while not rospy.is_shutdown():
    print(mes.steer_to)
    pub.publish(mes.steer_to)
