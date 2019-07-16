import cv2
import numpy as np
import os


def capture_logic(bounding_boxes, scores, frame, now):
    global bestScore
    global previous_detection_count
    global screenshot_timestamp
    global image_path

    filename = None

    new_session = previous_detection_count != len(bounding_boxes)

    if len(bounding_boxes) > 0:
        if new_session:
            screenshot_timestamp = str(now).replace(':', '_')
            filename = str(screenshot_timestamp) + '_newperson.jpg'
            cv2.imwrite(image_path + '/' + filename, frame)
            bestScore = np.mean(scores) if any(scores) else 0
        elif np.mean(scores) > bestScore:
            filename = str(screenshot_timestamp) + '_best_.jpg'
            print(str(bestScore) + ' -> ' + str(np.mean(scores)))
            cv2.imwrite(image_path + '/' + filename, frame)
            bestScore = np.mean(scores) if any(scores) else 0
    elif new_session:
        filename = screenshot_timestamp + '_empty.jpg'
        cv2.imwrite(image_path + '/' + filename, frame)
        bestScore = np.mean(scores) if any(scores) else 0

    previous_detection_count = len(bounding_boxes)

    return filename


def initialize_capture():
    if not os.path.exists(image_path):
        os.mkdir(image_path)


bestScore = 0
previous_detection_count = 0
image_path = 'camera_'
screenshot_timestamp = ''
