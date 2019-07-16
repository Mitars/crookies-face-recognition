from __future__ import division
import cv2
import datetime
from detect_face import detect_face
from recognize_face import recognize_face
import image_capture as cpt
import fps_counter


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

            height, width, channels = frame.shape
            x = box[0] if box[0] >= 0 else 0
            x2 = box[2] if box[2] <= width else width
            y = box[1] if box[1] >= 0 else 0
            y2 = box[3] if box[3] <= height else height

            crop_img = frame[y:y2, x:x2]
            cv2.imshow("Face off", crop_img)

            frame_height = crop_img.shape[0]
            frame_width = crop_img.shape[1]
            in_width = int((frame_width / frame_height) * 100)
            scale_height = frame_height / 100
            scale_width = frame_width / in_width
            frame_small = cv2.resize(crop_img, (in_width, 100))

            if counter % 30 == 0:
                face, confidence = recognize_face.compare_with_all(frame_small)

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
