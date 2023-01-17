# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:52:49 2019

@author: Abhimanyu
"""

import cv2
import numpy as np

img_1999=cv2.imread("amazon 1999.jpg")
img_2005=cv2.imread("amazon 2005.jpg")
img_2017=cv2.imread("amazon 2017.jpg")

img_1999=cv2.resize(img_1999,(260,110),interpolation = cv2.INTER_AREA)
img_2005=cv2.resize(img_2005,(260,110),interpolation = cv2.INTER_AREA)
img_2017=cv2.resize(img_2017,(260,110),interpolation = cv2.INTER_AREA)

hsv_1999=cv2.cvtColor(img_1999, cv2.COLOR_BGR2HSV)
hsv_2005=cv2.cvtColor(img_2005, cv2.COLOR_BGR2HSV)
hsv_2017=cv2.cvtColor(img_2017, cv2.COLOR_BGR2HSV)

lower_green = np.array([36, 65, 75])
upper_green = np.array([70, 255,255])

mask_1999 = cv2.inRange(hsv_1999, lower_green, upper_green)
mask_2005 = cv2.inRange(hsv_2005, lower_green, upper_green)
mask_2017 = cv2.inRange(hsv_2017, lower_green, upper_green)

cv2.imwrite("mask_1999.jpg",mask_1999)
cv2.imwrite("mask_2017.jpg",mask_2017)

m_1999=cv2.imread("mask_1999.jpg")
m_2017=cv2.imread("mask_2017.jpg")
ret,thresh1999 = cv2.threshold(m_1999,127,255,cv2.THRESH_BINARY)
ret2,thresh2000 = cv2.threshold(m_2017,127,255,cv2.THRESH_BINARY)

intersect_99_05 = cv2.bitwise_and(mask_1999,mask_2005)
intersect_99_17 = cv2.bitwise_and(m_1999,m_2017)
in_99_17 = cv2.bitwise_xor(m_1999,m_2017)


#cv2.imshow("op1", intersect_99_05)
#cv2.waitKey(0)
cv2.imshow("im",img_1999)
cv2.imshow("im2",img_2017)
cv2.imshow("mask_im1", mask_1999)
cv2.imshow("mask_im2", mask_2017)
cv2.imshow("and", intersect_99_17)
#cv2.imshow("xor", in_99_17)
#cv2.imshow("green",img_1999[:,:,1])
#cv2.imshow("green2",img_2017[:,:,1])
#ret,thresh1 = cv2.threshold(img_1999[:,:,1],127,255,cv2.THRESH_BINARY)
#cv2.imshow("green2",thresh1)
cv2.waitKey(0)

diff_99_05=cv2.subtract(mask_1999,mask_2005)
diff_99_17=cv2.add(mask_1999,mask_2017)

cv2.imshow("op", mask_1999)
cv2.imshow("op1", mask_2017)
#cv2.imshow("op1_diff", diff_99_05)
cv2.imshow("op_diff", diff_99_17)
cv2.waitKey(0)