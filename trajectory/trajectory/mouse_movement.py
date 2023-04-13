import pyautogui, time
from PIL import Image, ImageDraw
import win32api

window_size = (1920, 1080)

color_line = (108, 204, 96)
thickness = 4
cords = []

start_time = time.time()

img = Image.new('RGB', window_size, (255, 255, 255))
draw = ImageDraw.Draw(img)

while time.time() - start_time < 10:
    x, y = win32api.GetCursorPos()
    cords.append((x, y))
    
    if len(cords) > 1:
        draw.line([cords[-2], cords[-1]], fill=color_line, width=thickness)
        
    time.sleep(0.1)

img.save('trajectory.png')

with open('mouse_coords.txt', 'w') as f:
    for cord in cords:
        f.write(f'{cord[0]} {cord[1]}\n')