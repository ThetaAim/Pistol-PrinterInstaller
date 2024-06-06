import os
import shutil
import tkinter as tk


def check_file_exists(pkg_path):
    """Check if the given file path exists."""
    return os.path.isfile(pkg_path)


def install_pkgs(pkgs, text_widget):
    """Install the specified packages using AppleScript for administrative privileges."""
    tmp_pkg_paths = []
    pkg_names = []

    for pkg_path, file_name in pkgs:
        if check_file_exists(pkg_path):
            tmp_pkg_path = f'/tmp/{file_name}.pkg'
            try:
                shutil.copy(pkg_path, tmp_pkg_path)
                text_widget.insert(tk.END, f"Coping files...\n")
                tmp_pkg_paths.append(tmp_pkg_path)
                pkg_names.append(file_name)
            except Exception as e:
                text_widget.insert(tk.END, f"Failed to copy {pkg_path} to {tmp_pkg_path}: {e}\n")
        else:
            text_widget.insert(tk.END, f"Package path {pkg_path} does not exist.\n")

    if not tmp_pkg_paths:
        text_widget.insert(tk.END, "No packages to install.\n")
        return

    try:
        applescript_commands = ''

        for tmp_pkg_path, file_name in zip(tmp_pkg_paths, pkg_names):
            applescript_commands += f'do shell script "/usr/sbin/installer -verbose -pkg {tmp_pkg_path} -target /" with administrator privileges\n'

        full_applescript = f"osascript -e '{applescript_commands}'"
        result = os.system(full_applescript)

        if result == 0:
            for file_name in pkg_names:
                text_widget.insert(tk.END, f"Installed {file_name} package successfully.\n")
        else:
            text_widget.insert(tk.END, "Installation failed.\n")
    except Exception as e:
        text_widget.insert(tk.END, f"Installation aborted: {e}\n")
    finally:
        for tmp_pkg_path in tmp_pkg_paths:
            if os.path.exists(tmp_pkg_path):
                os.remove(tmp_pkg_path)
                text_widget.insert(tk.END, f"Cleaned up {tmp_pkg_path}.\n")
