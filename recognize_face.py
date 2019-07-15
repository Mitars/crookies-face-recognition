import dlib


def recognize_face(frame, bounding_box):
    shape = sp(frame, bounding_box)
    face_descriptor = facerec.compute_face_descriptor(frame, shape, 100, 0.25)
    print(face_descriptor)
    face_chip = dlib.get_face_chip(frame, shape)
    face_descriptor_from_prealigned_image = facerec.compute_face_descriptor(face_chip)
    print(face_descriptor_from_prealigned_image)

# call the detector
sp = dlib.shape_predictor('data/shape_predictor_5_face_landmarks.dat')
facerec = dlib.face_recognition_model_v1('data/dlib_face_recognition_resnet_model_v1.dat')