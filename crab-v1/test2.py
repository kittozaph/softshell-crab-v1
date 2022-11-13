# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 10:02:19 2022

@author: user
"""

from skimage.feature import hog
import matplotlib.pyplot as plt
import cv2

img1 = cv2.imread(cv2.samples.findFile("C:/Users/user/new/New folder/crab.jpeg"))

img1 = cv2.resize(img1, (128, 64)) 

g = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) 

#creating hog features 
fd, hog_image = hog(g, orientations=9, pixels_per_cell=(8, 8), 
                    cells_per_block=(2, 2), visualize=True, multichannel=True)

plt.axis("on")
plt.imshow(hog_image, cmap="gray")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), sharex=True, sharey=True) 

ax1.imshow(img1, cmap=plt.cm.gray) 
ax1.set_title('Input image') 
 
ax2.imshow(hog_image, cmap="gray")
ax2.set_title('Histogram of Oriented Gradients')

plt.hist(img1(), bins=8, range=(0,255))
plt.show()