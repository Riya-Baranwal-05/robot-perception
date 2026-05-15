"""
This takes camera frame in realtime and predicts the
object class.
"""



from ultralytics import YOLO
import cv2

def camera_publisher():
    model = YOLO('best.pt')
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("Error: couldn't open camera")
        exit()

    while True:
        ret,frame = cam.read()

        if not ret:
            print("Error: Can't recieve frame.")
            break
        result = model(frame)

        for i in result:
            frame = i.plot()
            cv2.imshow('camera',frame)

        if cv2.waitKey(1)==ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()

      
if __name__ == "__main__":
    camera_publisher()