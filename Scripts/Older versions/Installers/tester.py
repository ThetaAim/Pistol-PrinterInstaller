import os
import shutil
import subprocess

def check_file_exists(pkg_path):
    """Check if the given file path exists."""
    return os.path.isfile(pkg_path)


def install_pkgs(pkgs):
    """Install the specified packages using AppleScript for administrative privileges."""
    all_tmp_pkg_paths = []
    pkg_names = []

    for pkg_path, file_name in pkgs:
        if check_file_exists(pkg_path):
            tmp_pkg_path = f'/tmp/{file_name}.pkg'
            try:
                shutil.copy(pkg_path, tmp_pkg_path)
                print(f"Copied package to {tmp_pkg_path}.")
                all_tmp_pkg_paths.append(tmp_pkg_path)
                pkg_names.append(file_name)
            except Exception as e:
                print(f"Failed to copy {pkg_path} to {tmp_pkg_path}: {e}")
        else:
            print(f"Package path {pkg_path} does not exist.")

    if not all_tmp_pkg_paths:
        print("No packages to install.")
        return

    try:
        install_commands = ''

        for tmp_pkg_path in all_tmp_pkg_paths:
            install_commands = f'/usr/sbin/installer -verbose -pkg {tmp_pkg_path} -target /'
            result = subprocess.run(install_commands, shell=True, check=True, text=True)

        if result == 0:
            print("Installation completed successfully.")
            for file_name in pkg_names:
                print(f"Installed {file_name} package successfully.")
        else:
            print("Installation failed.")
    except Exception as e:
        print(f"Installation aborted: {e}")
    finally:
        for tmp_pkg_path in all_tmp_pkg_paths:
            if os.path.exists(tmp_pkg_path):
                os.remove(tmp_pkg_path)
                print(f"Cleaned up {tmp_pkg_path}.")
