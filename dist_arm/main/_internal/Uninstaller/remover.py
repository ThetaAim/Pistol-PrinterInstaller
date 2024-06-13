import os

username = os.popen('whoami').read().strip()

# List of files to remove
files_to_remove = [
    "com.apple.print.add.plist",
    "com.apple.print.custompresets.forprinter.Black.plist",
    "com.apple.print.custompresets.forprinter.Color.plist",
    "com.apple.print.custompresets.forprinter.Fiery.plist",
    "com.apple.print.custompresets.forprinter.Mix.plist",
    "com.apple.print.custompresets.forprinter.Unique.plist",
    "com.apple.print.custompresets.plist"
]

# Base directory
base_directory = f"/users/{username}/library/preferences/"

# Remove each file
for file in files_to_remove:
    file_path = os.path.join(base_directory, file)
    try:
        os.remove(file_path)
        print(f"Removed: {file_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error removing {file_path}: {e}")

# Remove Printers
def remove_printer(printer_name):
    result = os.system(f'lpadmin -x {printer_name}')
    if result == 0:
        print('Printer removed')
    else:
        print(f"Failed to remove printer {printer_name}. Command returned: {result}")


printers_to_remove = ["Black", "Fiery", "Unique", "Color"]
# [remove_printer(printer) for printer in printers_to_remove if printer]
for printer in printers_to_remove:
    remove_printer(printer)

# # Remove YSoft

command = f"sudo -S ../../pkgs/Ysoft/uninstall-safeq-client.command"
os.popen(command).read().strip()
