from __future__ import print_function
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import sys
import numpy
import rospy
import random
import math

def dist_line_point(l1,l2,p):
    "gibt distanz von p zu gerade definiert durch l1, l2 zurueck"
    x1 = l1[0] 
    y1 = l1[1] 
    x2 = l2[0] 
    y2 = l2[1] 
    x0 = p[0]
    y0 = p[1]

    distance = abs((y2-y1)*x0 - (x2-x1)*y0 + x2*y1 - y2*x1) / math.sqrt((y2-y1)**2 + (x2-x1)**2)

    return distance


def ransac(img):
    rows, cols = img.shape

    #oberen Teil ganz abschneiden?
    #img = img[220:rows,:]
    #cv.imshow('beforeThresh',img)

    #Binarisierung des Bildes
    ret,thresh = cv.threshold(img,140,255,cv.THRESH_BINARY)

    #oder auf null setzen?
    rows, cols = thresh.shape
    thresh[0:220,:] = 0
    thresh[380:rows,:] = 0
    cv.imshow('afterThresh',thresh)

    #whitepixels = np.whitepixels([])
    whitepixels = []
    for x in range(cols):
        for y in range(rows):
            if thresh[y,x] > 0:
                whitepixels.append((y,x))# = numpy.append(whitepixels, [y,x])



    
    for walks in range(3):

        #number of iterations
        N = 100

        consensus_cur = []
        linepoints_cur = [0,0]
        for i in range(N):
            #we need to get two points with different x-coordinates
            #otherwise pitch is infinite
            x1 = x2 = 0
            while x1 == x2:
                sample = random.sample(whitepixels, 2)
                x1 = sample[0][1]
                x2 = sample[1][1]


            #distance threshold for accepted points
            t = 15

            consensus_new = []
            for p in whitepixels:
                if dist_line_point(sample[0],sample[1],p) <= t:
                    consensus_new.append(p)

            if len(consensus_new) > len(consensus_cur):
               consensus_cur = consensus_new 
               linepoints_cur = sample


        #get point with y coord = 0 and x coord = 0
        #rename for clarity
        y1 = linepoints_cur[0][0]
        x1 = linepoints_cur[0][1]
        y2 = linepoints_cur[1][0]
        x2 = linepoints_cur[1][1]

        #get parameters for line-equation
        a = float((y1 - y2)) / (x1 - x2)
        b = y2 - a * x2

        #get values for x zero and y zero
        xforyzero = -b / a
        xforymax = (rows -b) / a

        #yforxzero = b
        

        #show image with line
        cv.line(img,  (0,int(xforyzero)), (rows, int(xforymax)),(0,255,0), 5)
        cv.imshow(str(walks), img)

        #print(whitepixels)

        whitepixels = list(set(whitepixels) - set(consensus_cur))







    cv.waitKey(-1)
    cv.destroyAllWindows()

    




"""
        new_whitepixels = []
        for old_point in whitepixels:
            append = True
            for i in range(len(consensus_cur)):
                if consensus_cur[i] == old_point:
                    del(consensus_cur[i])
                    append = False
                    break
            if append:
                new_whitepixels.append(old_point)
        
        whitepixels = new_whitepixels
"""
