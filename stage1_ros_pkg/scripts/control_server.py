#!/usr/bin/env python3
import rospy
from stage1_ros_pkg.srv import RobotControl, RobotControlResponse

# 全局状态（实际可以通过参数服务器或 topic 维护）
robot_state = {
    'battery': 100.0,
    'position_id': 1,
    'status': 'normal'
}

def handle_control(req):
    global robot_state
    rospy.loginfo("Received command: %s, param: %s", req.command, req.param)

    if req.command == "reset":
        robot_state['battery'] = 100.0
        robot_state['position_id'] = 1
        robot_state['status'] = "normal"
        return RobotControlResponse(True, "Robot reset to initial state.")

    elif req.command == "set_mode":
        mode = req.param
        if mode in ["normal", "warning", "error"]:
            robot_state['status'] = mode
            return RobotControlResponse(True, f"Mode set to {mode}.")
        else:
            return RobotControlResponse(False, "Invalid mode.")

    elif req.command == "set_battery":
        try:
            value = float(req.param)
            if 0 <= value <= 100:
                robot_state['battery'] = value
                return RobotControlResponse(True, f"Battery set to {value}%.")
            else:
                return RobotControlResponse(False, "Battery value must be between 0 and 100.")
        except ValueError:
            return RobotControlResponse(False, "Invalid battery value.")

    else:
        return RobotControlResponse(False, "Unknown command.")

def control_server():
    rospy.init_node('control_server')
    srv = rospy.Service('/robot_control', RobotControl, handle_control)
    rospy.loginfo("Control server ready.")
    rospy.spin()

if __name__ == '__main__':
    control_server()
