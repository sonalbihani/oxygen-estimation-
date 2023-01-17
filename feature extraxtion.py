import os
import cv2
import numpy as np
from matplotlib import pyplot as plt
#matplotlib inline

"""
ds_path = "Flavia leaves dataset"

test_img_path = ds_path + "\\2546.jpg"
test_img_path
"""
main_img = cv2.imread("leaf image.jpg")
img = cv2.cvtColor(main_img, cv2.COLOR_BGR2RGB)
plt.imshow(img)


gs = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
plt.imshow(gs,cmap='Greys_r')

gs.shape

blur = cv2.GaussianBlur(gs, (5,5),0)
plt.imshow(blur,cmap='Greys_r')

ret_otsu,im_bw_otsu = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
plt.imshow(im_bw_otsu,cmap='Greys_r')

kernel = np.ones((10,10),np.uint8)
closing = cv2.morphologyEx(im_bw_otsu, cv2.MORPH_CLOSE, kernel)

plt.imshow(closing,cmap='Greys_r')

_, contours, hierarchy = cv2.findContours(closing,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

len(contours)

cnt = contours[0]
len(cnt)

plottedContour = cv2.drawContours(gs,contours,-1,(0,255,0),2)
plt.imshow(plottedContour,cmap="Greys_r")

M = cv2.moments(cnt)
M
area = cv2.contourArea(cnt)
area

perimeter = cv2.arcLength(cnt,True)
perimeter


rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
contours_im = cv2.drawContours(closing,[box],0,(255,255,255),2)
plt.imshow(contours_im,cmap="Greys_r")

ellipse = cv2.fitEllipse(cnt)
im = cv2.ellipse(closing,ellipse,(255,255,255),2)
plt.imshow(closing,cmap="Greys_r")


x,y,w,h = cv2.boundingRect(cnt)
aspect_ratio = float(w)/h
aspect_ratio

rectangularity = w*h/area
rectangularity

circularity = ((perimeter)**2)/area
circularity

equi_diameter = np.sqrt(4*area/np.pi)
equi_diameter

(x,y),(MA,ma),angle = cv2.fitEllipse(cnt)

red_channel = img[:,:,0]
plt.imshow(red_channel,cmap="Greys_r")


green_channel = img[:,:,1]
plt.imshow(green_channel,cmap="Greys_r")

blue_channel = img[:,:,2]
plt.imshow(blue_channel,cmap="Greys_r")

blue_channel[blue_channel == 255] = 0
green_channel[green_channel == 255] = 0
red_channel[red_channel == 255] = 0

red_mean = np.mean(red_channel)
green_mean = np.mean(green_channel)
blue_mean = np.mean(blue_channel)

red_var = np.std(red_channel)

import mahotas as mt

textures = mt.features.haralick(gs)
ht_mean = textures.mean(axis=0)
ht_mean


print(ht_mean[1]) #contrast
print(ht_mean[2]) #correlation
print(ht_mean[4]) #inverse difference moments
print(ht_mean[8]) #entropy








