from FaceMeshModule import FaceMeshDetector
import cv2
import time

if __name__ == '__main__':
    cap = cv2.VideoCapture("./Path_to_video")
    pTime = 0
    detector = FaceMeshDetector()

    while True:
        success, img = cap.read()
        img, faces, landmarks = detector.FindFaceMesh(img)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f"FPS: {int(fps)}", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)
