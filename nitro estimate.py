import cv2
import numpy as np

img=cv2.imread("leaf image.jpg")
hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_green = np.array([36, 25, 25])
upper_green = np.array([70, 255,255])


mask = cv2.inRange(hsv, lower_green, upper_green)

output = cv2.bitwise_and(img, img, mask = mask)

avg_color_per_row = np.average(output, axis=0)
avg_color = np.average(avg_color_per_row, axis=0)
avg_colour_round=np.round(avg_color, decimals=2)
#kernel = np.ones((3,3),np.float32)/9

chlorophyll=(avg_colour_round[1]-(avg_colour_round[2]/2)-(avg_colour_round[0]/2))
print(chlorophyll, " mgr/cm.sq")

# cv2.imshow("images", output)
# cv2.imshow("m", mask)
# cv2.imshow("or",img)

# cv2.waitKey(0)
array_255 = np.array([255.0,255.0,255.0])
avg_nitro = np.divide(avg_colour_round,array_255)
min_nitro = avg_nitro.min()
max_nitro = avg_nitro.max()
if(max_nitro == avg_nitro[2]):
    hue = ((avg_nitro[1]-avg_nitro[0])/(max_nitro-min_nitro))*60   
elif(max_nitro == avg_nitro[1]):
    hue = (((avg_nitro[0]-avg_nitro[2])/(max_nitro-min_nitro))+2)*60    
elif(max_nitro == avg_nitro[0]):
    hue = (((avg_nitro[2]-avg_nitro[1])/(max_nitro-min_nitro))+2)*60
sat = (max_nitro-min_nitro)/max_nitro
bright = max_nitro
nitro = (((hue-60)/60)+(1-sat)+(1-bright))/3
print(nitro," mgr/cm.sq")


