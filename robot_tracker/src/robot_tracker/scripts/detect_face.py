#!/usr/bin/env python

# Following script is used to identify faces within within the image/ video frame.
import argparse
import cv2
import numpy as np

import rospy
from robot_tracker.msg import FaceData
from sensor_msgs.msg import CompressedImage


def image_callback(ros_data):
    # Section decodes compressed image stream from the "usb_cam" node.
    np_arr = np.fromstring(ros_data.data, np.uint8)
    image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    cam_height = image_np.shape[0]
    cam_width = image_np.shape[1]

    msg_face_data.cam_height = cam_height
    msg_face_data.cam_width = cam_width

    # Generate an array of faces.
    faces = face_cascade.detectMultiScale(image_np, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
                                          flags=cv2.CASCADE_SCALE_IMAGE)

    # Identify the largest face (closest) in the array.
    face = [[0, 0, 0, 0]]
    for temp_face in faces:
        if np.less(face[0][1], temp_face[1]):
            face = [temp_face]

    # Outline the identified face and display.
    for (x, y, w, h) in face:
        cv2.rectangle(image_np, (x, y), (x + w, y + h), (255, 0, 0), 2)
        distance_from_center = (x + w / 2) - cam_width/2
        distance_per_degree = 4
        rotation_angle = distance_from_center / distance_per_degree

        # Here we construct the msg to be published to roscore.
        msg_face_data.x_center = x + w/2
        msg_face_data.y_center = y + h/2
        msg_face_data.area = w * h
        msg_face_data.rotation_angle = rotation_angle
        pub_face_data.publish(msg_face_data)

        cv2.imshow('Video', image_np)
        cv2.waitKey(2)


if __name__ == '__main__':
    msg_face_data = FaceData()
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-hc", "--haarcascade", help="haarcascade file to be used", required=True)
        args = parser.parse_args(rospy.myargv()[1:])
        rospy.init_node('detect_face', anonymous=True)

        face_cascade = cv2.CascadeClassifier(args.haarcascade)
        pub_face_data = rospy.Publisher('face_data', FaceData, queue_size=1)
        sub = rospy.Subscriber("/usb_cam/image_raw/compressed", CompressedImage, image_callback, queue_size=1)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
