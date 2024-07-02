import os
import shutil
import pwd

# Get the current username
# username = os.popen('whoami').read().strip()
username = os.getenv('USER')
uid = pwd.getpwnam(username).pw_uid
gid = pwd.getpwnam(username).pw_gid


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

        # Copy valid files from the source folder to the temporary folder
        for source_file in list_of_files_with_full_paths:
            # print(f"SOURCE FILES{source_file}")

            os.chown(source_file, uid, gid)
            print(f"Changed ownership for {source_file} to user {username}.")
            shutil.copy(source_file, destination_folder)
            print(f"Copied {source_file} to {destination_folder}")

        print("All files moved successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")
