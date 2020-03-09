#!/usr/bin/env python

# This script is used to define the movements of Rosie (or simulated robot) based on vest data.
import argparse

import rospy
import numpy as np
from geometry_msgs.msg import Twist
from robot_tracker.msg import VestData

win_size = 10


def moving_average(x, n=win_size):
    ret = np.cumsum(x, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


def log(object_area, frame_area, coverage, object_x_center, frame_x_center, linear_velocity, rotation_angle):
    rospy.loginfo(rospy.get_name() + ":\n\t object_area = %s, frame_area = %s\n\t coverage = %s%%\n\t"
                                     " object_x_center = %s,\n\t\t frame_x_center -10%% = %s, frame_x_center +10%% = %s"
                                     "\n\t linear_velocity = %f, rotation_angle =  %f"
                  % (object_area, frame_area, coverage, object_x_center, frame_x_center * 0.9, frame_x_center * 1.1,
                     linear_velocity, rotation_angle))


def deg2rad(deg):
    deg2rad_ratio = 0.0174533
    return deg * deg2rad_ratio


def callback(data):
    global current_vel_window, rotation_angle_window
    # Here the msg data is extracted from the msg published by the "vest_data" topic located on roscore.
    frame_area = data.cam_height * data.cam_width
    frame_x_center = data.cam_width / 2
    object_area = data.area
    object_x_center = data.x_center
    coverage = object_area / frame_area * 100

    # Determines new rotation angle value to append to the "rotation_angle_window".
    if data.rotation_angle > 30:
        new_rotation_angle = deg2rad(30)
    elif data.rotation_angle < -30:
        new_rotation_angle = deg2rad(-30)
    else:
        new_rotation_angle = deg2rad(data.rotation_angle)

    # Determines new liner velocity value to append to the "current_vel_window".
    liner_vel_max = 0.5
    new_vel = 0.0
    if (object_x_center > frame_x_center * 0.9) and (object_x_center < frame_x_center * 1.1):
        if coverage >= 30:
            new_vel = 0.0 * liner_vel_max
        elif (coverage >= 20) and (coverage < 30):
            new_vel = 0.1 * liner_vel_max
        elif (coverage >= 10) and (coverage < 20):
            new_vel = 0.3 * liner_vel_max
        elif (coverage >= 5) and (coverage < 10):
            new_vel = 0.5 * liner_vel_max
        elif (coverage >= 2.5) and (coverage < 5):
            new_vel = 0.7 * liner_vel_max
        elif (coverage >= 1.25) and (coverage < 2.5):
            new_vel = 0.9 * liner_vel_max
        elif (coverage >= 0.635) and (coverage < 1.25):
            new_vel = 1.0 * liner_vel_max
        else:
            new_vel = 0.0 * liner_vel_max

    # This section sets the linear velocity and rotation angle to the moving average of all the window samples.
    current_vel_window = np.delete(current_vel_window, 0)
    current_vel_window = np.append(current_vel_window, new_vel)
    print("vel window: %s" % current_vel_window)
    current_vel = moving_average(current_vel_window)

    rotation_angle_window = np.delete(rotation_angle_window, 0)
    rotation_angle_window = np.append(rotation_angle_window, new_rotation_angle)
    print(" RA window: %s" % rotation_angle_window)
    rotation_angle = moving_average(rotation_angle_window)

    # Construct Twist msg with the velocity data to be published to roscore.
    msg_twist_out.linear.x = current_vel
    msg_twist_out.angular.z = rotation_angle
    log(object_area, frame_area, coverage, object_x_center, frame_x_center, current_vel, rotation_angle)


def timer_callback(data):
    pub_twist.publish(msg_twist_out)


def listener():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cmd_vel", help="define cmd_vel topic", required=False, default='/safebase/cmd_vel')
    args = parser.parse_args(rospy.myargv()[1:])

    cmd_vel = args.cmd_vel
    print("cmd_vel = %s" % cmd_vel)
    global pub_twist
    pub_twist = rospy.Publisher(cmd_vel, Twist, queue_size=10)

    global msg_twist_out
    msg_twist_out = Twist()

    global current_vel_window, rotation_angle_window

    current_vel_window = np.zeros(win_size, )
    rotation_angle_window = np.zeros(win_size, )

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node.
    rospy.init_node('vest_move_robot', anonymous=True)

    rospy.Subscriber('vest_data', VestData, callback)
    # Timer ensures that velocity data is sent only every tenth of a second or a rate of 10Hz.
    rospy.Timer(rospy.Duration(0.1), timer_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
