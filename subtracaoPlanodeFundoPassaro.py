import cv2
import numpy as np


src = cv2.imread('bird.jpg',0);
th2 = cv2.adaptiveThreshold(src,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,15,5)
newImage = th2
newImage = cv2.medianBlur(newImage,5)
cv2.imshow("Final Image", newImage)
cv2.waitKey(0)
