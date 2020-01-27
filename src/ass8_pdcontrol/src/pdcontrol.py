#!/usr/bin/env python
import rospy
from autominy_msgs.msg import Speed, SteeringAngle, SpeedCommand, NormalizedSteeringCommand
from nav_msgs.msg import Odometry
import numpy
import math
import tf
from std_msgs.msg import Float64
import sys

pi = math.pi


class OdoMeasurer:
    def __init__(self):
        self.initial_pose = True
        self.initial_steering = True
        self.theta = 0
        self.wanted_angle = pi
        #ceiling_cam_sub = rospy.Subscriber('/communication/gps/6', Odometry, self.ceiling_callback)



        ceiling_cam_sub = rospy.Subscriber('/sensors/localization/filtered_map', Odometry, self.ceiling_callback)
        steering_angle_sub = rospy.Subscriber('/sensors/steering', SteeringAngle, self.steering_callback)
        wanted_angle_sub = rospy.Subscriber("/angle", Float64, self.wanted_angle_callback)

    def ceiling_callback(self, data):
        self.theta = tf.transformations.euler_from_quaternion(
            [data.pose.pose.orientation.w, data.pose.pose.orientation.x, data.pose.pose.orientation.y,
             data.pose.pose.orientation.z])[0]

    def steering_callback(self, data):
        self.steering = data.value

    def wanted_angle_callback(self, data):
        self.wanted_angle = data.data


def error_signed(wanted_angle, theta):

    # 1: steer fully left, -1: steer fully right

    angle = theta - wanted_angle # einfache subtraktion gibt uns kleinsten winkel ohne wrap

    if angle < 0:
        counter_angle = angle + 2 * pi # wenn der winkel negativ ist, kriegen wir den Gegenwinkel durch Addition von 2pi
    else:
        counter_angle = angle - 2 * pi # sonst durch Subtraktion

    if abs(angle) < abs(counter_angle):
        return angle
    else:
        return counter_angle
"""
  #  if wanted_angle > 2 * pi:
  #      wanted_angle = wanted_angle - 2 * pi

    wanted_angle %= 2*pi
    theta %= 2 * pi

    right_dist = (2 * pi - theta + wanted_angle) % (2 * pi)
#    left_dist = (2 * pi - wanted_angle + theta) % (2 * pi)
    left_dist = 2 * pi - right_dist

    #right_dist = wanted_angle - theta
    #left_dist = wanted_angle + theta

    if (right_dist) < (left_dist):
        return -right_dist  # negative value for steering to right
    else:
        return left_dist  # positive for steering to left
    """




# ---main---


rospy.init_node('my_odometry', anonymous=True)

# ---Publishers---
speed_pub = rospy.Publisher('/actuators/speed', SpeedCommand, queue_size=10)
steering_pub = rospy.Publisher('/actuators/speed', SpeedCommand, queue_size=10)
pub_steering = rospy.Publisher("/actuators/steering_normalized", NormalizedSteeringCommand, queue_size=100)

measurer = OdoMeasurer()
rospy.sleep(1)

# constants
Kp = 2
Kd = 0.5

# initialize loop variables
wanted_angle = measurer.wanted_angle
#wanted_angle = 0
theta = measurer.theta
old_error = abs(error_signed(wanted_angle, theta))
t = 0
error_diff = 0

# main loop
r = rospy.Rate(50)
while not rospy.is_shutdown():

    wanted_angle = measurer.wanted_angle
    #wanted_angle = 0
    theta = measurer.theta
    print(theta)
    speed_pub.publish(value=0.2)

    # get steering with direction
    steering = error_signed(wanted_angle, theta)
    # get absolute error
    error = abs(steering)

    # dont measure error too often, only every 16th loop
    # so the noise is not too big
    #if (t == 0):
    error_diff = (error - old_error) / math.pi
    old_error = error
    #t = (t + 1) % 16

    # control formula
    steering_angle = Kp * steering + Kd * error_diff

    pub_steering.publish(value=steering_angle)

    r.sleep()

rospy.spin()
