# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 10:40:41 2022

@author: user
"""

from skimage.feature import hog
import matplotlib.pyplot as plt
import cv2 as cv
from pathlib import Path
#importing image file
img1 = cv.imread(cv.samples.findFile("crab-v1/images/crab2.jpg"))

#resizing image
img1 = cv.resize(img1, (128, 64)) 

#creating hog features 
fd, hog_image = hog(img1, orientations=9, pixels_per_cell=(8, 8), 
                    cells_per_block=(2, 2), visualize=True, multichannel=True)

plt.imshow(hog_image, cmap="gray")

#figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), sharex=True, sharey=True) 

ax1.imshow(img1, cmap=plt.cm.gray) 
ax1.set_title('Input image') 
 
ax2.imshow(hog_image, cmap="gray")
ax2.set_title('Histogram of Oriented Gradients')

plt.show()