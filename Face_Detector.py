import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
video = cv2.VideoCapture(0)
address = "http://10.147.161.236:8080/video"
video.open(address)
while True:
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5)
    for x,y,w,h in face:
       img = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0), 3)
    cv2.imshow("gottach", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
       break
video.release()
cv2.destroyAllWindows

