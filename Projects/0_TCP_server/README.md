# TCP server just to receive messages
>This simple TCP server receives messages and echoes them back to the client. The client program sets up its socket differently from the way a server does. Instead of binding to a port and listening, it uses connect() to attach the socket directly to the remote address.

NOTE: Make sure that the terminals running the scripts are separate


![alt text](https://github.com/alisimran/100-redteam-projects/blob/master/Projects/0_TCP_server/tcpserver.png)

## :information_source:  technologies used

* Python

## :information_source: How to use?

```bash
# Clone the repository
$ git clone https://github.com/kurogai/100-redteam-projects

# Enter the repository
$ cd 100-redteam-projects/0_TCP_server

# Open a terminal and run
python ./server.py

# Open another terminal and run
python ./client.py
```

## :books: References 
    https://pymotw.com/2/socket/tcp.html

## Developer
    https://github.com/alisimran
