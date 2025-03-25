import cv2
import numpy as np
import utlis

pathImage = "zd3.jpg"


heightImg = 640
widthImg = 480

if __name__ == "__main__":
    
    img = cv2.imread(pathImage)
    img = cv2.resize(img, (widthImg, heightImg))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img = cv2.GaussianBlur(img, (5, 5), 1)
    img = cv2.Canny(img, 100, 200)  # ustalone progi (można dostroić)

    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    biggest = utlis.biggestContour(contours)

    if biggest.size != 0:
        img = cv2.imread(pathImage)
        img = cv2.resize(img, (widthImg, heightImg))
        img = utlis.warpImg(img, biggest, widthImg, heightImg)
    else:
        img = np.zeros((heightImg, widthImg, 3), np.uint8)  # pusta grafika, jeśli brak konturu

    cv2.imwrite("przetworzony.jpg", img)
    
    # Podgląd
    #cv2.imshow("Kontury", imgContour)
    #cv2.imshow("Canny", imgCanny)
    
    