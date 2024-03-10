import numpy as np
import cv2

img = cv2.imread('sudoku.png',0)
cv2.imshow("Original", img)

#Doing basic thresholding

ret, thresh_basic = cv2.threshold(img,70,255,cv2.THRESH_BINARY)
cv2.imshow("Bisic Binary", thresh_basic)
# cv2.imshow("Bisic Binary", ret)

thres_adapt = cv2.adaptiveThreshold(img,225,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow("Adaptive Threshold", thres_adapt)
# inhere 255- maximum pixel value
#115 - adaptive thrsholding act over
# 1 - mean sustraction of the end result

cv2.waitKey(0)
cv2.destroyAllWindows()
