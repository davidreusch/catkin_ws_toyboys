#!/usr/bin/python3.6

import numpy
from scipy.interpolate import CubicSpline

import rospy
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point
import cv2 as cv
from matplotlib import pyplot as plt
import sys
import random
import math

def get_spline(file):
    lane = numpy.load(file)

    arc = lane[:,0]
    X = lane[:,1]
    Y = lane[:,2]

    arcsample = arc[0::100]
    Xsample = X[0::100]
    Ysample = Y[0::100]

    xspline = CubicSpline(arcsample,Xsample)
    yspline = CubicSpline(arcsample,Ysample)

    xspline = xspline(arc)
    yspline = yspline(arc)
    points = []
    for i in range(len(xspline)):
        points.append((xspline[i], yspline[i]))

    return points

rospy.init_node('spliner', anonymous=True)
spline = get_spline("/home/davidlin/robotik/u10/lane2.npy")

pub = rospy.Publisher('/spline', Marker, queue_size=100 )
pointarray = [Point(x = x,y = y,z = 0.0) for (x, y) in spline]

print(len(pointarray))

msg = Marker()
msg.type = 4
msg.points = pointarray
msg.header.frame_id = "map"
msg.color.r = 100
msg.color.a = 100
msg.scale.x = 1
msg.scale.y = 1
msg.scale.z = 1

while not rospy.is_shutdown():
    pub.publish(msg)

try:
   rospy.spin()
except KeyboardInterrupt:
 print("Shutting down")

