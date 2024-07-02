import os
import sys


def change_button_to_quit(install_button):
    install_button.config(text="Quit", state=tk.NORMAL, command=main_window.quit)


def to_absolute(relative_path):
    return os.path.abspath(os.path.join(find_base_dir(), relative_path))


def find_base_dir():
    if hasattr(sys, '_MEIPASS'):
        # If running as a PyInstaller app
        base_dir = os.path.join(sys._MEIPASS, 'Resources')
    else:
        # Adjusting for parent directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = "../pkgs/"  # Move up one directory
    return base_dir

# Example usage
base_dir = find_base_dir()  # Call the function to get the base directory
print("Base Directory:", base_dir)  # Print the result