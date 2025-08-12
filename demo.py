from pymycobot import MyCobot320
from pymycobot.genre import Angle
import time

mc = MyCobot320("/dev/ttyAMA0", 115200) # 実機のIP/port
mc.start_client()

# IOで駆動する設定のコントローラなら、DOピンで開閉
def gripper_open():
    mc.set_digital_out(16, 0)
    mc.set_digital_out(17, 1)

def gripper_close():
    mc.set_digital_out(16, 1)
    mc.set_digital_out(17, 0)

gripper_open();  time.sleep(1.0)
gripper_close(); time.sleep(1.0)
