import os
import shutil
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from threading import Thread


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
                text_widget.insert(tk.END, f"Copied package to {tmp_pkg_path}.\n")
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
        for tmp_pkg_path, file_name in zip(tmp_pkg_paths, pkg_names):
            text_widget.insert(tk.END, f"Installing {file_name}...\n")
            text_widget.update_idletasks()
            command = f'/usr/sbin/installer -verbose -pkg {tmp_pkg_path} -target /'
            applescript_command = f"osascript -e 'do shell script \"{command}\" with administrator privileges'"
            result = os.system(applescript_command)

            if result == 0:
                text_widget.insert(tk.END, f"Installed {file_name} package successfully.\n")
            else:
                text_widget.insert(tk.END, f"Installation of {file_name} failed.\n")
    except Exception as e:
        text_widget.insert(tk.END, f"Installation aborted: {e}\n")
    finally:
        for tmp_pkg_path in tmp_pkg_paths:
            if os.path.exists(tmp_pkg_path):
                os.remove(tmp_pkg_path)
                text_widget.insert(tk.END, f"Cleaned up {tmp_pkg_path}.\n")


def start_installation(pkgs, text_widget):
    Thread(target=install_pkgs, args=(pkgs, text_widget)).start()


def main():
    packages = [
        ('../../pkgs/Ysoft/Ysoft.pkg', 'Ysoft'),
        ('../../pkgs/Fiery/fiery.pkg', 'fiery'),
        ('../../pkgs/Color/color.pkg', 'c3000'),
        ('../../pkgs/Uniqe/unique.pkg', 'unique'),
        ('../../pkgs/Black/Black.pkg', 'black')
    ]

    root = tk.Tk()
    root.title("Package Installer")

    text_widget = ScrolledText(root, wrap=tk.WORD, width=60, height=20)
    text_widget.pack(pady=10, padx=10)

    install_button = tk.Button(root, text="Start Installation",
                               command=lambda: start_installation(packages, text_widget))
    install_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
