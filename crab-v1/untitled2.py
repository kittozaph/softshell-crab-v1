# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 10:42:21 2022

@author: user
"""
from skimage import exposure
from skimage import feature
import matplotlib.pyplot as plt
import cv2


img = cv2.imread(cv2.samples.findFile("C:/Users/user/new/New folder/crab.jpeg"))

img = cv2.resize(img, (128, 64))

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

(H, hogImage) = feature.hog(img, orientations=9, pixels_per_cell=(8, 8),
	cells_per_block=(2, 2), transform_sqrt=True, block_norm="L1",
	visualize=True)
hogImage = exposure.rescale_intensity(hogImage, out_range=(0, 255))
hogImage = hogImage.astype("uint8")

plt.imshow(hogImage, cmap="gray")