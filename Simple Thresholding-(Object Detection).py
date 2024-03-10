import numpy as np
import cv2

bw = cv2.imread("detect_blob.png",0)

cv2.imshow("Blck and white",bw)
height, width = bw.shape[0:2]

binary = np.zeros([height,width,1],'uint8') # 1 mean one channel binary image

thresh = 85

for row in range(0,height):
    for col in range(0,width):
        if bw[row][col]> thresh:
            binary[row][col] = 255

cv2.imshow("Slow Binary", binary)

ret , BWthresh = cv2.threshold(bw,thresh,255,cv2.THRESH_BINARY)
cv2.imshow("CV Thershold",BWthresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
