import os
import tkinter as tk
from threading import Thread
from tkinter import messagebox
import threading
import time

# Import Data
from Scripts.Installer.tk_installer import install_pkgs
from Scripts.Printers.Create_printer_with_settings import create_printer
from Scripts.Presets.Copy_Prst import copy_files
from Data.Data import packages, printer_configs
from Tools.tools import to_absolute

# Define the log file path
log_file = "/tmp/Pistol_log.txt"

open(log_file, "a")

# Initialize global variables
install_thread = None
install_event = None


def on_closing():
    if install_thread is not None and install_thread.is_alive():
        messagebox.showinfo("Wait", "Installation is still running. Please wait until it finishes.")
    else:
        main_window.destroy()


def change_button_to_quit(install_button):
    install_button.config(text="Quit", state=tk.NORMAL, command=main_window.quit)


def run_installation(text_widget, install_button, event):
    # Disable the install button
    install_button.config(state=tk.DISABLED)

    # Run Package Installer Setup files
    text_widget.insert(tk.END, "Starting Installation Process.\n")
    install_pkgs(packages, text_widget, event)

    # Create Printers and set Settings
    text_widget.insert(tk.END, "Setting up printers...\n")
    for config in printer_configs:
        text_widget.insert(tk.END, f"Setting up {config[0]}...\n")
        create_printer(*config[:5], **config[5])

    # Copy/Set Presets
    username = os.popen('whoami').read().strip()
    copy_files(to_absolute("../pkgs/Presets"), f"/Users/{username}/Library/Preferences")
    text_widget.insert(tk.END, "Copied presets successfully.\n")
    text_widget.insert(tk.END, "Installation complete.\n")

    # Signal Event Done
    event.set()
    # Change the button to quit
    change_button_to_quit(install_button)


def start_installation_with_thread(text_widget, install_button):
    global install_thread, install_event
    install_event = threading.Event()
    install_thread = threading.Thread(target=run_installation, args=(text_widget, install_button, install_event))
    install_thread.start()


def update_log(text_widget, log_file, done_event):
    """Update the Text widget with the latest log content."""
    while not done_event.is_set():  # Continue updating until the installation is done
        try:
            with open(log_file, "r") as file:
                log_content = file.read()
            text_widget.delete(1.0, tk.END)  # Clear the Text widget
            text_widget.insert(tk.END, log_content)  # Insert new log content
        except Exception as e:
            text_widget.insert(tk.END, f"Error reading log file: {e}\n")

        time.sleep(1)  # Wait for 5 seconds before checking again

    # Final update after installation is done
    try:
        with open(log_file, "r") as file:
            log_content = file.read()
        text_widget.delete(1.0, tk.END)  # Clear the Text widget
        text_widget.insert(tk.END, log_content)  # Insert new log content
    except Exception as e:
        text_widget.insert(tk.END, f"Error reading log file: {e}\n")


def main():
    global main_window

    main_window = tk.Tk()

    posx = 800  # X coordinate
    posy = 300  # Y coordinate
    main_window.geometry(f"+{posx}+{posy}")

    main_window.title("Pistol Printer Installer")

    main_window.protocol("WM_DELETE_WINDOW", on_closing)

    text_widget = tk.Text(main_window, wrap=tk.WORD, width=60, height=25)
    text_widget.pack(pady=10, padx=10)

    install_button = tk.Button(main_window, text="Start Installation",
                               command=lambda: start_installation_with_thread(text_widget, install_button))
    install_button.pack(pady=10)

    # Create an Event object to signal when the installation is done
    done_event = threading.Event()

    # Start the log update in a separate thread
    log_thread = threading.Thread(target=update_log, args=(text_widget, log_file, done_event))
    log_thread.daemon = True  # Ensure the thread exits when the main program exits
    log_thread.start()

    main_window.mainloop()


if __name__ == "__main__":
    main()
