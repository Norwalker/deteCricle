import cv2 as cv
import os
import numpy as np
# 定义封闭曲线的轮廓层级结构
x = [[[-1, -1, 1,-1], [-1, -1, -1,0]]]
x = np.array(x)
def circle(j):
    src = cv.imread('O:/work/circleimg/1009/'+str(j))
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    # 一定要二值化后再进行反转
    _, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    gray = 255 - binary
    # 膨胀，将差不多连接的区域进行连接
    imgdIlate = cv.dilate(gray, kernel=np.ones((5, 5), np.uint8))
    # 寻找轮廓
    contours, hierarchy = cv.findContours(imgdIlate, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    # 轮廓数量为3 且符合x标准 且两个轮廓的坐标点数量的差值小于某个数量则为封闭曲线
    if len(contours)==2 and (hierarchy  == x).all() and abs(len(contours[1])-len(contours[0]))<55 :
        print(j+"         有缘")
    else:
        print(j+"无缘")
    cv.drawContours(imgdIlate,contours,-1,(0,255,0),2)
    cv.imshow(j, imgdIlate)
    cv.waitKey(0)
    cv.destroyAllWindows()

for i in os.listdir('O:/work/circleimg/1009/'):
    circle(i)