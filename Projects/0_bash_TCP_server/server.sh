#!/bin/bash
source detect_os.sh

detect_os > /dev/null
echo "OS détecté : $DETECTED_OS"


if [ "$DETECTED_OS" = "Linux" ]; then
    echo "Starting server on Linux..."
    nc -l -p 7777
elif [ "$DETECTED_OS" = "macOS" ]; then
    echo "Starting server on macOS..."
    nc -l 7777
elif [ "$DETECTED_OS" = "Windows" ]; then
    echo "Starting server on Windows..."
    # Test multiple syntaxes
    if command -v ncat >/dev/null 2>&1; then
        ncat -l 7777
    elif command -v nc >/dev/null 2>&1; then
        # Test both possible syntaxes
        nc -l 7777 2>/dev/null || nc -l -p 7777
    else
        echo "Netcat not found. Installation required."
        echo "Install with: choco install netcat or download ncat"
    fi
else
    echo "Unsupported OS: $DETECTED_OS"
fi
