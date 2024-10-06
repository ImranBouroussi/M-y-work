from pynput import keyboard

Teksti = {
    '1': "Partridge in a pear tree",
    '2': "Two french hens",
    '3': "Three turtle doves",
    '4': "Four calling birds",
    '5': "FIVE GOLD RINGS",
    '6': "Six geese-a-laying",
    '7': "Seven swans-a-swimming",
    '8': "Eight maids-a-milking",
    '9': "Nine ladies dancing",
    '0': "Joulu on peruttu!"
}

def on_click(key):
    try:
        if hasattr(key, 'char') and key.char in Teksti:
            print(Teksti[key.char])
    except AttributeError:
        pass

with keyboard.Listener(on_press=on_click) as listener:
    listener.join()