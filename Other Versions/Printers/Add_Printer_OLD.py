import subprocess


def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Command succeeded: {result.stdout}")
        else:
            print(f"Command failed: {result.stderr}")
    except subprocess.CalledProcessError as e:
        print(f"Command execution failed: {e}")


def setup_printer(printer_name, ip_address, queue, ppd_path, location=""):
    # Add the printer using sqport
    command = f"lpadmin -p {printer_name} -v sqport://{ip_address}/{queue} -L '{location}' -P '{ppd_path}' -E -o printer-is-shared=false"
    run_command(command)

    # Set the Wide Large Capacity Tray option
    set_tray_command = f"lpadmin -p {printer_name} -o EFPaperDeckOpt=Option2"
    run_command(set_tray_command)

    # Set the Finisher to Fnisher7
    set_tray_command = f"lpadmin -p {printer_name} -o EFFinisher=Finisher7"
    run_command(set_tray_command)

    # Set the binder to True
    set_tray_command = f"lpadmin -p {printer_name} -o EFPerfectBinder=True"
    run_command(set_tray_command)


