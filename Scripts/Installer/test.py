import subprocess
import os
script_dir = '/Users/administrator/Desktop/Pistol/Scripts/Installer'
installer_script = os.path.join(script_dir, 'installer.sh')
# result = subprocess.run(
#     ['osascript', '-e', f'do shell script "sudo {installer_script}" with administrator privileges'],
#     text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
result = os.system(f'echo {osacode} | sudo -S' + ' ' + installer_script)
# Access the stdout and stderr output
# stdout_output = result.stdout
# stderr_output = result.stderr

print(result)
# print(stderr_output)
