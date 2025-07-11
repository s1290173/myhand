from MyHand import MyGripper_H100
import time
if __name__=="__main__":
    g=MyGripper_H100("/dev/ttyCH343USB0",baudrate=115200,id=14)##填写实际的串口号和波特率和夹爪ID
    print("夹爪的实际ID为:",g.get_gripper_Id())
    print(g.set_gripper_joint_angle(1,50))
    time.sleep(2)
    print(g.set_gripper_joint_angle(1,0))
    time.sleep(2)
    print(g.set_gripper_joint_angle(2,100))
    time.sleep(2)
    print(g.set_gripper_joint_angle(2,0))
    time.sleep(2)
    print(g.set_gripper_joint_angle(3,50))
    time.sleep(2)
    print(g.set_gripper_joint_angle(3,0))
    time.sleep(2)
    print(g.set_gripper_joint_angle(4,50))
    time.sleep(2)
    print(g.set_gripper_joint_angle(4,0))
    time.sleep(2)
    print(g.set_gripper_joint_angle(5,50))
    time.sleep(2)
    print(g.set_gripper_joint_angle(5,0))
    time.sleep(2)
    print(g.set_gripper_joint_angle(6,50))
    time.sleep(2)
    print(g.set_gripper_joint_angle(6,0))
    time.sleep(2)


