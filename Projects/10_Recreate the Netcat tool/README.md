#	Recreate the Netcat tool

## TCP Connection as Client and Server:

### To start a TCP server listening on a specific port (e.g., port 12345), you can use the following command:
  
  ```bash
    ./main -l -p :12345 or ./main -l -p 127.0.0.1:12345
```

##  To connect to this server as a client:
  ```bash
  ./main 127.0.0.1 :12345
```

# Data Transmission:

**You can use netcat to send data from one terminal to another. For example, to send a message from one terminal to another:**

### Terminal 1 (receiving data):

 ```bash
  ./main  -l -p :12345
```

### Terminal 2 (sending data):
```bash
  echo "Hello, world!" | ./main localhost :12345
```

# File Transfer:

**You can use netcat to transfer files from one computer to another. In one terminal (as the server):**

```bash
  ./main -l -p :12345 > received_file.txt
```

### In another terminal (as the client), you can send a file to the server:

```bash
 ./main  localhost :12345 < file_to_send.txt
```


# Port Scanner:

**To check if a specific port is open on a host:**

  ```bash
    ./main -zv host_or_ip port
```

# UDP Connection:

**Netcat can be used for UDP connections in the same way as TCP connections. For example, to start a UDP server:**

```bash
  ./main -lu -p :12345
```

## To send UDP data to the server:
 ```bash
 echo "Hello, UDP!" | ./main -u -w1 :12345
```
