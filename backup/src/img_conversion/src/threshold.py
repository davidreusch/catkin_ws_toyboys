from __future__ import print_function
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import sys
import numpy

def find_matrices(img):
    #einlesen des aus ROS extrahierten Bildes
    #img = cv.imread('cvoutput.png',0)

    #Binarisierung des Bildes
    ret,thresh = cv.threshold(img,140,255,cv.THRESH_BINARY)

    #cv.imwrite("cvbinary.png", thresh)

    def get_marker_middle(y1, y2, x1, x2):
        "Funktion, um Mittelpunkt der weissen Pixel eines Rechtecks zu finden"
        y_sum = 0
        x_sum = 0
        count = 0
        for y in range(y1, y2):
            for x in range(x1, x2):
                if thresh[y,x] > 0:
                    y_sum += y
                    x_sum += x
                    count += 1

        if count > 0:
            return [y_sum / count, x_sum / count]

    #durch scharfes Hinsehen Pixelkoordinaten der Rechtecke um Marker gefunden:
    marker_coords = [(229,253,193,229), #bottom left
                    (220,240,485,524),  #bottom right
                    (160,180,230,260),  #middle left
                    (130,160,430,462),  #middle right
                    (109,130,258,280),  #up left
                    (100,120,405,430)]  #up right

    #Mittelpunkte der Marker berechnen
    marker_middles_cam = []
    for coords in marker_coords:
        marker_middles_cam.append(get_marker_middle(*coords))


    #in numpy convertieren damit solvePnP gluecklich ist
    marker_middles_cam = numpy.float32(marker_middles_cam)

    #Weltmittelpunkte aus Aufgabe gegeben
    marker_middles_world = numpy.float32([[0.5,0.2,0], [0.5,-0.2,0], [0.8,0.2,0], [0.8,-0.2,0], [1.1,0.2,0],[1.1,-0.2,0]])

    #Die Kameramatrix mit den Werten aus Aufgabe 1
    cameraMatrix = numpy.float64([[383.7944641113281,0, 322.3056945800781],[0, 383.7944641113281, 241.67051696777344],[0,0,1]])

    #Distortioncoefficients waren Null
    distcoeffs = numpy.float32([0,0,0,0,0])

    #solvePnP gibt uns Rodrigues und Translationsvektor
    retval, rvec, tvec = cv.solvePnP(marker_middles_world, marker_middles_cam, cameraMatrix, distcoeffs)

    #Rodrigues-Funktion wandelt rodriguesvektor in Rotationsmatrix um
    rot_mat, jacobian = cv.Rodrigues(rvec)

    print("Rotationsmatrix R:")
    print(rot_mat)

    #translationsvektor rechts anhaengen
    rot_mat_extended = numpy.append(rot_mat, tvec,1)

    #Zeile [0 0 0 1] unten anhaengen
    transformation_mat = numpy.append(rot_mat_extended, [[0,0,0,1]], 0)

    print("Transformationsmatrix:")
    print(transformation_mat)

    #Rotationsmatrix transponieren
    inverse_rot_mat = rot_mat.transpose()

    print("R transponiert:")
    print(inverse_rot_mat)

    #Translationsvektor mit -Rtransponiert multiplizieren
    tvec_inv = numpy.matmul(-inverse_rot_mat, tvec)

    #und an Rotationsmatrix anhaengen
    inv_extended = numpy.append(inverse_rot_mat, tvec_inv,1)

    #Zeile [0 0 0 1] unten anhaengen
    inv_transformation_mat = numpy.append(inv_extended, [[0,0,0,1]], 0)

    print("Inverse Transformationsmatrix:")
    print(inv_transformation_mat)


    #Zur letzten Frage: Die Rotationsmatrix wandelt Weltkoordinaten in Kamerakoordinaten um 
