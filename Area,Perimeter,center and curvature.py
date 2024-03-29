import numpy as np
import cv2

img = cv2.imread('detect_blob.png',1)

#Convert image in to gray sacle and thresold it'
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

thresh = cv2.adaptiveThreshold(gray,225,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

cv2.imshow("Binary",thresh)

#Apply contours command
#this command use to haver 3 outputs, in open Cv only has 2

contours , hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#Copy image not effect to original image
img2 =img.copy()

index = -1 # this mean we draw all counters
#thisckness is draw line
thickness = 4
#color of the line
color = (255,0,255)

#Now drow a counters
cv2.drawContours(img2,contours,index,color,thickness)
cv2.imshow("Counters",img2)

#Create empty array
#Format uint 8
#shape[0]- rows(width)
#shape[1]- columns(height)
objects = np.zeros([img.shape[0],img.shape[1],3],'uint8') # This is blank canvas

#Loop over our counters

for c in contours:
  cv2.drawContours(objects,[c],-1,color,-1)


#now leats get some information from that contours
  area = cv2.contourArea(c)
  perimeter = cv2.arcLength(c,True)

#Get the parameter
#M is matrix, taking momentom for searching center
  M =cv2.moments(c)
#m001(X center weight),m00(Total mass),m01-Y center weight
  cx = int(M['m10']/M['m00'])
  cy = int(M['m01']/M['m00'])
  cv2.circle(objects,(cx,cy),4,(0,0,255),-1)
  print(f"Area : {area}, perimiter :{perimeter}")

cv2.imshow("Counters", objects)

cv2.waitKey(0)
cv2.destroyAllWindows()
