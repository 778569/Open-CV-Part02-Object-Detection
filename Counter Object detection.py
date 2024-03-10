import numpy as np
import cv2

img = cv2.imread('detect_blob.png',1)

#Convert image in to gray sacle and thresold it'
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

thresh = cv2.adaptiveThreshold(gray,225,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

cv2.imshow("Binary",thresh)

#Apply contours command
#this command use to haver 3 outputs, in open Cv only has 2

countours , hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Copy image not effect to original image
img2 =img.copy()

index = -1 # this mean we draw all counters
#thisckness is draw line
thickness = 4
#color of the line
color = (255,0,255)

#Now drow a counters
cv2.drawContours(img2,countours,index,color,thickness)
cv2.imshow("Counters",img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
