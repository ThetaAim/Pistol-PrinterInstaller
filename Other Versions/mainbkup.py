import os
import sys
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from threading import Thread
from Scripts.Installer.tk_installer import install_pkgs
from Scripts.Printers.Create_printer_with_settings import create_printer
from Scripts.Presets.Copy_Prst import copy_files


def disable_event():
    pass

def run_installation(text_widget, install_button):
    # Disable the install button
    install_button.config(state=tk.DISABLED)

    # Determine the base directory
    if hasattr(sys, '_MEIPASS'):
        base_dir = os.path.join(sys._MEIPASS, 'Resources')
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))

    # Convert relative paths to absolute paths
    def to_absolute(relative_path):
        return os.path.abspath(os.path.join(base_dir, relative_path))

    # A. Run Package Installer Setup files
    packages = [
        (to_absolute('../../pkgs/Ysoft/Ysoft.pkg'), 'Ysoft'),
        (to_absolute('../../pkgs/Fiery/fiery.pkg'), 'Fiery'),
        (to_absolute('../../pkgs/Color/color.pkg'), 'Color'),
        (to_absolute('../../pkgs/Uniqe/unique.pkg'), 'Unique'),
        (to_absolute('../../pkgs/Black/Black.pkg'), 'Black')
    ]
    print(packages[0])
    printer_configs = [
        (
            "Fiery", "172.16.100.100", "ColB",
            "/Library/Printers/PPDs/Contents/Resources/en.lproj/Pro C7200Sseries E-35A PS 1.0", "MainFarm",
            {"EFPaperDeckOpt": "Option2", "EFFinisher": "Finisher7", "EFPerfectBinder": True}
        ),
        (
            "Color", "172.16.100.100", "ColS",
            "/Library/Printers/PPDs/Contents/Resources/RICOH IM C3000", "MainFarm",
            {"OptionTray": "1Cassette"}
        ),
        (
            "Unique", "172.16.100.100", "Tos",
            "/Library/Printers/PPDs/Contents/Resources/RICOH MP C4504", "MainFarm",
            {}
        ),
        (
            "Black", "172.16.100.100", "BWS",
            "/Library/Printers/PPDs/Contents/Resources/TOSHIBA_MonoMFP.gz", "MainFarm",
            {"ModelSelection": "e-STUDIO4528ASeries", "Pedestal": "Drawer1234"}
        )
    ]


    install_pkgs(packages, text_widget)

    # B. Create Printers and set Settings
    text_widget.insert(tk.END, "Setting up printers...\n")
    # create_printer("Fiery", "172.16.100.100", "ColB",
    #                "/Library/Printers/PPDs/Contents/Resources/en.lproj/Pro C7200Sseries E-35A PS 1.0", "MainFarm",
    #                EFPaperDeckOpt="Option2", EFFinisher="Finisher7", EFPerfectBinder=True)

    create_printer(*printer_configs[0][:5], **printer_configs[0][5])


    # text_widget.insert(tk.END, "Printer Fiery setup completed.\n")
    #
    # create_printer("Color", "172.16.100.100", "ColS", "/Library/Printers/PPDs/Contents/Resources/RICOH IM C3000",
    #                "MainFarm", OptionTray="1Cassette")
    # text_widget.insert(tk.END, "Printer Color setup completed.\n")
    #
    # create_printer("Unique", "172.16.100.100", "Tos", "/Library/Printers/PPDs/Contents/Resources/RICOH MP C4504",
    #                "MainFarm")
    # text_widget.insert(tk.END, "Printer Unique setup completed.\n")
    #
    # create_printer("Black", "172.16.100.100", "BWS", "/Library/Printers/PPDs/Contents/Resources/TOSHIBA_MonoMFP.gz",
    #                "MainFarm", ModelSelection="e-STUDIO4528ASeries", Pedestal="Drawer1234")
    # text_widget.insert(tk.END, "Printer Black setup completed.\n")
    #

    # D. Copy/Set Presets
    username = os.popen('whoami').read().strip()
    copy_files(to_absolute("../../pkgs/Presets"), f"/Users/{username}/Library/Preferences")
    text_widget.insert(tk.END, "Copied presets successfully.\n")

    # Change the button to quit
    install_button.config(text="Quit", state=tk.NORMAL, command=main_window.quit)

def start_installation(text_widget, install_button):
    Thread(target=run_installation, args=(text_widget, install_button)).start()

def main():
    global main_window
    main_window = tk.Tk()
    main_window.title("Installer")

    # main_window.protocol("WM_DELETE_WINDOW", disable_event)

    text_widget = ScrolledText(main_window, wrap=tk.WORD, width=60, height=20)
    text_widget.pack(pady=10, padx=10)

    install_button = tk.Button(main_window, text="Start Installation",
                               command=lambda: start_installation(text_widget, install_button))
    install_button.pack(pady=10)

    main_window.mainloop()

if __name__ == "__main__":
    main()
