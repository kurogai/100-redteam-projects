#!/bin/bash

detect_os() {
    local os_type=""
    local os_info=""

    case "$(uname -s)" in
        Linux*)
            os_type="Linux"
            if [ -f /etc/os-release ]; then
                . /etc/os-release
                os_info="$NAME $VERSION"
            fi
            ;;
        Darwin*)
            os_type="macOS"
            os_info=$(sw_vers -productVersion)
            ;;
        CYGWIN*|MINGW32*|MSYS*|MINGW*)
            os_type="Windows"
            ;;
        *)
            os_type="Unknown"
            os_info="$(uname -s)"
            ;;
    esac

    export DETECTED_OS="$os_type"
    export OS_INFO="$os_info"

    echo "$os_type"
}

get_os_details() {
    detect_os > /dev/null
    echo "OS: $DETECTED_OS"
    if [ -n "$OS_INFO" ]; then
        echo "Info: $OS_INFO"
    fi
}
