#!/usr/bin/python
#3.6

import numpy
from scipy.interpolate import CubicSpline
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point
import math


def get_spline(file):
    lane = numpy.load(file)

    arc = lane[:, 0]
    X = lane[:, 1]
    Y = lane[:, 2]

    arcsample = arc[0::100]
    Xsample = X[0::100]
    Ysample = Y[0::100]

    return arc, CubicSpline(arcsample, Xsample), CubicSpline(arcsample, Ysample)


def get_points_from_spline(arc, xspline, yspline):
    """get an array of (x,y) Points from a spline accessed by arc"""
    xspline = xspline(arc)
    yspline = yspline(arc)
    points = []
    for i in range(len(xspline)):
        points.append((xspline[i], yspline[i]))

    return points


def dist(p1, p2):
    """calc. distance between two points, second has index on position 0"""
    x1, y1 = p1
    arc, x2, y2 = p2
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


def closest_dist(targetpoint, pointarray):
    """finds the point from pointarray with closest distance to targetpoint"""
    min_dist, min_point = dist(targetpoint, pointarray[0]), pointarray[0]
    for i in range(len(pointarray)):
        cur_dist = dist(targetpoint, pointarray[i])
        if cur_dist < min_dist:
            min_dist = cur_dist
            min_point = pointarray[i]
    return min_point


def closest_point(spline, targetpoint, lookahead = 0):
    """calculate closest point to targetpoint on spline. lookahead gives a point a certain distance further on the spline"""
    arc, xspline, yspline = spline
    arclen = len(arc)
    step = 128
    low = 0
    high = arclen
    index = 0
    while (step > 0 and low != high):

        # get points on the spline from low to high with distance step, add index to retrieve point on spline later
        points = []
        for i in range(low, high, step):
            points.append((i, xspline(arc[i]), yspline(arc[i])))

        # get closest point to target in the sampled points
        if len(points) > 0:
            point = closest_dist(targetpoint, points)


        # get the point left an right to closest point in the sample
        index = point[0]
        low = (index - step) % arclen
        high = (index + step) % arclen

        # smaller step for next iteration
        step //= 2

    # if we have lookahead, get point on spline with further lookahead
    if lookahead > 0:
        lookahead = (index + lookahead) % arclen
        point = Point(x = xspline(arc[lookahead]), y = yspline(arc[lookahead]), z = 0.0)
    else:
        point = Point(x = point[1], y = point[2], z = 0.0)

    print(point)

    return point


def gps_callback(data):
    global gps_pos
    gps_pos = data.pose.pose.position

def lane_callback(data):
    global lane
    lane = data.data

# --- Main ---
rospy.init_node('spliner', anonymous=True)

#sub = rospy.Subscriber("/communication/gps/6", Odometry, gps_callback)
gps_sub = rospy.Subscriber('/sensors/localization/filtered_map', Odometry, gps_callback)
# subscriber writes the clicked Point into the variable clickedPoint
#lane_sub = rospy.Subscriber('/toyboys_lane', int, lane_callback)

gps_pos = Point()

lane = 1

spline1 = get_spline("/home/julian/Downloads/lane1.npy")
spline2 = get_spline("/home/julian/Downloads/lane2.npy")

closest_point_pub = rospy.Publisher('/lookahead', Point, queue_size=100)

while not rospy.is_shutdown():
    if lane == 1:
        point = closest_point(spline1, (gps_pos.x, gps_pos.y), lookahead=3)
        closest_point_pub.publish(point)
    elif lane == 2:
        point = closest_point(spline2, (gps_pos.x, gps_pos.y), lookahead=3)
        closest_point_pub.publish(point)

try:
    rospy.spin()
except KeyboardInterrupt:
    print("Shutting down")
