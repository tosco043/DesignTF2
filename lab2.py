import cv2
import time
cap = cv2.VideoCapture('cam_video.mp4')
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    ret, thresh = cv2.threshold(gray, 105, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh,
                                            cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        if x > gray.shape[1] // 2:
            cv2.circle(frame, (x + w // 2, y + h // 2), w // 2, (255, 0, 0), 2)
            print("BLUE")
        else:
            cv2.circle(frame, (x + w // 2, y + h // 2), w // 2, (0, 0, 255), 2)
            print("RED")
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(0.1)
cap.release()
cv2.destroyAllWindows()

