#!/usr/bin/env python

# This script is used to define the movements of Rosie (or simulated robot) based on face data.
import rospy
from geometry_msgs.msg import Twist
from robot_tracker.msg import FaceData

cmd_vel = 'turtle1/cmd_vel'


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
    # Here the msg data is extracted from the msg published by the "face_data" topic located on roscore.
    frame_area = data.cam_height * data.cam_width
    frame_x_center = data.cam_width / 2
    object_area = data.area
    object_x_center = data.x_center
    coverage = object_area / frame_area * 100

    # Determines new rotation angle value.
    if data.rotation_angle > 30:
        new_rotation_angle = deg2rad(30)
    elif data.rotation_angle < -30:
        new_rotation_angle = deg2rad(-30)
    else:
        new_rotation_angle = deg2rad(data.rotation_angle)
    rotation_angle = new_rotation_angle

    # Determines new liner velocity value.
    liner_vel_max = 0.5
    new_vel = 0.0
    if (object_x_center > frame_x_center * 0.9) and (object_x_center < frame_x_center * 1.1):
        if coverage >= 50:
            new_vel = 0.0 * liner_vel_max
        elif (coverage >= 35) and (coverage < 50):
            new_vel = 0.5 * liner_vel_max
        elif (coverage >= 20) and (coverage < 35):
            new_vel = 1.0 * liner_vel_max
        else:
            new_vel = 0.0 * liner_vel_max
    current_vel = new_vel

    # Construct Twist msg with the velocity data to be published to roscore.
    msg_twist_out.linear.x = current_vel
    msg_twist_out.angular.z = rotation_angle
    log(object_area, frame_area, coverage, object_x_center, frame_x_center, current_vel, rotation_angle)


def timer_callback(data):
    pub_twist.publish(msg_twist_out)


def listener():
    global pub_twist
    pub_twist = rospy.Publisher(cmd_vel, Twist, queue_size=10)

    global msg_twist_out
    msg_twist_out = Twist()

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node.
    rospy.init_node('face_move_robot', anonymous=True)

    rospy.Subscriber('face_data', FaceData, callback)
    # Timer ensures that velocity data is sent only every tenth of a second or a rate of 10Hz.
    rospy.Timer(rospy.Duration(0.1), timer_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()
