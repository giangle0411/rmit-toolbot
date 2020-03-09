#!/usr/bin/env

# The script is to be used for debugging purposes. It allows you to remotely view what Rosie see through the attached
# webcam, with any identified contours overlaid. Note: debug argument needs to be set to true when launching the
# "detect_vest.py" script.

import cv2

import numpy as np
import rospy
from sensor_msgs.msg import CompressedImage


def showvideo(winname, image_np):
    cv2.namedWindow(winname, cv2.WINDOW_NORMAL)
    cv2.imshow(winname, image_np)
    cv2.waitKey(2)


def callback(data):
    np_arr = np.fromstring(data.data, np.uint8)
    image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    showvideo("debug_detect_vest", image_np)


def shutdown_hook():
    cv2.destroyAllWindows()


def listener():
    rospy.init_node('debug_vid_detect_vest', anonymous=True)
    rospy.Subscriber("/debug_detect_vest/image_raw/compressed", CompressedImage, callback, queue_size=1)
    rospy.on_shutdown(shutdown_hook)

    rospy.spin()


if __name__ == '__main__':
    listener()
