import os
import subprocess
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

# Run YSoft uninstall script with admin privileges
Ysoft_Uninstall = "../../pkgs/Ysoft/uninstall-safeq-client.command"
try:
    subprocess.run(['sudo', '-S', Ysoft_Uninstall], check=True)
    print("YSoft uninstallation completed.")
except subprocess.CalledProcessError as e:
    print(f"Failed to run the uninstallation script: {e}")

###

# def uninstall_ysoft():
#     if os.geteuid() != 0:
#         # Not running as root, so rerun with sudo
#         subprocess.run(['sudo', 'python3', __file__])
#         exit()
#
#     # Kill processes
#     os.system("pkill -f '/Applications/SafeQClient'")
#     os.system("pkill -f '/Applications/YSoft SafeQ Client'")
#
#     # Remove applications
#     os.system("rm -rf '/Applications/SafeQClient.app' '/Applications/YSoft SafeQ Client.app'")
#
#     # Remove other files
#     os.system("rm -rf '/usr/libexec/cups/backend/sqport' '/Library/PreferencePanes/ClientPreferences.prefPane'")
#     os.system("rm -rf '/Library/Application Support/YSoft'")
#
#     # Remove launch daemons
#     os.system("launchctl remove com.ysoft.service.CUPS")
#     os.system("launchctl remove com.ysoft.service.DHCPOption")
#     os.system("rm -rf '/Library/LaunchDaemons/com.ysoft.service.CUPS.plist' '/Library/LaunchDaemons/com.ysoft.service.DHCPOption.plist'")
#
#     # Remove launch agent
#     os.system("launchctl asuser $(stat -f%u /dev/console) sudo -u $(id -un $(stat -f%u /dev/console)) launchctl remove com.ysoft.client.agent")
#     os.system("rm -rf '/Library/LaunchAgents/com.ysoft.client.agent.plist'")
#
#     # Forget package receipt
#     os.system("pkgutil --forget com.ysoft.safeq.client")
#
#     # Deactivate relaxed sandbox in CUPS
#     cups_config = "/etc/cups/cups-files.conf"
#     os.system("launchctl stop org.cups.cupsd")
#     os.system(f"sed -i '' -e 's/Sandboxing Relaxed//g' '{cups_config}'")
#     os.system("launchctl start org.cups.cupsd")
#
#     uninstall_ysoft()