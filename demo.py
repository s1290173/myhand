from pymycobot import MyCobot320
from pymycobot.genre import Angle
import time

GRIPPER_ID　= 14

mc = MyCobot320("/dev/ttyAMA0", 115200) # 実機のIP/port
mc.power_on()
time.sleep(0.3)

# 開く→閉じる→角度指定（0〜100）
mc.set_pro_gripper_open(GRIPPER_ID)
time.sleep(1.0)

mc.set_pro_gripper_close(GRIPPER_ID)
time.sleep(1.0)

mc.set_pro_gripper_angle(GRIPPER_ID, 100)
time.sleep(1.0)
mc.set_pro_gripper_angle(GRIPPER_ID, 0)
