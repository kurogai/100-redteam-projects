package serverTcp

import (
    "fmt"
    "net"
    "os"
)


func StartServer(host string) {
    ln, err := net.Listen("tcp", host)

 
    if err != nil {
        fmt.Println("Error listening:", err)
        os.Exit(1)
    }
    
    defer ln.Close()

    conn, err := ln.Accept()
    if err != nil {
        fmt.Println("Error accepting connection:", err)
    }
    defer conn.Close()

    buffer := make([]byte, 1024)
    n, err := conn.Read(buffer)
    if err != nil {
        fmt.Println("Error reading:", err)
    }

    fmt.Printf("%s\n",buffer[:n])
}

func Start(port string){
    StartServer(port)
}   