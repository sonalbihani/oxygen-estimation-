# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 02:43:13 2019

@author: Abhimanyu
"""

import cv2
import numpy as np
from skimage.measure import compare_ssim

img1=cv2.imread("mask_1999.jpg")
img2=cv2.imread("mask_2017.jpg")

cv2.imwrite("mask_1999.png",img1)
cv2.imwrite("mask_2017.png",img2)

img1=cv2.imread("mask_1999.png")
img2=cv2.imread("mask_2017.png")

test1=cv2.imread("drawing_1.png")
test2=cv2.imread("drawing_2.png")

_,img1 = cv2.threshold(img1,127,255,cv2.THRESH_BINARY)
_,img2 = cv2.threshold(img2,127,255,cv2.THRESH_BINARY)


hsv_1=cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
hsv_2=cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
lower_green = np.array([36, 65, 75])
upper_green = np.array([70, 255,255])

mask_1 = cv2.inRange(hsv_1, lower_green, upper_green)
mask_2 = cv2.inRange(hsv_2, lower_green, upper_green)


k1=cv2.bitwise_not(img1)
band=cv2.bitwise_and(img1,img2)
bor=cv2.bitwise_or(img1,img2)
#diff=cv2.bitwise_not(cv2.subtract(img1,img2))


(score, diff) = compare_ssim(img1, img2, full=True, multichannel=True)
#diff = (diff * 255).astype("uint8")

cv2.imshow("image 1",img1)
cv2.imshow("image 2",img2)
#cv2.imshow("and",band)
#cv2.imshow("or",bor)
cv2.imshow("diff",diff)
cv2.waitKey(0)

cv2.imshow("a",test1[:,:,0])
cv2.imshow("b",test1[:,:,1])
cv2.imshow("c",test1[:,:,2])
cv2.waitKey(0)

#img_grey=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)