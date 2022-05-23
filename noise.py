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

------------------------------------------------------------------------------------------------------------------
import numpy as np
import random
import cv2
import math

def salt_and_pepper(image,prob):
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

def calPSNRval(image, blur):
    mean_squared_error = np.mean((image - blur)**2)
    return 20 * math.log10(255/math.sqrt(mean_squared_error))
    
    
image = cv2.imread('lenna_grayscale.png',0) 
noise_img = salt_and_pepper(image,0.05)

gaus_blur = cv2.GaussianBlur(noise_img,(5,5),0)
avg_blur = cv2.blur(noise_img,(5,5))
med_blur = cv2.medianBlur(noise_img,5)

cv2.imshow("lenna", image)
cv2.waitKey(0)

cv2.imshow("lenna", noise_img)
cv2.waitKey(0)

cv2.imshow("lenna", gaus_blur)
cv2.waitKey(0)

cv2.imshow("lenna", med_blur)
cv2.waitKey(0)

cv2.imshow("lenna", avg_blur)
cv2.waitKey(0)

cv2.destroyAllWindows()


print(calPSNRval(image, gaus_blur))
print(calPSNRval(image, med_blur))
print(calPSNRval(image, avg_blur))




