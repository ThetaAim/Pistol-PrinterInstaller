import subprocess
import os
import shutil


def check_file_exists(pkg_path):
    """Check if the given file path exists."""
    return os.path.isfile(pkg_path)


def install_pkg(pkg_path, file_name):
    """Install the specified package using AppleScript for administrative privileges."""
    if not check_file_exists(pkg_path):
        print(f"Package path {pkg_path} does not exist.")
        return

    tmp_pkg_path = f'/tmp/{file_name}.pkg'
    try:
        shutil.copy(pkg_path, tmp_pkg_path)
        print(f"Copied package to {tmp_pkg_path}. Proceeding with installation.")
        print(tmp_pkg_path)
        install_command = f'sudo /usr/sbin/installer -verbose -pkg {tmp_pkg_path} -target /'

        # Correcting the AppleScript syntax by using escape characters
        applescript_command = f'do shell script "{install_command}" with administrator privileges'
        result = subprocess.run(['osascript', '-e', applescript_command], stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)

        if result.returncode == 0:
            print(f"Installation completed successfully:\n{result.stdout.decode()}")
        else:
            print(f"Installation failed:\n{result.stderr.decode()}")
    except subprocess.CalledProcessError as e:
        print(f"Installation failed: {e}")
    except Exception as e:
        print(f"Installation aborted: {e}")
    finally:
        if os.path.exists(tmp_pkg_path):
            os.remove(tmp_pkg_path)
            print(f"Cleaned up {tmp_pkg_path}.")



