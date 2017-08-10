import keyboard
import pymem
import time
from config import *

pm = pymem.Pymem("csgo.exe")


def main():
    toggled = False
    print("Ruby has launched. Auto bunny hopping is disabled. Toggle on with '{}'".format(hop_key))
    player = client_base + local_player
    in_air = pm.read_int(player) + m_fflags

    force_jump = client_base + dwforcejump

    while True:
        if keyboard.is_pressed("x"):
            if not toggled:
                toggled = True
                print("Bhop has been toggled on.")
                time.sleep(1)
            else:
                toggled = False
                print("Bhop has been toggled off.")
                time.sleep(1)

        result = pm.read_char(in_air)
        print(result)

        if toggled is True:
            if keyboard.is_pressed("space"):
                if result is 1:
                    pm.write_int(force_jump, 5)
                    time.sleep(0.20)
                    pm.write_int(force_jump, 4)
                    time.sleep(0.20)


if __name__ == '__main__':
    main()
