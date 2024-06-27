import os
import sys


# def on_closing():
#     if install_thread is not None and install_thread.is_alive():
#         messagebox.showinfo("Wait", "Installation is still running. Please wait until it finishes.")
#     else:
#         main_window.destroy()


def change_button_to_quit(install_button):
    install_button.config(text="Quit", state=tk.NORMAL, command=main_window.quit)


def to_absolute(relative_path):
    return os.path.abspath(os.path.join(find_base_dir(), relative_path))


def find_base_dir():
    # Determine the base directory
    if hasattr(sys, '_MEIPASS'):
        base_dir = os.path.join(sys._MEIPASS, 'Resources')
        return base_dir
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        return base_dir
