#!/bin/bash

default_server="localhost"

read -p "Enter the server address [$default_server]: " server_address

server_address=${server_address:-$default_server}

read -p "Enter the message: " message

echo "Sending message to $server_address..."
echo "$message" | nc $server_address 7777
