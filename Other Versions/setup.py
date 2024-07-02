from setuptools import setup
import os

# Define your main script
APP = ['Scripts/main.py']

# Define your data files
DATA_FILES = [
    ('Resources/pkgs/Black', [
        os.path.join('../../pkgs/Black', 'Black.pkg')
    ]),
    ('Resources/pkgs/Color', [
        os.path.join('../../pkgs/Color', 'color.pkg')
    ]),
    ('Resources/pkgs/Fiery', [
        os.path.join('../../pkgs/Fiery', 'fiery.pkg')
    ]),
    ('Resources/pkgs/Uniqe', [
        os.path.join('../../pkgs/Uniqe', 'unique.pkg')
    ]),
    ('Resources/pkgs/Ysoft', [
        os.path.join('../../pkgs/Ysoft', 'Ysoft.pkg')
    ]),
    # Include all files in the Presets directory
    ('Resources/pkgs/Presets', [
        os.path.join('../../pkgs/Presets', filename) for filename in os.listdir('../../pkgs/Presets')
    ])
]

# Define the options
OPTIONS = {
    # 'argv_emulation': True,
    'packages': [],  # Add any additional packages your script uses
    # 'iconfile': 'my_icon.icns',  # Uncomment and use if you have an icon file
}

# Setup configuration
setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    install_requires=[
        'altgraph==0.17.4',
        'macholib==1.16.3',
        'modulegraph==0.19.6',
        'packaging==24.0',
        'pipdeptree==2.22.0',
        'platformdirs==4.2.2',
        'py2app==0.28.8',
        'setuptools==70.0.0',
        'typing_extensions==4.12.1'
    ],
)
