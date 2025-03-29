import cv2
import numpy as np

pathImage = "zd1.jpg"
#heightImg = 1000
#widthImg = 562
points = []

def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points) < 4:
            points.append([x, y])
            print(f"Kliknięto punkt: {x}, {y}")

if __name__ == "__main__":
    img = cv2.imread(pathImage)
    heightImg, widthImg, channel = img.shape

    x = 1000*widthImg/heightImg

    heightImg = 1000
    widthImg = int(x)

    img = cv2.resize(img, (widthImg, heightImg))
    imgOriginal = img.copy()

    cv2.namedWindow("Wybierz 4 punkty")
    cv2.setMouseCallback("Wybierz 4 punkty", mousePoints)

    print(points)

    while True:
        for x in range(0, len(points)):
            cv2.circle(img, (points[x][0], points[x][1]), 5, (0, 255, 0), cv2.FILLED)

        cv2.imshow("Wybierz 4 punkty", img)
        key = cv2.waitKey(1)

        if key == ord('q'):
            break

        if len(points) == 4:
            pts1 = np.float32(points)
            pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
            matrix = cv2.getPerspectiveTransform(pts1, pts2)
            imgOutput = cv2.warpPerspective(imgOriginal, matrix, (widthImg, heightImg))
            cv2.imwrite("przetworzony.png", imgOutput)
            print("Zapisano do przetworzony.png")
            cv2.imshow("Skan", imgOutput)
            cv2.waitKey(0)
            break

    cv2.destroyAllWindows()
