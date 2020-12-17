#!/usr/bin/env python

import rospy
from math import sqrt
from autominy_msgs.msg import SpeedCommand, NormalizedSteeringCommand, Tick
from nav_msgs.msg import Odometry
from std_msgs.msg import String, Float32

#Code ist inspiriert vom Beispielcode simple_drive_control aus Aufg. 2

epsilon = 0.001   # threshold to mitigate inaccuracy of ceiling cams 
                  # position measurement

angle = 0.0
speed = 0.2
distance = 1.0

last_odom = None

last_ceiling = None

is_active = False

ticks = 0

def callbackTick(msg):
    global ticks
    ticks += msg.value


def callbackOdom(msg):
    global last_odom
    last_odom = msg

def callbackCeiling(msg):
    global last_ceiling
    last_ceiling = msg

def drive(distance, speed, angle):
    global is_active
    global ticks

    rospy.loginfo("%s: Running (%f)", rospy.get_caller_id(), distance)
    if distance <= 0:
        rospy.logerr(
            "%s: Error, distance argument has to be > 0! %f given",
            rospy.get_caller_id(),
            distance)
        return

    pub_info.publish("BUSY")
    if is_active:
        rospy.logwarn(
            "%s: Warning, another command is still active! Please wait and try again.",
            rospy.get_caller_id())
        return

    is_active = True

    # stop the car 
    speed_cmd = SpeedCommand()
    speed_cmd.value = 0
    pub_speed.publish(speed_cmd)
    rospy.sleep(1)
    #set steering angle + speed
    steering_cmd = NormalizedSteeringCommand()
    steering_cmd.value = angle
    pub_steering.publish(steering_cmd)
    rospy.sleep(1)

    last_pos = last_ceiling.pose.pose.position
    current_distance = 0
    speed_cmd.value = speed
    pub_speed.publish(speed_cmd)
    distance_per_round = 0
    abs_distance = 0
    rounds = 0 
    if angle == 0.0:
        num_rounds = 1 
    else: 
        num_rounds = 5

    while not rospy.is_shutdown(): 
        current_pos = last_ceiling.pose.pose.position

        current_distance = sqrt(
            (current_pos.x - last_pos.x)**2 + (current_pos.y - last_pos.y)**2)
        if current_distance > epsilon:
            distance_per_round += current_distance
            abs_distance += current_distance

        last_pos = current_pos
        rospy.loginfo("current distance = %f", distance_per_round)

        #drive for num_rounds rounds and reset distance after 1 meter
        if distance_per_round >= 1.0:
            rounds += 1
            distance_per_round = 0
            if rounds >= num_rounds:
                break

        rospy.sleep(0.1)

    speed_cmd.value = 0
    pub_speed.publish(speed_cmd)
    is_active = False

    ratio = ticks/abs_distance
    pub_info.publish("FINISHED")

    rospy.sleep(0.3)
    rospy.loginfo(
            "%s: Finished (%f)\nActual travelled distance = %f\nTicks = %f\nTicks per meter: %f",
        rospy.get_caller_id(),
        distance,
        abs_distance,
        ticks, ratio)

#Main
# --- Initialize Node ---
rospy.init_node("drive_1m")

# --- Subscribers ---
ceiling_cam_sub = rospy.Subscriber('/communication/gps/7', Odometry, callbackCeiling)
sub_odom = rospy.Subscriber("/sensors/odometry/odom", Odometry, callbackOdom, queue_size=100)
sub_ticks = rospy.Subscriber("/sensors/arduino/ticks", Tick, callbackTick, queue_size=100)

# --- Publishers ---
pub_speed = rospy.Publisher("/actuators/speed", SpeedCommand, queue_size=100)
pub_steering = rospy.Publisher(
    "/actuators/steering_normalized",
    NormalizedSteeringCommand,
    queue_size=100)
pub_info = rospy.Publisher("simple_drive_control/info", String, queue_size=100)

# --- start ---
rospy.loginfo(rospy.get_caller_id() + ": started!")
drive(distance,speed,angle)


# spin() simply keeps python from exiting until this node is stopped
rospy.spin()
