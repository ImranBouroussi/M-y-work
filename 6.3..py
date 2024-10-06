import os
from pynput import keyboard
 
x = 3
y = 3
 
def printta():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(5):
        row = ""
        for d in range(5):
            if i == y and d == x:
                row += "O"
            else:
                row += "."
        print(row)
 
def button(key):
    global x, y
    try:
        if key == keyboard.Key.up and y > 0:
            y -= 1
        elif key == keyboard.Key.down and y < 4:
            y += 1
        elif key == keyboard.Key.left and x > 0:
            x -= 1
        elif key == keyboard.Key.right and x < 4:
            x += 1
 
        printta()
    except AttributeError:
        return False
 
printta()
with keyboard.Listener(on_press=button) as listener:
    listener.join()