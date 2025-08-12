from elegripper import Gripper
import time

if __name__ == "__main__":
    # 実際のシリアルポート、ボーレート、グリッパーIDを入力してください
    g = Gripper("COM27", baudrate=115200, id=14)
    print("Gripper ID:", g.get_gripper_Id())

    # 全開（値 = 100）→ 全閉（値 = 0）
    g.set_gripper_value(100, 100)
    time.sleep(2)
    g.set_gripper_value(0, 100)
    time.sleep(2)
