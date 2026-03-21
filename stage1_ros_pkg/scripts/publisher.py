#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import rospy
from std_msgs.msg import String

def publisher():
    rospy.init_node('talker',anonymous=False)
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rate = rospy.Rate(1)  # 1Hz
    count = 0
    while not rospy.is_shutdown():
        msg = String()
        msg.data = "Hello ROS! Count: %d" % count
        rospy.loginfo("Publishing: %s", msg.data)
        pub.publish(msg)
        rate.sleep()
        count += 1

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass


