#!/usr/bin/env python3
import rospy
from stage1_ros_pkg.msg import RobotStatus
import random

def status_publisher():
    rospy.init_node('status_publisher', anonymous=False)
    pub = rospy.Publisher('/robot_status', RobotStatus, queue_size=10)
    rate = rospy.Rate(1)  # 1Hz

    battery = 100.0
    position_id = 1
    status = "normal"

    while not rospy.is_shutdown():
        battery -= random.uniform(0, 5)
        if battery < 0:
            battery = 0
        if battery < 20:
            status = "warning"
        elif battery == 0:
            status = "error"
        else:
            status = "normal"

        # 示例：随时间改变位置
        if rospy.get_time() > 10:
            position_id = 2
        if rospy.get_time() > 20:
            position_id = 3

        msg = RobotStatus()
        msg.battery = battery
        msg.position_id = position_id
        msg.status = status

        rospy.loginfo("Publishing: battery=%.1f%%, position=%d, status=%s",
                      battery, position_id, status)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        status_publisher()
    except rospy.ROSInterruptException:
        pass
