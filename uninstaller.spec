# -*- mode: python ; coding: utf-8 -*-
import os

block_cipher = None

a = Analysis(
    ['Scripts/Uninstaller/remover.py'],
    pathex=['/Users/administrator/Desktop/Pistol'],
    binaries=[],
    datas=[
#        ('pkgs', 'Resources/pkgs'),  # Include the pkgs directory
        ('Scripts/Installer', 'Installer'),  # Include the Installer directory
        ('Scripts/Presets', 'Presets'),  # Include the Presets directory
        ('Scripts/Printers', 'Printers'),  # Include the Printers directory
        ('Scripts/Uninstaller', 'Uninstaller'),  # Include the Uninstaller directory
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)

app = BUNDLE(
    coll,
    name='main.app',
    icon=None,
    bundle_identifier='com.yourcompany.main',
)
