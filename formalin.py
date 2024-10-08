# package
import cv2
import matplotlib.pyplot as plt
# load figure
# gray scale = 0
img = cv2.imread('Capture.png',0)
img_color = cv2.imread('tahu_borax.jpeg',1)
img_color2 = cv2.imread('tahu.jpeg',1)

# kernel:
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
# tophat and black hat
topHat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel) 
blackHat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

# using equation black hat and top hat
res = img + topHat - blackHat

# show image via opencv
# cv2.imshow('tahu borax',img_color)
cv2.imshow('lung',res)
# cv2.imshow('res',res)
# tinggal buat histogram : 

plt.hist(res.ravel(),256,[0,256])
# plt.hist(img_color.ravel(),256,[0,256])
# plt.hist(img_color2.ravel(),256,[0,256])

plt.show()
# closing
cv2.waitKey(0)
cv2.destroyAllWindows()