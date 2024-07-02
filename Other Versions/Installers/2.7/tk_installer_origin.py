import os
import shutil
import tkinter as tk

import subprocess


def check_file_exists(pkg_path):
    """Check if the given file path exists."""
    return os.path.isfile(pkg_path)


def install_pkgs(pkgs, text_widget, event):
    """Install the specified packages using AppleScript for administrative privileges."""
    applescript_commands = ''
    tmp_paths = []
    for pkg_path, file_name in pkgs:
        if not check_file_exists(pkg_path):
            text_widget.insert(tk.END, f"Package path {pkg_path} does not exist.\n")
            continue

        tmp_pkg_path = f'/tmp/{file_name}.pkg'
        tmp_paths.append(tmp_pkg_path)
        try:
            shutil.copy(pkg_path, tmp_pkg_path)
            # text_widget.insert(tk.END, f"Coping files...\n")
        except Exception as e:
            text_widget.insert(tk.END, f"Failed to copy {pkg_path} to {tmp_pkg_path}: {e}\n")
            continue

        # Collects Commands in lines for AppleScript to run

        # applescript_commands += (f'do shell script "/usr/sbin/installer -verbose -pkg {tmp_pkg_path} '
        #                          f'-target /" with administrator privileges\n')
        log_file = "/tmp/Pistol_log.txt"

        applescript_commands += (f'do shell script "bash -c \\"/usr/sbin/installer -verbose -pkg {tmp_pkg_path} '
                                 f'-target / >> {log_file} 2>&1\\"" with administrator privileges\n')

    text_widget.insert(tk.END, f"\nDone Coping files.\n")
    text_widget.insert(tk.END, "\nWaiting for authentication...\n")
    text_widget.insert(tk.END, "\nThis Might take up to 10 minutes, Please wait\n")

    #  full_applescript = f"osascript -e {shlex.quote(applescript_commands)}"
    full_applescript = f"osascript -e '{applescript_commands}'"

    # Run the command using os.system
    result = os.system(full_applescript)

    if result == 0:
        text_widget.insert(tk.END, f"Installed All package successfully.\n")
    else:
        text_widget.insert(tk.END, f"Installation failed.\n")
        exit()

#   Remove temp file(s)
    for tmp in tmp_paths:

        if os.path.exists(tmp):
            os.remove(tmp)
            text_widget.insert(tk.END, f"Cleaned up temp file.\n")

#   Signal Event Done, all packages have been installed
    event.set()

