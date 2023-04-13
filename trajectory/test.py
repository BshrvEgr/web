import win32api, win32con, time, keyboard
from colorama import Fore
from os import system

iterator = 0
is_active = False

if __name__ == '__main__':
    while True:

        if keyboard.is_pressed('x'):

            if  is_active:
                system('cls')
                is_active = False
                print(Fore.RED + "Status: disabled")
                time.sleep(0.2)
        
            else:
                system('cls')
                is_active = True
                print(Fore.GREEN + "Status: enabled")
                time.sleep(0.2)

        if win32api.GetKeyState(0x01) < 0 and keyboard.is_pressed('ctrl') and is_active:

            if iterator <= 12:
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -1, 6, 0, 0)

            elif iterator >= 12 and iterator <= 25:
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -2, 4, 0, 0)
            
            elif iterator >= 26 and iterator <= 32:
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -3, 6, 0, 0)

            elif iterator >= 33 and iterator <= 46:  
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -3, 6, 0, 0)
            
            elif iterator >= 47 and iterator <= 60:
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -3, 4, 0, 0)

            elif iterator >= 61 and iterator <= 73:
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -5, 7, 0, 0)

            elif iterator >= 74 and iterator <= 86:
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -3, 5, 0, 0)

            elif iterator >= 87 and iterator <= 99:
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -4, 6, 0, 0)

            elif iterator >= 100 and iterator <= 112:
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -3, 5, 0, 0)

            elif iterator >= 113 and iterator <= 125:
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -4, 5, 0, 0)

            elif iterator >= 126 and iterator <= 138:
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -4, 5, 0, 0)

            elif iterator >= 139 and iterator <= 151:
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -2, 6, 0, 0)

            elif iterator >= 152 and iterator <= 164:
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, -3, 6, 0, 0)
            
            iterator += 1
            print(iterator)
            time.sleep(0.025)

        else:
            iterator = 0

        time.sleep(0.001)