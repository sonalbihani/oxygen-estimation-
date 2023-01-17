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
cambodia_2001=cv2.imread("cambodia 2001.jpg")
cambodia_2014=cv2.imread("cambodia 2014.jpg")

cambodia_2001=cv2.resize(cambodia_2001,(500,500),interpolation = cv2.INTER_AREA)
cambodia_2014=cv2.resize(cambodia_2014,(500,500),interpolation = cv2.INTER_AREA)

hsv_2001=cv2.cvtColor(cambodia_2001, cv2.COLOR_BGR2HSV)
hsv_2014=cv2.cvtColor(cambodia_2014, cv2.COLOR_BGR2HSV)

#define green range
#lower_green = np.array([36, 65, 75])
#upper_green = np.array([70, 255,255])
lower_green = np.array([36, 0, 0])
upper_green = np.array([85, 255,255])

#create binary mask image
mask_2001 = cv2.inRange(hsv_2001, lower_green, upper_green)
mask_2014 = cv2.inRange(hsv_2014, lower_green, upper_green)

#threshold masks
_,mask01= cv2.threshold(mask_2001,127,255,cv2.THRESH_BINARY)
_,mask14= cv2.threshold(mask_2014,127,255,cv2.THRESH_BINARY)

#analysis
an=np.zeros_like(mask01)

for i in range(500):
    for j in range(500):
        if(mask01[i,j]==255 and mask14[i,j]==255):
            an[i,j]=0
        if(mask01[i,j]==255 and mask14[i,j]==0):
            an[i,j]=255
        if(mask01[i,j]==0 and mask14[i,j]==255):
            an[i,j]=150
        if(mask01[i,j]==0 and mask14[i,j]==0):
            an[i,j]=0


an=np.array(an)

num=500*500;
count=0
for m in range(500):
    for n in range(500):
        if (mask01[m,n]==255):
            count=count+1
veg_01=np.round((count/num)*100, decimals=2)
print("original vegetation percentage:",veg_01," %")

count3=0
for m in range(500):
    for n in range(500):
        if (mask14[m,n]==255):
            count3=count3+1
            
veg_14=np.round((count3/num)*100, decimals=2)
print("2014 vegetation percentage:",veg_14," %")

total=175*175
print("total area is ",total," sq km")
area_v_01=total*(veg_01/100)
area_v_14=total*(veg_14/100)

print("Oxygen production (cu mm/year/sq km)")

oxg_01=(chlorophyll*9*365*15.652114*area_v_01)/1000000
oxg_14=(chlorophyll*9*365*15.652114*area_v_14)/1000000

x=[2001,2014]
y=[oxg_01,oxg_14]

plt.plot(x,y)


cv2.imshow("2001",mask01)
cv2.imshow("2014",mask14)
cv2.imshow("2001",cambodia_2001)
cv2.imshow("2014",cambodia_2014)
cv2.waitKey(0)
#cv2.imshow("2014",mask14)
cv2.imshow("2001-2014",an)
cv2.waitKey(0)
