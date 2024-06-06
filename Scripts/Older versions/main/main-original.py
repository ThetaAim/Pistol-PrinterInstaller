import os

from Installer.tester import install_pkgs
from Printers.Create_printer_with_settings import create_printer
from Presets.Copy_Prst import copy_files

# -- A.Setup files
packages = [
    ('../pkgs/Ysoft/Ysoft.pkg', 'Ysoft'),
    ('../pkgs/Fiery/fiery.pkg', 'fiery'),
    ('../pkgs/Color/color.pkg', 'c3000'),
    ('../pkgs/Uniqe/unique.pkg', 'unique'),
    ('../pkgs/Black/Black.pkg', 'black')
]
install_pkgs(packages)

# install_pkg('../pkgs/Ysoft/Ysoft.pkg', 'Ysoft')
# install_pkg('../pkgs/Fiery/fiery.pkg', 'fiery')
# install_pkg('../pkgs/Color/color.pkg', 'c3000')
# install_pkg('../pkgs/Uniqe/unique.pkg', 'unique')
# install_pkg('../pkgs/Black/Black.pkg', 'black')

# -- B.Create Printers and set Settings

create_printer("Fiery", "172.16.100.100", "ColB", "/Library/Printers/PPDs/"
               "Contents/Resources/Pro C7200Sseries E-35A PS 1.0", "MainFarm",
               EFPaperDeckOpt="Option2", EFFinisher="Finisher7", EFPerfectBinder=True)

create_printer("Color", "172.16.100.100", "ColS", "/Library/Printers/PPDs/Contents/Resources/RICOH IM C3000",
               "MainFarm", OptionTray="1Cassette")

create_printer("Unique", "172.16.100.100", "Tos", "/Library/Printers/PPDs/Contents/Resources/RICOH MP C4504",
               "MainFarm")

create_printer("Black", "172.16.100.100", "BWS", "/Library/Printers/PPDs/Contents/Resources/TOSHIBA_MonoMFP.gz", "MainFarm",
               ModelSelection="e-STUDIO4528ASeries", Pedestal="Drawer1234")

# -- D.Copy/Set Presets

username = os.popen('whoami').read().strip()
copy_files("../pkgs/Presets", f"/Users/{username}/Library/Preferences")
