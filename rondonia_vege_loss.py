# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 17:29:54 2019

@author: Abhimanyu
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 16:59:52 2019

@author: Abhimanyu
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
ESTIMATE CHOROPHYLL
"""
img=cv2.imread("2.jpg")
img_b=cv2.blur(img,(3,3))
hsv=cv2.cvtColor(img_b, cv2.COLOR_BGR2HSV)
lower_green = np.array([36, 25, 25])
upper_green = np.array([70, 255,255])
mask = cv2.inRange(hsv, lower_green, upper_green)
output = cv2.bitwise_and(img_b,img_b,mask=mask)
avg_color_per_row = np.average(output, axis=0)
avg_color = np.average(avg_color_per_row, axis=0)
avg_colour_round=np.round(avg_color, decimals=2)
chlorophyll=(avg_colour_round[1]-(avg_colour_round[2]/2)-(avg_colour_round[0]/2))


#########################################

"""
ANALYSE VEGETATION LOSS
"""
r_2001=cv2.imread("rondonia 2001 1.jpg")
r_2005=cv2.imread("rondonia 2005 1.jpg")
r_2008=cv2.imread("rondonia 2008 1.jpg")
r_2012=cv2.imread("rondonia 2012 1.jpg")


r_2001=cv2.resize(r_2001,(500,500),interpolation = cv2.INTER_AREA)
r_2005=cv2.resize(r_2005,(500,500),interpolation = cv2.INTER_AREA)
r_2008=cv2.resize(r_2008,(500,500),interpolation = cv2.INTER_AREA)
r_2012=cv2.resize(r_2012,(500,500),interpolation = cv2.INTER_AREA)


hsv_2001=cv2.cvtColor(r_2001, cv2.COLOR_BGR2HSV)
hsv_2005=cv2.cvtColor(r_2005, cv2.COLOR_BGR2HSV)
hsv_2008=cv2.cvtColor(r_2008, cv2.COLOR_BGR2HSV)
hsv_2012=cv2.cvtColor(r_2012, cv2.COLOR_BGR2HSV)

#define green range
#lower_green = np.array([36, 65, 75])
#upper_green = np.array([70, 255,255])
lower_green = np.array([36, 0, 0])
upper_green = np.array([85, 255,255])

#create binary mask image
mask_2001 = cv2.inRange(hsv_2001, lower_green, upper_green)
mask_2005 = cv2.inRange(hsv_2005, lower_green, upper_green)
mask_2008 = cv2.inRange(hsv_2008, lower_green, upper_green)
mask_2012 = cv2.inRange(hsv_2012, lower_green, upper_green)

#threshold masks
_,mask01= cv2.threshold(mask_2001,127,255,cv2.THRESH_BINARY)
_,mask05= cv2.threshold(mask_2005,127,255,cv2.THRESH_BINARY)
_,mask08= cv2.threshold(mask_2008,127,255,cv2.THRESH_BINARY)
_,mask12= cv2.threshold(mask_2012,127,255,cv2.THRESH_BINARY)


#analysis
an=np.zeros_like(mask01)
for i in range(500):
    for j in range(500):
        if(mask01[i,j]==255 and mask05[i,j]==255):
            an[i,j]=0
        if(mask01[i,j]==255 and mask05[i,j]==0):
            an[i,j]=255
        if(mask01[i,j]==0 and mask05[i,j]==255):
            an[i,j]=150
        if(mask01[i,j]==0 and mask05[i,j]==0):
            an[i,j]=0
an=np.array(an)

an2=np.zeros_like(mask08)
for i in range(500):
    for j in range(500):
        if(mask01[i,j]==255 and mask08[i,j]==255):
            an2[i,j]=0
        if(mask01[i,j]==255 and mask08[i,j]==0):
            an2[i,j]=255
        if(mask01[i,j]==0 and mask08[i,j]==255):
            an2[i,j]=150
        if(mask01[i,j]==0 and mask08[i,j]==0):
            an2[i,j]=0
an2=np.array(an2)

an3=np.zeros_like(mask12)
for i in range(500):
    for j in range(500):
        if(mask01[i,j]==255 and mask12[i,j]==255):
            an3[i,j]=0
        if(mask01[i,j]==255 and mask12[i,j]==0):
            an3[i,j]=255
        if(mask01[i,j]==0 and mask12[i,j]==255):
            an3[i,j]=150
        if(mask01[i,j]==0 and mask12[i,j]==0):
            an3[i,j]=0
an3=np.array(an3)


num=500*500;
#vegetation in 2001
count=0
for m in range(500):
    for n in range(500):
        if (mask01[m,n]==255):
            count=count+1
veg_01=np.round((count/num)*100, decimals=2)
print("original vegetation percentage:",veg_01," %")

#vegetation in 2005
count2=0
for m in range(500):
    for n in range(500):
        if (mask05[m,n]==255):
            count2=count2+1
veg_05=np.round((count2/num)*100, decimals=2)
print("2005 vegetation percentage:",veg_05," %")

#vegetation in 2010
count3=0
for m in range(500):
    for n in range(500):
        if (mask08[m,n]==255):
            count3=count3+1
            
veg_08=np.round((count3/num)*100, decimals=2)
print("2008 vegetation percentage:",veg_08," %")

#vegetation in 2017
count4=0
for m in range(500):
    for n in range(500):
        if (mask12[m,n]==255):
            count4=count4+1
            
veg_12=np.round((count4/num)*100, decimals=2)
print("2012 vegetation percentage:",veg_12," %")

total=175*175
print("total area is ",total," sq km")
area_v_01=total*(veg_01/100)
area_v_05=total*(veg_05/100)
area_v_08=total*(veg_08/100)
area_v_12=total*(veg_12/100)

print("Oxygen production (cu mm/year/sq km)")
oxg_01=(chlorophyll*9*365*15.652114*area_v_01)/1000000
oxg_05=(chlorophyll*9*365*15.652114*area_v_05)/1000000
oxg_08=(chlorophyll*9*365*15.652114*area_v_08)/1000000
oxg_12=(chlorophyll*9*365*15.652114*area_v_12)/1000000


x=[2001,2005,2008,2012]
y=[oxg_01,oxg_05,oxg_08,oxg_12]

plt.plot(x,y)
"""
cv2.imshow("2001",mask01)
cv2.imshow("2005",mask05)
cv2.imshow("2008",mask08)
cv2.imshow("2012",mask12)
cv2.waitKey(0)
cv2.imshow("2001-2005",an)
cv2.imshow("2001-2008",an2)
cv2.imshow("2001-2012",an3)
#cv2.imshow("2014",mask14)
#cv2.imshow("1999-2005",an)
cv2.waitKey(0)
"""