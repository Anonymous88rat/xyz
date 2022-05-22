import cv2
from skimage.util import random_noise

image = cv2.imread('img1.jpg')
#cv2.imshow('Original', image)
#cv2.waitKey(0)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray_image)

noise_img = random_noise(gray_image, mode='s&p')

# cv2.imshow("Noise",noise_img)
# cv2.waitKey(0)
# dst = cv2.medianBlur(noise_img,7)
dst = cv2.GaussianBlur(noise_img,(3,3),cv2.BORDER_DEFAULT) 
cv2.imshow("De-Noise", dst)

# enh_img = cv2.fastNlMeansDenoising(noise_img,None,3,7,21)
# cv2.imshow("Enhanced",enh_img)
cv2.waitKey(0)

cv2.destroyAllWindows()
