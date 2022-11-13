# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 10:03:12 2022

@author: user
"""

import cv2
import matplotlib.pyplot as plt

image = cv2.imread('C:/Users/user/new/New folder/crab.jpeg')

imagex = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.hist(imagex.ravel(),8,[0,8]);
plt.show()