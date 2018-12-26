import keyboard
import pymem
import pymem.process
import time

dwForceJump = (0x5170DB0)
dwLocalPlayer = (0xCBD6B4)
m_fFlags = (0x104)

pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client_panorama.dll").lpBaseOfDll


def main():
    print("Ruby has launched.")

    while True:
        try:
            player = pm.read_int(client + dwLocalPlayer)
            force_jump = client + dwForceJump
            on_ground = pm.read_int(player + m_fFlags)
            
            if keyboard.is_pressed("space"):
                if on_ground == 257:
                    pm.write_int(force_jump, 5)
                    time.sleep(0.17)
                    pm.write_int(force_jump, 4)
            time.sleep(0.002)
        except pymem.exception.MemoryReadError:
            pass


if __name__ == '__main__':
    main()