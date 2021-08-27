#暂未添加导出文件语句

import cv2

img = cv2.imread(r"D:\A_V_Photo\feifeisleep.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")    #如果有需要，改成绝对路径

faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors = 5)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("sheep", img)
