import subprocess
import os
import shutil
import pwd
import grp

username = os.popen('whoami').read().strip()


def copy_files(source_folder, destination_folder):
    if not os.path.isdir(source_folder):
        print(f"The specified source folder does not exist: {source_folder}")
        return

    files = os.listdir(source_folder)
    if not files:
        print("No files found in the source folder.")
        return

    valid_files = []
    for file_name in files:
        source_file = os.path.join(source_folder, file_name)
        if os.path.isfile(source_file):
            valid_files.append(source_file)

    if not valid_files:
        print("No valid files to copy.")
        return

    try:
        # Create a temporary folder in /tmp
        temp_folder = "/tmp/presets2"
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)

        # Copy valid files from the source folder to the temporary folder
        for source_file in valid_files:
            shutil.copy(source_file, temp_folder)

        # Change ownership of the copied files to the current user

        uid = pwd.getpwnam(username).pw_uid
        gid = pwd.getpwnam(username).pw_gid

        for source_file in valid_files:
            tmp_file = os.path.join(temp_folder, os.path.basename(source_file))
            os.chown(tmp_file, uid, gid)
            print(f"Changed ownership for {tmp_file} to user {username}.")

        # Create the AppleScript command to move all files at once
        move_commands = [f"mv '{os.path.join(temp_folder, os.path.basename(source_file))}' '{destination_folder}'" for source_file in valid_files]
        combined_move_command = " && ".join(move_commands)
        applescript_command = f'do shell script "{combined_move_command}" with administrator privileges'
        result = subprocess.run(['osascript', '-e', applescript_command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode == 0:
            print("All files moved successfully.")
        else:
            print(f"Failed to move files: {result.stderr.decode()}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Clean up the temporary folder
        shutil.rmtree(temp_folder, ignore_errors=True)

# Example usage
# source_folder = "../../pkgs/Presets"
# destination_folder = f"/users/{username}/library/preferences/"
# copy_files(source_folder, destination_folder)
