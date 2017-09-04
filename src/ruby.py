import keyboard
import pymem
import pymem.process
import time
from config import *

pm = pymem.Pymem("csgo.exe")


def main():
    print("Ruby has launched. Enable bhop with {}.".format(hop_key))
    client = pymem.process.module_from_name(pm.process_id, "client.dll")
    player = client.base_address + dwLocalPlayer
    in_air = pm.read_int(player) + m_fFlags
    force_jump = client.base_address + dwForceJump

    toggled = False

    while True:
        if keyboard.is_pressed(hop_key):
            if not toggled:
                toggled = True
                print("Bhop has been toggled on.")
                time.sleep(1)
            else:
                toggled = False
                print("Bhop has been toggled off.")
                time.sleep(1)

        result = pm.read_char(in_air)

        if toggled is True:
            if keyboard.is_pressed("space"):
                if result is 1:
                    pm.write_int(force_jump, 5)
                    time.sleep(0.20)
                    pm.write_int(force_jump, 4)
                    time.sleep(0.20)


if __name__ == '__main__':
    main()
