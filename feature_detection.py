import cv2
import numpy as np

# !IMPORTANT: Change the directory to save your results for every img_func in the 'status' variable
def SIFT_IMG(img):
	sift = cv2.xfeatures2d.SIFT_create()
	kps = sift.detect(img, None)
	img = cv2.drawKeypoints(img, kps, None)
	status = cv2.imwrite("C:\\Users\\Arjun Kumar Kolipaka\\Desktop\\sift_img.jpg",img)

	return img

def SURF_IMG(img):
	#surf is patented. To use, please use the NON FREE licenced version
	surf = cv2.xfeatures2d.SURF_create()
	kps = surf.detect(img, None)
	img = cv2.drawKeypoints(img, kps, None)
	status = cv2.imwrite("C:\\Users\\Arjun Kumar Kolipaka\\Desktop\\surf_img.jpg",img)

	return img

def ORB_IMG(img):
	orb = cv2.ORB_create(nfeatures=20000)
	kps = orb.detect(img, None)
	img = cv2.drawKeypoints(img, kps, None)
	status = cv2.imwrite("C:\\Users\\Arjun Kumar Kolipaka\\Desktop\\orb_img.jpg",img)

	return img

def BRIEF_IMG(img):
	star = cv2.xfeatures2d.StarDetector_create()
	brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()
	kps = star.detect(img,None)
	kps, des = brief.compute(img, kps)
	img = cv2.drawKeypoints(img, kps, None)
	status = cv2.imwrite("C:\\Users\\Arjun Kumar Kolipaka\\Desktop\\brief_img.jpg",img)

	return img

def FAST_IMG(img):
	fast = cv2.FastFeatureDetector_create()
	#kps = fast.detect(img,None)
	fast.setNonmaxSuppression(1)
	kps = fast.detect(img,None)
	img = cv2.drawKeypoints(img, kps, None)
	status = cv2.imwrite("C:\\Users\\Arjun Kumar Kolipaka\\Desktop\\fast_img.jpg",img)

	return img
