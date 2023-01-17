# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:06:43 2019

@author: Abhimanyu
"""

import cv2
import numpy as np

img=cv2.imread("leaf image.jpg")
img_b=cv2.blur(img,(3,3))
hsv=cv2.cvtColor(img_b, cv2.COLOR_BGR2HSV)

lower_green = np.array([36, 25, 25])
upper_green = np.array([70, 255,255])


mask = cv2.inRange(hsv, lower_green, upper_green)
output = cv2.bitwise_and(img_b,img_b,mask=mask)

avg_color_per_row = np.average(output, axis=0)
avg_color = np.average(avg_color_per_row, axis=0)
avg_colour_round=np.round(avg_color, decimals=2)

print(avg_colour_round)

chlorophyll=(avg_colour_round[1]-(avg_colour_round[2]/2)-(avg_colour_round[0]/2))
print(chlorophyll, " mgr/cm.sq")

cv2.imshow("image", img)
cv2.imshow("image blurred", img_b)
cv2.imshow("mask", mask)
cv2.imshow("ROI",output)
#cv2.imshow("blur",sm)
cv2.waitKey(0)

