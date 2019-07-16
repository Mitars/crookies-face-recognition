import cv2
import dlib


def detect(frame):
    in_height = 300
    in_width = 0

    frame_height = frame.shape[0]
    frame_width = frame.shape[1]
    if not in_width:
        in_width = int((frame_width / frame_height) * in_height)

    scale_height = frame_height / in_height
    scale_width = frame_width / in_width

    frame_small = cv2.resize(frame, (in_width, in_height))

    frame_small = cv2.cvtColor(frame_small, cv2.COLOR_BGR2RGB)

    face_rects, scores, idx = hogFaceDetector.run(frame_small, 0, 0)

    bounding_boxes = []
    for faceRect in face_rects:
        cv_rect = [int(faceRect.left()*scale_width), int(faceRect.top()*scale_height),
                   int(faceRect.right()*scale_width), int(faceRect.bottom()*scale_height)]
        bounding_boxes.append(cv_rect)
    return bounding_boxes, scores


# call the detector
hogFaceDetector = dlib.get_frontal_face_detector()
