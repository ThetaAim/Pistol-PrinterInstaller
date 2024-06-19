#!/bin/bash
cd "$(dirname "$0")" || exit
# Function to check if a file exists
file_exists() {
    if [ -f "$1" ]; then
        return 0  # File exists
    else
        return 1  # File does not exist
    fi
}

# Check and install Ysoft package
if file_exists "/tmp/Ysoft.pkg"; then
    installer -pkg "/tmp/Ysoft.pkg" -target /
fi

# Check and install fiery package
if file_exists "/tmp/fiery.pkg"; then
    installer -pkg "/tmp/fiery.pkg" -target /
fi

# Check and install Color package
if file_exists "/tmp/color.pkg"; then
    installer -pkg "/tmp/color.pkg" -target /
fi

# Check and install Unique package
if file_exists "/tmp/unique.pkg"; then
    installer -pkg "/tmp/unique.pkg" -target /
fi

# Check and install Black package
if file_exists "/tmp/Black.pkg"; then
    installer -pkg "/tmp/Black.pkg" -target /
fi

