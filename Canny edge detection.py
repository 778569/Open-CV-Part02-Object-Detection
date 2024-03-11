import numpy as np
import cv2

img = cv2.imread("tomatoes.jpg",1)

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
res, thresh = cv2.threshold(hsv[:,:,0],25,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Thresh", thresh)

edges = cv2.Canny(img,100,200, apertureSize=3)
cv2.imshow("Canny", edges)

edges_inv = 225- edges
#put errotion filter - eges bit thicker

kernal = np. ones((3,3),'uint8')
erode = cv2.erode(edges_inv, kernal, iterations=1)

#thrsold and errotion image together
canny_thresh = cv2.bitwise_and(erode, thresh)
cv2.imshow("Canny Thresh", canny_thresh)

#use contours in the image
contours, hierarcy = cv2.findContours( canny_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

objects = img.copy()
for c in contours:
	area = cv2.contourArea(c)
	if area < 300:
		# This contour is around something too small for our interest
		continue
	print("Area: ", area)
	cv2.drawContours(objects, [c], -1, (255, 255, 255), 1)
	M = cv2.moments(c)
	cx = int(M['m10'] / M['m00'])
	cy = int(M['m01'] / M['m00'])
	cv2.circle(objects, (cx, cy), 4, (255, 255, 0), -1)

cv2.imshow("Final draw-over", objects)

cv2.waitKeyEx()
cv2.destroyAllWindows()
