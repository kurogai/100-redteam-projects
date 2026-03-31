#!/bin/bash
# server.sh

# Clean up old files from previous runs
rm -f /tmp/connected_clients.txt
rm -f /tmp/client_*_fifo

PORT=6666
MESSAGE_FILE="messages.txt"

echo "Starting chat server on port $PORT..."
echo "Messages will be logged to $MESSAGE_FILE"
echo "Press Ctrl+C to stop server"

# Start server with socat
socat TCP-LISTEN:$PORT,fork,reuseaddr EXEC:./handle_client.sh
