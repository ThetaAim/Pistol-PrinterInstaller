import os
import sys

def disable_event():
    pass


def find_base_dir():
    # Determine the base directory
    if hasattr(sys, '_MEIPASS'):
        base_dir = os.path.join(sys._MEIPASS, 'Resources')
        return base_dir
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        return base_dir



