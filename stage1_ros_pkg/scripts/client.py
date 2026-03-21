#!/usr/bin/env python3
import rospy
import sys
from stage1_ros_pkg.srv import AddTwoInts

def add_two_ints_client(a, b):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        resp = add_two_ints(a, b)
        return resp.sum
    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: client.py <a> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    rospy.init_node('add_two_ints_client')
    result = add_two_ints_client(a, b)
    if result is not None:
        rospy.loginfo(f"Result of {a} + {b} = {result}")
    else:
        rospy.logerr("Service call failed")
