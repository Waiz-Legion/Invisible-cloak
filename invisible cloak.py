import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
time.sleep(3)
background = 0
for i in range(30):
    ret, background = cap.read()

while cap.isOpened():
    ret, img = cap.read()

    img = np.flip(img, axis=1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    value = (35, 35)

    blurred = cv2.GaussianBlur(hsv, value, 0)

    l_red = np.array([0, 120, 70])
    u_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, l_red, u_red)

    l_red = np.array([170, 120, 70])
    u_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, l_red, u_red)

    mask = mask1 + mask2
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))

    img[np.where(mask == 255)] = background[np.where(mask == 255)]
    cv2.imshow('Display', img)
    k = cv2.waitKey(10)
    if k == 27:
        break

