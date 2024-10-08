import cv2

cam = cv2.VideoCapture(0)
while True:
    _, frame = cam.read()
    frame = cv2.flip(frame,1)
    # gray scale 
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # kernel:
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
# tophat and black hat
    topHat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel) 
    blackHat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)

# using equation
    res = gray + topHat - blackHat

    # equalize = cv2.equalizeHist(frame)
    cv2.imshow("detection", frame)
    cv2.imshow("gray detection", gray)
    # cv2.imshow("equalize detection", equalize)
    cv2.imshow("res", res)
    
    if cv2.waitKey(1) and 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
