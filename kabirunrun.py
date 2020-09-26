import numpy as np
import cv2
from matplotlib import pyplot as plt



img = cv2.imread('/Users/tomixrm/Desktop/カビ　画像/iPad1.png')
cv2.imshow("general", img)
print("--------------------start--------------------")

# にちか
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 63, 255, cv2.THRESH_BINARY)
# calcArea(thresh)
cv2.imshow('thresh', thresh)

# threshold1 = 0
# threshold2 = 360
# edge_img = cv2.Canny(img, threshold1, threshold2)
# cv2.imshow('canny', edge_img)
# print(edge_img.type)


# 輪郭を検出。
contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


length = len(hierarchy[0])#検出した輪郭の数を出す
print("len:"+str(length))

baseArea = -1#シャーレの面積
mildewArea = -1#カビの面積
mildewNonArea = -1#シャーレのうち、カビが生えてない面積

contimg = img

for i in range(0,length):
        print("hierarchy"+str(i)+str(hierarchy[0][i]))
        if hierarchy[0][i][3] == 0 and hierarchy[0][i][0] == -1 :
                contimg = cv2.drawContours(img, contours, i, (180, 100, 240), 2)
                # print(i)
                # print("contours")
                cnt = contours[i]
                # print(cnt)
                baseArea = cv2.contourArea(cnt)
                # print("area:"+str(baseArea))
        elif hierarchy[0][i][3] != 0 and hierarchy[0][i][3] != -1 :
                contimg = cv2.drawContours(img, contours, i, (200, 180, 80), 2)
                # print(i)
                # print("contours2")
                cnt = contours[i]
                # print(cnt)
                area = cv2.contourArea(cnt)
                # print("area2:"+str(area))
                mildewArea += area

mildewNonArea = baseArea - mildewArea#カビの生えてない面積の計算
print("--------------------result--------------------")
RatioMildew = round((mildewArea/baseArea)*100, 3)  # [%]
RatioNonMildew = round((mildewNonArea/baseArea)*100, 3)  # [%]

print("Mildew Area [%] : ", RatioMildew)
print("NonMildew Area [%] : ", RatioNonMildew)
# height, width = contimg.shape
str1 = "Mildew"+str(RatioMildew)+"%"
str2 = "None"+str(RatioNonMildew)+"%"
contimg = cv2.rectangle(contimg,(0,0),(150,50),(255,255,255),cv2.FILLED)
cv2.putText(contimg, str1, (10,20), cv2.FONT_HERSHEY_PLAIN,1.2, (180, 180, 0), 1, cv2.LINE_AA)
cv2.putText(contimg, str2, (10, 40), cv2.FONT_HERSHEY_PLAIN,1.2, (180, 180, 0), 1, cv2.LINE_AA)
cv2.imshow('final', contimg)



k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):  # wait for 's' key to save and exit
    cv2.imwrite('Mildew.png', img)
    cv2.destroyAllWindows()
