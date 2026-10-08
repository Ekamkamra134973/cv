import cv2
import mediapipe as mp
import time
cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
ptime=0
ctime=0


while True:
    success, img = cap.read()
    if not success:
        print("Could not read from camera")
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                img,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
            )
    ctime= time.time()
    fps= 1/(ctime-ptime)
    ptime= ctime
    cv2.putText(img,str(int(fps)),(10,60),cv2.FONT_HERSHEY_COMPLEX,5,(0,255,0),3,)
    cv2.imshow("Hand tracking", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
