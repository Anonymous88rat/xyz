import matplotlib.pyplot as plt
import cv2
import numpy as np

img = cv2.imread('img1.jpg',0)

# calculate frequency of pixels in range 0-255
histr = cv2.calcHist([img],[0],None,[256],[0,256])
equ = cv2.equalizeHist(img)
histe = cv2.calcHist([equ],[0],None,[256],[0,256])
plt.plot(histr)
plt.plot(histe)
plt.show()
cv2.imshow("Compare", np.hstack((img, equ)))
cv2.waitKey(0)
cv2.destroyAllWindows()
