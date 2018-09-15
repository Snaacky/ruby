import keyboard
import pymem
import pymem.process
import time

dwForceJump = (0x50DE048)
dwLocalPlayer = (0xC5E87C)
m_fFlags = (0x100)

pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_id, "client_panorama.dll").base_address


def main():
    print("Ruby has launched.")

    while True:
        try:
            player = pm.read_int(client + dwLocalPlayer)
            force_jump = client + dwForceJump
            on_ground = pm.read_char(player + m_fFlags)

            if keyboard.is_pressed("space"):
                if on_ground:
                    pm.write_int(force_jump, 5)
                    time.sleep(0.20)
                    pm.write_int(force_jump, 4)
                    time.sleep(0.20)
            time.sleep(0.002)
        except pymem.exception.MemoryReadError:
            pass


if __name__ == '__main__':
    main()
