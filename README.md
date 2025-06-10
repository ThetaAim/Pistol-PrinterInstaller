# 🖨️ Pistol - Printer Installer for macOS

**Pistol**, AKA "Printer Installer", is an intuitive macOS application designed to streamline the setup of multiple printers and apply their preferences automatically. It empowers users — especially students — to print their work directly from their laptops without relying on shared institutional devices, making printing faster, simpler, and more user-friendly.

Built with care, clarity, and some command-line magic ✨ — just run and print.

---

## 🚀 Key Features

* 🧹 **Automated Printer Installation**: Installs multiple printers with minimal user action.
* 📂 **Custom Printer Preferences**: Automatically applies presets and settings for each printer.
* 🚀 **Compatibility**: Designed specifically for **macOS Sonoma** (Apple Silicon & Intel).
* 💼 **User-Friendly Interface**: One-click install experience via a simple GUI.

---

## 🚧 Requirements

* macOS Sonoma (M1 or Intel)
* Admin privileges (prompted automatically)
* Active connection (Wi-Fi or Ethernet) to the printer's network

---

## 🧰 What It Does

1. **Authenticates** user via GUI input
2. **Installs all required printer packages** via AppleScript (with admin rights)
3. **Adds multiple printers** with custom `lpadmin` configurations (including advanced options)
4. **Copies preset configuration files** to user preference folders
5. **Optionally deploys an uninstaller app & LaunchDaemon** (automated via `copy_uninstaller_app()` and `generate_a_plist()`)

---

## 📦 Packages Installed

| Printer | Package Path               | PPD Location                |
| ------- | -------------------------- | --------------------------- |
| Ysoft   | `../pkgs/Ysoft/Ysoft.pkg`  | —                           |
| Fiery   | `../pkgs/Fiery/fiery.pkg`  | `Pro C7200Sseries E-35A PS` |
| Color   | `../pkgs/Color/color.pkg`  | `RICOH IM C3000`            |
| Unique  | `../pkgs/Uniqe/unique.pkg` | `RICOH MP C4504`            |
| Black   | `../pkgs/Black/Black.pkg`  | `TOSHIBA_MonoMFP.gz`        |

---

## 🖥️ Sample Printers Created

Configured via `lpadmin` using `sqport://`:

* `Fiery`: `ColB` queue with multiple options (Binder, Finisher)
* `Color`: `ColS` with tray settings
* `Unique`: `Tos`
* `Black`: `BWS` with model and pedestal selections

---

## ⚙️ How to Use

1. Place all `.pkg` and `.ppd` files in their respective folders (`../pkgs/...`)
2. Launch the app:

```bash
python main.py
```

3. Enter the password when prompted (`1212` by default, can be changed in `main.py`)
4. Watch the GUI log and wait for completion

---

## 📁 Project Structure

```
Pistol-PrinterInstaller/
├── main.py
├── Data/
│   └── Data.py                # Contains pkg & printer configuration
├── Scripts/
│   ├── Installer/
│   │   └── tk_installer.py    # GUI + AppleScript-based installer
│   ├── Printers/
│   │   └── Create_printer_with_settings.py
│   ├── Presets/
│   │   └── Copy_Prst.py       # Copies presets to ~/Library/Preferences
│   └── Uninstaller/
│       ├── copy_uninstaller.py
│       └── Generate_plist.py
├── Tools/
│   └── tools.py
└── pkgs/
    ├── Ysoft/
    ├── Fiery/
    ├── Color/
    ├── Uniqe/
    ├── Black/
    └── Presets/
```

---

## 👨‍💼 Author

**Oren Ohayon 🌟**

Wishing you an awesome day — ✨Expect Miracles✨




   
