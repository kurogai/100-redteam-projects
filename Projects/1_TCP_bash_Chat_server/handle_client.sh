#!/bin/bash
# handle_client.sh
PID=$$
CLIENT_ID="client_$PID"
USERNAME=""
CLIENT_FIFO="/tmp/${CLIENT_ID}_fifo"

echo "Welcome! Your ID: $CLIENT_ID"
echo "Enter your username:"

# Read username
read -r USERNAME
echo "SYSTEM:Connected as $USERNAME"

# Create FIFO for this client
mkfifo "$CLIENT_FIFO" 2>/dev/null

# Process to listen for messages from other clients
(
    while IFS= read -r broadcast_msg < "$CLIENT_FIFO"; do
        echo "BROADCAST:$broadcast_msg"
    done
) &
BROADCAST_PID=$!

# Register this client in the connected clients list
echo "$CLIENT_ID:$USERNAME:$CLIENT_FIFO" >> /tmp/connected_clients.txt

# Main loop to process messages
while IFS= read -r line; do
    # Confirm to sender
    echo "CONFIRM:$line"

    # Save message
    echo "$(date): $USERNAME: $line" >> messages.txt

    # Broadcast to other clients
    while IFS=':' read -r other_client_id other_username other_fifo; do
        if [[ "$other_client_id" != "$CLIENT_ID" && -p "$other_fifo" ]]; then
            echo "$USERNAME: $line" > "$other_fifo" 2>/dev/null || true
        fi
    done < /tmp/connected_clients.txt
done

# Cleanup on disconnection
kill $BROADCAST_PID 2>/dev/null
rm -f "$CLIENT_FIFO"

# Remove this client from the list
grep -v "^$CLIENT_ID:" /tmp/connected_clients.txt > /tmp/connected_clients.tmp 2>/dev/null
mv /tmp/connected_clients.tmp /tmp/connected_clients.txt 2>/dev/null
