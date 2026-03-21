#!/usr/bin/env python3
import rospy
from stage1_ros_pkg.srv import AddTwoInts, AddTwoIntsResponse

def handle_add_two_ints(req):
    # 接收请求，返回响应
    result = req.a + req.b
    rospy.loginfo(f"Received request: {req.a} + {req.b} = {result}")
    return AddTwoIntsResponse(result)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    # 创建服务，服务名称为 'add_two_ints'，类型为 AddTwoInts
    srv = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    rospy.loginfo("Ready to add two ints.")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
