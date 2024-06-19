import os
import tkinter as tk
from threading import Thread

# import Data
from Scripts.Installer.tk_installer import install_pkgs
from Scripts.Printers.Create_printer_with_settings import create_printer
from Scripts.Presets.Copy_Prst import copy_files
from Data.Data import packages, printer_configs, to_absolute


def run_installation(text_widget, install_button):

    # Disable the install button
    install_button.config(state=tk.DISABLED)

    # A. Run Package Installer Setup files
    ###############################################
    install_pkgs(packages, text_widget)

    # B. Create Printers and set Settings
    ###############################################
    text_widget.insert(tk.END, "Setting up printers...\n")

    for config in printer_configs:
        text_widget.insert(tk.END, f"Setting up {config[0]}...\n")
        create_printer(*config[:5], **config[5])

    # D. Copy/Set Presets
    username = os.popen('whoami').read().strip()
    copy_files(to_absolute("pkgs/Presets"), f"/Users/{username}/Library/Preferences")
    text_widget.insert(tk.END, "Copied presets successfully.\n")

    # Change the button to quit
    install_button.config(text="Quit", state=tk.NORMAL, command=main_window.quit)


def start_installation_with_thread(text_widget, install_button):
    Thread(target=run_installation, args=(text_widget, install_button)).start()
    # run_installation(text_widget, install_button)


def main():
    global main_window
    main_window = tk.Tk()

    posx = 800  # X coordinate
    posy = 300  # Y coordinate
    main_window.geometry(f"+{posx}+{posy}")

    main_window.title("Pistol Printer Installer")

    # main_window.protocol("WM_DELETE_WINDOW", disable_event)

    text_widget = tk.Text(main_window, wrap=tk.WORD, width=60, height=25)
    text_widget.pack(pady=10, padx=10)

    install_button = tk.Button(main_window, text="Start Installation",
                               command=lambda: start_installation_with_thread(text_widget, install_button))
    install_button.pack(pady=10)

    main_window.mainloop()


if __name__ == "__main__":
    main()
