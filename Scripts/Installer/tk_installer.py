import os
import tkinter as tk


def check_file_exists(pkg_path):
    """Check if the given file path exists."""
    return os.path.isfile(pkg_path)


def install_pkgs(pkgs, text_widget, event):
    """Install the specified packages using AppleScript for administrative privileges."""
    applescript_commands = ''

    for pkg_path, file_name in pkgs:
        if not check_file_exists(pkg_path):
            text_widget.insert(tk.END, f"Package path {pkg_path} does not exist.\n")
            continue
        else:
            print(f'{pkg_path} exists')

        log_file = "/tmp/Pistol_log.txt"

        applescript_commands += (f'do shell script "bash -c \\"/usr/sbin/installer -verbose -pkg {pkg_path} '
                                 f'-target / >> {log_file} 2>&1\\"" with administrator privileges\n')

    text_widget.insert(tk.END, f"\nDone copying files.\n")
    text_widget.insert(tk.END, "\nWaiting for authentication...\n")
    text_widget.insert(tk.END, "\nThis might take up to 10 minutes, please wait\n")

    full_applescript = f"osascript -e '{applescript_commands}'"
    print(full_applescript)
    result = os.system(full_applescript)

    if result == 0:
        text_widget.insert(tk.END, f"Installed all packages successfully.\n")
    else:
        text_widget.insert(tk.END, f"Installation failed.\n")
        exit()

    event.set()
