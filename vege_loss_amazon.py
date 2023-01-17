# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 11:52:55 2019

@author: Abhimanyu
"""

import cv2
import numpy as np

#read images
a99=cv2.imread("amazon 1999.jpg")
a05=cv2.imread("amazon 2005.jpg")
a17=cv2.imread("amazon 2017.jpg")

#resize images
a99=cv2.resize(a99,(260,110),interpolation = cv2.INTER_AREA)
a05=cv2.resize(a05,(260,110),interpolation = cv2.INTER_AREA)
a17=cv2.resize(a17,(260,110),interpolation = cv2.INTER_AREA)

#convert to hsv
hsv_1999=cv2.cvtColor(a99, cv2.COLOR_BGR2HSV)
hsv_2005=cv2.cvtColor(a05, cv2.COLOR_BGR2HSV)
hsv_2017=cv2.cvtColor(a17, cv2.COLOR_BGR2HSV)

#define green range
lower_green = np.array([36, 65, 75])
upper_green = np.array([70, 255,255])

#create binary mask image
mask_1999 = cv2.inRange(hsv_1999, lower_green, upper_green)
mask_2005 = cv2.inRange(hsv_2005, lower_green, upper_green)
mask_2017 = cv2.inRange(hsv_2017, lower_green, upper_green)

#threshold masks
_,mask99= cv2.threshold(mask_1999,127,255,cv2.THRESH_BINARY)
_,mask05= cv2.threshold(mask_2005,127,255,cv2.THRESH_BINARY)
_,mask17= cv2.threshold(mask_2017,127,255,cv2.THRESH_BINARY)

#analysis
an=np.zeros_like(mask99)
an2=np.zeros_like(mask99)
for i in range(110):
    for j in range(260):
        if(mask99[i,j]==255 and mask05[i,j]==255):
            an[i,j]=0
        if(mask99[i,j]==255 and mask05[i,j]==0):
            an[i,j]=255
        if(mask99[i,j]==0 and mask05[i,j]==255):
            an[i,j]=150
        if(mask99[i,j]==0 and mask05[i,j]==0):
            an[i,j]=0

an=np.array(an)

for i in range(110):
    for j in range(260):
        if(mask99[i,j]==255 and mask17[i,j]==255):
            an2[i,j]=0
        if(mask99[i,j]==255 and mask17[i,j]==0):
            an2[i,j]=255
        if(mask99[i,j]==0 and mask17[i,j]==255):
            an2[i,j]=150
        if(mask99[i,j]==0 and mask17[i,j]==0):
            an2[i,j]=0


an2=np.array(an2)

num=260*110
count=0
for m in range(110):
    for n in range(260):
        if (mask99[m,n]==255):
            count=count+1
print("original vegetation percentage:",(count/num)*100," %")

count2=0
for m in range(110):
    for n in range(260):
        if (mask05[m,n]==255):
            count2=count2+1
print("2005 vegetation percentage:",(count2/num)*100," %")

count3=0
for m in range(110):
    for n in range(260):
        if (mask17[m,n]==255):
            count3=count3+1
print("2017 vegetation percentage:",(count3/num)*100," %")

print("black area: no change\ngrey area: new areas of vegetation in new year\nwhite area: loss of vegetation")
cv2.imshow("1999",a99)
cv2.imshow("2005",mask05)
cv2.imshow("2017",mask17)
#cv2.imshow("1999-2005",an)
#cv2.imshow("1999-2017",an2)
cv2.waitKey(0)  
        
        
        
        
        
        
        
        
        
        
        
