#!/bin/bash
# client.sh
SERVER="localhost"
PORT=6666
USERNAME=""

# Cleanup function
cleanup() {
    kill $READER_PID 2>/dev/null
    exec 3>&- 2>/dev/null
    echo
    echo "Disconnected from chat."
    exit 0
}

# Trap for clean exit
trap cleanup EXIT INT TERM

# Open connection
exec 3<>/dev/tcp/$SERVER/$PORT

# Ask for username at the beginning
read -p "Enter your username: " USERNAME
echo "$USERNAME" >&3

echo "=== Chat connected ==="
echo "Type your messages and press Enter"
echo "Ctrl+C to quit"
echo

# Background process for reading
(
    while IFS= read -r message <&3; do
        if [[ $message == "BROADCAST:"* ]]; then
            # Message from another client
            user_msg=${message#BROADCAST:}
            echo "$user_msg"
        elif [[ $message == "CONFIRM:"* ]]; then
            # Confirmation of our own message
            our_msg=${message#CONFIRM:}
            echo "You: $our_msg"
        elif [[ $message == "SYSTEM:"* ]]; then
            # System messages
            system_msg=${message#SYSTEM:}
            echo "[SYSTEM] $system_msg"
        else
            # Other messages (welcome, etc.)
            echo "[SYSTEM] $message"
        fi
    done
) &
READER_PID=$!

# Main loop for writing WITHOUT hiding input
while IFS= read -r input; do
    if [[ -n "$input" ]]; then
        # Clear the line we just typed
        printf "\033[1A\033[2K"

        # Send to server
        echo "$input" >&3
    fi
done
