# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 18:25:43 2019

@author: Abhimanyu
"""

import keras
import cv2
import glob
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
import numpy as np

lap_filter = np.array([[0,1,0],[1,-4,1],[0,1,0]])
n=cv2.imread("leaf image.jpg")
n = cv2.resize(n,(800,600))
gray = cv2.cvtColor(n, cv2.COLOR_BGR2GRAY)
median = cv2.medianBlur(gray,5)
lap_image = cv2.filter2D(median,-1,lap_filter)
inv=cv2.bitwise_not(lap_image)
cv2.imshow("or",n)
cv2.imshow("median",median)
cv2.imshow("lap_image",lap_image)
cv2.imshow("x",inv)
cv2.waitKey(0)
cv2.destroyAllWindows()