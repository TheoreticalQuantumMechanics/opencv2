import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True :

# Take each frame
    _, frame = cap.read() # frame olarak goruntuyu aldık

# BGR ' yi HSV ye çevirdik
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # HSV nin içindeki renk aralıgını belirledik
    lower_yellow = np.array([20,0,0])
    upper_yellow = np.array([40,255,255])

    # Yukarıda belırledıgımız eşik değerlerini gray goruntunun içinde eşleştirdik.
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # bitwise and operatörü ile de ana goruntude yukarıda buldugumuz mask'i aldık.
    res = cv2.bitwise_and(frame,frame, mask= mask)
    img = cv2.medianBlur(res, 5)

    # cimg = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    cimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 5, 20,
                            param1=50, param2=30, minRadius=0, maxRadius=10)

    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # draw the outer circle
        cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

    cv2.imshow('detected circles', cimg)
    #ayarladıgımız 3 görüntüyü gösterdik

    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()