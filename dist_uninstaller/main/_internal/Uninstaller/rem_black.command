#!/bin/sh

if ! pkgutil --pkg-info "${INSTALL_PKG_SESSION_ID}" >/dev/null; then
	exit 0
fi

# Get a list of all files and delete them. If FILE refers to a directory
# then only delete it if it is a bundle, otherwise leave it for the second
# part of the script
IFS='
'
for FILE in $(pkgutil --files "${INSTALL_PKG_SESSION_ID}"); do
	if [ -z "${FILE}" ]; then
		echo "Error: filename blank"
	elif [ -f "/${FILE}" ]; then
		rm "/${FILE}"
	elif [ -d "/${FILE}" ]; then
		FILETYPE=$(mdls -name kMDItemContentTypeTree "/${FILE}" | fgrep -o com.apple.bundle)
		if [ "${FILETYPE}" == "com.apple.bundle" ]; then
			rm -r "/${FILE}"
		fi
	fi
	if [ "$?" -ne "0" ]; then
		echo "Error removing /${FILE}"
	fi
done

# remove directories (only if they are now empty)
for DIR in $(pkgutil --only-dirs --files "${INSTALL_PKG_SESSION_ID}" | tail -r); do
	rmdir /${DIR} >/dev/null 2>&1
	if [ "$?" -ne "0" ]; then
		echo "Not empty: /${DIR}"
	fi
done
