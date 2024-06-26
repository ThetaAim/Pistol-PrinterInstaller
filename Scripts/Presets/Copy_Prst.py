import os
import shutil
import pwd

# Get the current username
# username = os.popen('whoami').read().strip()
username = os.getenv('USER')


def copy_files(source_folder, destination_folder):
    list_of_files_with_full_paths = []

    files = os.listdir(source_folder)
    if not files:
        print("No files found in the source folder.")
        return

    for file in files:
        if os.path.isfile(os.path.join(source_folder, file)):
            list_of_files_with_full_paths.append(os.path.join(source_folder, file))
        else:
            print(f"The file {file} is missing or not a regular file. Unable to copy.")

    try:
        # Create a temporary folder in /tmp
        temp_folder = "/tmp/presets"
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)

        # Copy valid files from the source folder to the temporary folder
        for source_file in list_of_files_with_full_paths:
            shutil.copy(source_file, temp_folder)
            print(f"Copied {source_file} to {temp_folder}")

        # Change ownership of the copied files to the current user
        files_in_tmp_folder = os.listdir(temp_folder)
        if not files_in_tmp_folder:
            print('No Files in temp')
            return
        
        uid = pwd.getpwnam(username).pw_uid
        gid = pwd.getpwnam(username).pw_gid

        for tmp_file in files_in_tmp_folder:
            full_path_tmp_file = os.path.join(temp_folder, tmp_file)
            os.chown(full_path_tmp_file, uid, gid)
            print(f"Changed ownership for {tmp_file} to user {username}.")

        # Move files from the temporary folder to the destination folder
        for tmp_file in files_in_tmp_folder:
            destination_file = os.path.join(destination_folder, tmp_file)
            shutil.move(os.path.join(temp_folder, tmp_file), destination_file)
            print(f"Moved and overwritten {tmp_file} to {destination_file}")

        print("All files moved successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Clean up the temporary folder
        try:
            shutil.rmtree(temp_folder, ignore_errors=True)
        except Exception as e:
            print(f"Failed to delete temporary folder {temp_folder}: {e}")
