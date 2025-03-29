import cv2
import numpy as np

def biggestContour(contours):
    biggest = np.array([])
    max_area = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 5000:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            if len(approx) == 4 and area > max_area:
                biggest = approx
                max_area = area
    return biggest


def reorder(points):
    points = points.reshape((4, 2))
    new_points = np.zeros((4, 1, 2), dtype=np.int32)
    add = points.sum(1)
    new_points[0] = points[np.argmin(add)]      # top-left
    new_points[3] = points[np.argmax(add)]      # bottom-right
    diff = np.diff(points, axis=1)
    new_points[1] = points[np.argmin(diff)]     # top-right
    new_points[2] = points[np.argmax(diff)]     # bottom-left
    return new_points

def warpImg(img, points, width, height):
    reordered = reorder(points)
    pts1 = np.float32(reordered)
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (width, height))
    return imgOutput
