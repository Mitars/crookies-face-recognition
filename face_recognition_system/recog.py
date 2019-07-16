from __future__ import division
import cv2
import datetime
from face_recognition_system.detect_face import detect_face
from face_recognition_system import image_capture as cpt, fps_counter


def stream_entry(*args):
    print(args)
    logfile.write('\t'.join([str(item) for item in args]) + '\n')


if __name__ == '__main__':
    logfile = open('log.xls', 'w+')
    stream_entry('time', 'person', 'bounding box', 'detection_score', 'camera', 'screenshot name')
    cap = cv2.VideoCapture(0)
    cpt.initialize_capture()

    while True:
        hasFrame, frame = cap.read()
        input_key = cv2.waitKey(10)
        if input_key == 27 or not hasFrame:
            break

        frame_start = datetime.datetime.now()
        bounding_boxes, scores = detect_face(frame)

        screenshot_filename = cpt.capture_logic(bounding_boxes, scores, frame, frame_start)

        for i in range(len(bounding_boxes)):
            box = bounding_boxes[i]
            score = scores[i]

            #recognize_face(frame, box)

            cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 3, 3)
            cv2.putText(frame, str("%.2f" % score), (box[0], box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1, cv2.LINE_AA)

            stream_entry(frame_start, 'unknown', box, score, 'Front Camera 1', screenshot_filename)

        if not any(bounding_boxes):
            stream_entry(frame_start, None, None, None, 'Front Camera 1', screenshot_filename)

        fps_count = fps_counter.get_fps(datetime.datetime.now(), frame_start)
        label = 'DLIB HoG ; ; FPS : {:.2f}'.format(fps_count)
        cv2.putText(frame, label, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 0, 255), 3, cv2.LINE_AA)

        cv2.imshow("Face Detection Comparison", frame)

    cv2.destroyAllWindows()
    logfile.close()
