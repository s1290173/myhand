from elegripper import Gripper
import time

g = Gripper("/dev/ttyUSB0", baudrate=115200, id=14)

# 念のため有効化（00 01 = enable）
g.set_gripper_enable(1)
time.sleep(0.1)

print("Gripper ID:", g.get_gripper_Id())      # 14 が返るはず
print("FW Major:", g.get_firmware_version())  # 例: 1

# 開く（100）→ 閉じる（0）
g.set_gripper_value(100, speed=80)
time.sleep(1.0)
print("Angle now:", g.get_gripper_value())    # 100 付近

g.set_gripper_value(0, speed=80)
time.sleep(1.0)
print("Angle now:", g.get_gripper_value())  
