from __future__ import division
import cv2
import time
import datetime
from detect_face import detect_face

if __name__ == "__main__":
    logfile = open("log.csv", "w+")
    logfile.write('time, person, bounding box, camera\n')
    cap = cv2.VideoCapture(0)
    hasFrame, frame = cap.read()

    frame_count = 0
    time_delta = 0
    while True:
        hasFrame, frame = cap.read()
        if not hasFrame:
            break
        frame_count += 1

        t = time.time()
        now = datetime.datetime.now()
        bounding_boxes = detect_face(frame)
        time_delta += time.time() - t
        fpsCount = frame_count / time_delta

        label = "DLIB HoG ; ; FPS : {:.2f}".format(fpsCount)

        if len(bounding_boxes) > 0:
            for box in bounding_boxes:
                logfile.write(str(now) + ', ' + 'unknown' + ', ' + str(box) + ', ' + 'Front Camera 1' + '\n')
                if len(box):
                    cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 3, 3)

        cv2.putText(frame, label, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 0, 255), 3, cv2.LINE_AA)

        cv2.imshow("Face Detection Comparison", frame)

        if frame_count == 1:
            time_delta = 0

        k = cv2.waitKey(10)
        if k == 27:
            break
    cv2.destroyAllWindows()
    logfile.close()
