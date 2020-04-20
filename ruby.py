import keyboard
import pymem
import pymem.process
import time
from win32gui import GetWindowText, GetForegroundWindow

dwForceJump = (0x51ED750)
dwLocalPlayer = (0xD2FB84)
m_fFlags = (0x104)


def main():
    print("Ruby has launched.")
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client_panorama.dll").lpBaseOfDll

    while True:
        if not GetWindowText(GetForegroundWindow()) == "Counter-Strike: Global Offensive":
            continue

        if keyboard.is_pressed("space"):
            force_jump = client + dwForceJump
            player = pm.read_int(client + dwLocalPlayer)
            if player:
                on_ground = pm.read_int(player + m_fFlags)
                if on_ground and on_ground == 257:
                    pm.write_int(force_jump, 5)
                    time.sleep(0.08)
                    pm.write_int(force_jump, 4)

        time.sleep(0.002)


if __name__ == '__main__':
    main()
