from elegripper import Gripper
import time

g = Gripper("/dev/ttyAMA0", baudrate=115200, id=14)

print("try FW:", g.get_firmware_version())
print("try ID:", g.get_gripper_Id()) 
