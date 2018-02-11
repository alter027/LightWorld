# pip install opencv-python
import numpy as np
import cv2
# 讀取圖檔
img = cv2.imread('image.jpg')
# 查看資料型態
type(img)
# 資料大小
img.shape()
# 以灰階的方式讀取圖檔
img_gray = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
# 顯示圖片
cv2.imshow('My Image', img)
# 按下任意鍵則關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()
# 關閉 'My Image' 視窗
cv2.destroyWindow('My Image')
# 讓視窗可以自由縮放大小
cv2.namedWindow('My Image', cv2.WINDOW_NORMAL)
cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 尋找黑白格
cv2.findChessboardCorners()
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, corners = cv2.findChessboardCorners(gray, (w,h),None)
matplotlib
scipy