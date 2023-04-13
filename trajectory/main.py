import win32api, win32con, win32gui, time, keyboard
from os import system

x = 0
y = 0
speed = 2
iterator = 0
activate = False

list_x = [0, -2, -2, -2, -7, -6, -6, -6, -12, -12, -15, -15, -15, -8, -4, -10, -7, -3, -12, -6, -15, 0, -9, -6, -12, -7, -4]
list_y = [0, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 19, 19, 19, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
#list_y = [15, 14, 11, 14, 6, 14, 12, 15, 11, 14, 12, 15, 13, 17, 17, 14, 19, 16, 18, 27, 26, 18, 36, 27, 68, 58, 22]
print(len(list_y))

while True:
    if keyboard.is_pressed('x'):
        if activate:
            activate = False
            time.sleep(1.5)
        
        else:
            activate = True
            time.sleep(1.5)
        
        system('cls')

        print(activate)


    if win32api.GetKeyState(0x01) < 0 and (keyboard.is_pressed('ctrl') and activate):
        iterator += 1
        if(iterator < 27):
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, list_x[iterator] * 2, list_y[iterator] * 2, 0, 0)
            print(list_y[iterator])
        time.sleep(0.1342)


    else:
        iterator = 0
    
    time.sleep(0.01)