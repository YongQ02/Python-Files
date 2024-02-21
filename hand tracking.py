import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
MPHands = mp.solutions.hands
hands = MPHands.Hands(min_detection_confidence=0.01)
MPDraw = mp.solutions.drawing_utils
HandsLandmarkStyle = MPDraw.DrawingSpec(color=(255, 0, 0), thickness=10)
HandsConnectionStyle = MPDraw.DrawingSpec(color=(0, 255, 0), thickness=20)
PreviousTime = 0
CurrentTime = 0

while True:
    ret, img = cap.read()
    if ret:
        RGBImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(RGBImg)
        imgHeight = img.shape[0]
        imgWidth = img.shape[1]

        print(result.multi_hand_landmarks)
        if result.multi_hand_landmarks:
            for handLM in result.multi_hand_landmarks:
                MPDraw.draw_landmarks(img, handLM, MPHands.HAND_CONNECTIONS, HandsLandmarkStyle, HandsConnectionStyle)
                for i, lm in enumerate(handLM.landmark):
                    xPos = int(lm.x * imgWidth)
                    yPos = int(lm.y * imgHeight)
                    cv2.putText(img, str(i), (xPos-25, yPos+5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 2)
                    if i == 12:
                        cv2.circle(img, (xPos, yPos), 20, (178, 3, 174), cv2.FILLED)
                    print(i, xPos, yPos)

        CurrentTime = time.time()
        fps = 1/(CurrentTime-PreviousTime)
        PreviousTime = CurrentTime
        cv2.putText(img, f"FPS: {int(fps)}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)

        cv2.imshow('Cam', img)

    if cv2.waitKey(1) == ord('e'):
        break