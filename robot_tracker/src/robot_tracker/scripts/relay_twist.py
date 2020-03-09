#!/usr/bin/env python

# This script is used to interface Rosie's mobility base with the Gazibo MiR-100 simulation of the VXLab. It allows for
# the simulated MiR-100 to mimic the movements of Rosie. The script ensures that Twist msgs can only be sent from the
# mobility base and not received. This is so that none of Rosie's safety features are overridden / compromised.
#
# The relay was also required, as the mobility base published the TwistStamped msg type, and Twist msg type is required
# by the simulator. Therefore a conversion of data types also occurs.
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import TwistStamped

pub = rospy.Publisher('/mirsim/cmd_vel', Twist, queue_size=1)


def cmd_callback(data):
    print data.twist
    print '---'
    pub.publish(data.twist)


def relay():
    rospy.init_node('relay_cmd_vel', anonymous=False)
    rospy.Subscriber('/mobility_base/twist', TwistStamped, cmd_callback)
    print 'Relay ready'
    rospy.spin()


if __name__ == '__main__':
    try:
        relay()
    except rospy.ROSInterruptException:
        pass
