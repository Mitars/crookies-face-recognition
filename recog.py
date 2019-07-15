from __future__ import division
import cv2
import time
import datetime
from detect_face import detect_face

if __name__ == "__main__":
    logfile = open("log.csv", "w+")
    logfile.write('time, person, bounding box, detection_score, camera\n')
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
        bounding_boxes, scores = detect_face(frame) # add True at the end to get scores
        time_delta += time.time() - t
        fpsCount = frame_count / time_delta

        label = "DLIB HoG ; ; FPS : {:.2f}".format(fpsCount)

        for i in range(len(bounding_boxes)):
            box = bounding_boxes[i]
            if scores:
                score = scores[i]
            else:
                score = 0
            logfile.write(str(now) + ', ' + 'unknown' + ', ' + str(box) + ', ' + str(score) + ', ' + 'Front Camera 1' + '\n')
            cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 3, 3)
            if score > 0:
                cv2.putText(frame, str("%.2f" % score), (box[0], box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1, cv2.LINE_AA)

        cv2.putText(frame, label, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 0, 255), 3, cv2.LINE_AA)

        cv2.imshow("Face Detection Comparison", frame)

        if frame_count == 1:
            time_delta = 0

        k = cv2.waitKey(10)
        if k == 27:
            break
    cv2.destroyAllWindows()
    logfile.close()
