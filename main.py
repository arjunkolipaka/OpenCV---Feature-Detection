import cv2
import numpy as np
import feature_detection as f_d

#Change the image directory to yours
img = cv2.imread("C:\\Users\\Arjun Kumar Kolipaka\\Downloads\\koala-3055832_1920.jpg", cv2.IMREAD_GRAYSCALE)

img1 = f_d.SIFT_IMG(img)
#img2 = f_d.SURF_IMG(img)
img3 = f_d.ORB_IMG(img)
img4 = f_d.BRIEF_IMG(img)
img5 = f_d.FAST_IMG(img)

cv2.imshow("Image",img5)
cv2.waitKey(0)
cv2.destroyAllWindows()