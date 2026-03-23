#!/usr/bin/env python3
import rospy
from stage1_ros_pkg.msg import RobotStatus

def callback(msg):
    if msg.battery < 20:
        rospy.logwarn("Low battery: %.1f%%", msg.battery)
    if msg.status == "error":
        rospy.logerr("Robot is in ERROR state!")
    elif msg.status == "warning":
        rospy.logwarn("Robot is in WARNING state!")
    else:
        rospy.loginfo("Robot OK: battery=%.1f%%, position=%d, status=%s",
                      msg.battery, msg.position_id, msg.status)

def monitor():
    rospy.init_node('status_monitor', anonymous=False)
    rospy.Subscriber('/robot_status', RobotStatus, callback)
    rospy.spin()

if __name__ == '__main__':
    monitor()

