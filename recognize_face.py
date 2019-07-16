import os
import dlib
import glob

predictor_path = 'data/shape_predictor_5_face_landmarks.dat'
face_rec_model_path = 'data/dlib_face_recognition_resnet_model_v1.dat'
faces_folder_path = 'faces/'

detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(predictor_path)
facerec = dlib.face_recognition_model_v1(face_rec_model_path)

faces = []
names = []

for f in glob.glob(os.path.join(faces_folder_path, "*.jpg")):
    img = dlib.load_rgb_image(f)
    dets = detector(img, 1)

    for k, d in enumerate(dets):
        shape = sp(img, d)
        face_descriptor = facerec.compute_face_descriptor(img, shape)
        faces.append(face_descriptor)
        names.append(f)


def euclidean_dist(vector_x, vector_y):
    if len(vector_x) != len(vector_y):
        raise Exception('Vectors must be same dimensions')
    return sum((vector_x[dim] - vector_y[dim]) ** 2 for dim in range(len(vector_x)))


def compare_with_all(frame):
    height, width, channels = frame.shape
    new_shape = sp(frame, dlib.rectangle(0, 0, width, height))
    new_face = facerec.compute_face_descriptor(frame, new_shape)

    best_match_distance = 0.5
    name = 'Unknown'
    for i in range(len(faces)):
        distance = euclidean_dist(new_face, faces[i])
        if distance < best_match_distance:
            best_match_distance = distance
            name = names[i]

    confidence = (1 / (1 + best_match_distance));
    return name, confidence
