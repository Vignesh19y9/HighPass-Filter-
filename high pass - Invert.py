
import cv2
import numpy
img = cv2.imread('input.jpg')

img1=~img
blur = cv2.GaussianBlur(img1,(31,31),0)
filtered = img1 - blur
filtered = filtered + 127*numpy.ones(filtered.shape, numpy.uint8)

cv2.imshow("output", filtered)
cv2.waitKey(0)

