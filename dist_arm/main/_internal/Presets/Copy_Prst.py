import os
import shutil
import pwd

# Get the current username
username = os.popen('whoami').read().strip()

def copy_files(source_folder, destination_folder):
    # Check if the source folder exists and list its files
    if not os.path.isdir(source_folder):
        print(f"The specified source folder does not exist: {source_folder}")
        return

    files = os.listdir(source_folder)
    if not files:
        print("No files found in the source folder.")
        return

    # Initialize an empty list to store valid file paths
    valid_files = [os.path.join(source_folder, file_name)
                   for file_name in files
                   if os.path.isfile(os.path.join(source_folder, file_name))]

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
            destination_file = os.path.join(temp_folder, os.path.basename(source_file))
            if os.path.exists(destination_file):
                os.remove(destination_file)
            shutil.copy(source_file, destination_file)
            print(f"Copied {source_file} to {temp_folder}")

        # Change ownership of the copied files to the current user
        uid = pwd.getpwnam(username).pw_uid
        gid = pwd.getpwnam(username).pw_gid

        for source_file in valid_files:
            tmp_file = os.path.join(temp_folder, os.path.basename(source_file))
            os.chown(tmp_file, uid, gid)
            print(f"Changed ownership for {tmp_file} to user {username}.")

        # Move files from the temporary folder to the destination folder
        for source_file in valid_files:
            tmp_file = os.path.join(temp_folder, os.path.basename(source_file))
            destination_file = os.path.join(destination_folder, os.path.basename(source_file))
            if os.path.exists(destination_file):
                os.remove(destination_file)
            shutil.move(tmp_file, destination_file)
            print(f"Moved {tmp_file} to {destination_folder}")

        print("All files moved successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Clean up the temporary folder
        shutil.rmtree(temp_folder, ignore_errors=True)


