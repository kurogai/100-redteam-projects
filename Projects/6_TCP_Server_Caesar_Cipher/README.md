# TCP Server with Caesar Cipher Encryption

## Credits
This TCP server implementation is done by [AugustoSavi](https://github.com/AugustoSavi)

## How to use?
```bash
# Clone the repository
$ git clone https://github.com/kurogai/100-redteam-projects

# Enter the repository
$ cd 100-redteam-projects/Projects/1_TCP_chat_server

# Open a terminal and run
$ python3 TCPserver.py 127.0.0.1 5555 

# Client: Alice
# Open a new terminal and run
$ python3 TCPclient.py 127.0.0.1 5555 2

# Client: Bob
# Open a new terminal and run
$ python3 TCPclient.py 127.0.0.1 5555 2

# Client: Carl
# Open a new terminal and run
$ python3 TCPclient.py 127.0.0.1 5555 3
```

Only Alice and Bob can read each other messages in plaintext, because they share the same key. Since Carl's key is different, Carl can only see Alice and Bob's ciphertext messages.

The other way holds true: Alice and Bob cannot read Carl's plaintext message.

But, if Carl is hardworking, Carl only needs to decode Alice and Bob's messages with 25 key combinations in the worst case. This is why Caesar cipher is rarely used nowadays.

## Further Reading
[End-to-end Encryption](https://www.ibm.com/topics/end-to-end-encryption)