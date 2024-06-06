# from setuptools import setup
#
# APP = ['Scripts/main.py']
# DATA_FILES = []
# OPTIONS = {
#     'includes': ['Scripts'],
#     'resources': ['pkgs']
# }
#
# setup(
#     app=APP,
#     data_files=DATA_FILES,
#     options={'py2app': OPTIONS},
#     setup_requires=['py2app'],
#     install_requires=[
#         'altgraph==0.17.4',
#         'macholib==1.16.3',
#         'modulegraph==0.19.6',
#         'packaging==24.0',
#         'pipdeptree==2.22.0',
#         'platformdirs==4.2.2',
#         'py2app==0.28.8',
#         'typing_extensions==4.12.1',
#     ],
# )
from setuptools import setup

APP = ['Scripts/main.py']
DATA_FILES = []
OPTIONS = {
    'includes': ['Scripts'],
    'resources': ['pkgs'],
    # 'argv_emulation': True,
    'plist': {
        'LSArchitecturePriority': ['x86_64', 'arm64'],
    },
    'arch': 'universal2'
}

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
        'typing_extensions==4.12.1',
    ],
)
