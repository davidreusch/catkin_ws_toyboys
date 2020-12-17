#!/usr/bin/env python
from __future__ import print_function

import roslib
#roslib.load_manifest('img_conversion')
import sys
import rospy
import cv2 as cv
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from threshold import find_matrices

#Der Code wurde uebernommen und angepasst von http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython

class image_converter:

  def __init__(self):
    #self.image_pub = rospy.Publisher("image_topic_2",Image)
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/sensors/camera/infra1/image_rect_raw",Image,self.callback)
    self.exit = False

  def callback(self,data):
    try:
      if not self.exit:
          cv_image = self.bridge.imgmsg_to_cv2(data)
          find_matrices(cv_image)
          self.exit = True

          #cv.imwrite("/home/ubuntu/cvoutput.png", cv_image)
      else:
          self.image_sub.unregister()



    except CvBridgeError as e:
      print(e)

def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")

if __name__ == '__main__':
    main(sys.argv)
