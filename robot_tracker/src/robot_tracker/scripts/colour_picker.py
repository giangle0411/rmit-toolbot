#!/usr/bin/env python

# Original script was sourced then modified from the script located at the following github url:
# https://github.com/socratesk/ComputerVision/blob/master/ColorPicker.py
#
# USAGE: You need to specify a filter and "only one" image source
# python ColorPicker.py --filter RGB --image /path/image.png
# or
# python ColorPicker.py --filter HSV --webcam

# This script is to be run separately from rosie. It is just to run in a python environment and is to be used to
# determine the hsv values desired for the filtering process in the "detect_vest.py" script.

import cv2
import numpy as np
import argparse
from operator import xor


def callback():
    pass


def setup_trackbars(range_filter):
    cv2.namedWindow("Trackbars", 0)

    for i in ["MIN", "MAX"]:
        v = 0 if i == "MIN" else 255
        for j in range_filter:
            cv2.createTrackbar("%s_%s" % (j, i), "Trackbars", v, 255, callback)


def get_arguments():
    ap = argparse.ArgumentParser()
    ap.add_argument('-f', '--filter', required=True,
                    help='Range filter. RGB or HSV')
    ap.add_argument('-i', '--image', required=False,
                    help='Path to the image')
    ap.add_argument('-w', '--webcam', required=False,
                    help='Use webcam', action='store_true')
    args = vars(ap.parse_args())

    if not xor(bool(args['image']), bool(args['webcam'])):
        ap.error("Please specify only one image source")

    if not args['filter'].upper() in ['RGB', 'HSV']:
        ap.error("Please specify a correct filter.")

    return args


def get_trackbar_values(range_filter):
    values = []
    for i in ["MIN", "MAX"]:
        for j in range_filter:
            v = cv2.getTrackbarPos("%s_%s" % (j, i), "Trackbars")
            values.append(v)

    return values


def main():
    args = get_arguments()
    range_filter = args['filter'].upper()

    if args['image']:
        image = cv2.imread(args['image'])

        if range_filter == 'RGB':
            frame_to_thresh = image.copy()
        else:
            frame_to_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    else:
        camera = cv2.VideoCapture(0)

    setup_trackbars(range_filter)

    while True:
        if args['webcam']:
            ret, image = camera.read()

            if not ret:
                break

            if range_filter == 'RGB':
                frame_to_thresh = image.copy()
            else:
                frame_to_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        v1_min, v2_min, v3_min, v1_max, v2_max, v3_max = get_trackbar_values(range_filter)
        mask = cv2.inRange(frame_to_thresh, (v1_min, v2_min, v3_min), (v1_max, v2_max, v3_max))
        kernel = np.ones((3, 18), np.float32)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        mask = cv2.filter2D(mask, -1, kernel)

        preview = cv2.bitwise_and(image, image, mask=mask)
        img_con = cv2.hconcat((image, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR), preview))
        cv2.namedWindow('out', cv2.WINDOW_NORMAL)
        cv2.imshow('out', img_con)

        k = cv2.waitKey(5) & 0xFF
        if k == 27 or k == ord('q'):
            break


if __name__ == '__main__':
    main()
