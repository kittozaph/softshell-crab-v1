import cv2
  
image = cv2.imread('~/images/crab.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#resizing image
img = cv2.resize(gray, (128, 64)) 

cv2.imshow('Original image',image)
cv2.imshow('Gray image', img)
  
cv2.waitKey(0)
cv2.destroyAllWindows()