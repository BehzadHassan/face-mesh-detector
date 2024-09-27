from FaceRecognitionModule import FaceMeshDetector
import cv2

if __name__ == '__main__':
    img = cv2.imread("./Path_to_image")
    FaceMesh = FaceMeshDetector()
    img_lm, face_lm, landmarks = FaceMesh.FindFaceMesh(img)
    cv2.imshow('Image', img_lm)
    cv2.waitKey(0)
