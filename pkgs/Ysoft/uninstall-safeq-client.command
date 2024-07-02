#!/bin/bash

if [[ "$(whoami)" != "root" ]]; then
    sudo bash "$0"
    exit $?
fi

pkill -f "/Applications/SafeQClient"
pkill -f "/Applications/YSoft SafeQ Client"

# Ignore shared library
#rm -f /usr/lib/libzmq.3.dylib

rm -rf /Applications/SafeQClient.app "/Applications/YSoft SafeQ Client.app"
rm -rf /usr/libexec/cups/backend/sqport
rm -rf /Library/PreferencePanes/ClientPreferences.prefPane
rm -rf "/Library/Application\ Support/YSoft"

# Stop and remove daemons
launchctl remove com.ysoft.service.CUPS
launchctl remove com.ysoft.service.DHCPOption
rm -rf /Library/LaunchDaemons/com.ysoft.service.CUPS.plist
rm -rf /Library/LaunchDaemons/com.ysoft.service.DHCPOption.plist

# Stop and remove launch agent
launchctl asuser "$(stat -f%u /dev/console)" sudo -u "$(id -un "$(stat -f%u /dev/console)")" launchctl remove com.ysoft.client.agent
rm -rf /Library/LaunchAgents/com.ysoft.client.agent.plist

# remove package receipts
pkgutil --forget com.ysoft.safeq.client

CUPS_CONFIG="/etc/cups/cups-files.conf"

function deactivateRelaxedSandbox() 
{
    # Stop CUPS
    launchctl stop org.cups.cupsd

    sed -i -e 's/Sandboxing Relaxed//g' "${CUPS_CONFIG}"
    # Start CUPS
    launchctl start org.cups.cupsd
}

deactivateRelaxedSandbox 