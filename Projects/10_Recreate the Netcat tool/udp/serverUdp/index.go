package serverUdp

import (
    "fmt"
    "net"
    "os"
)

func StartServer(host string){
    addr, err := net.ResolveUDPAddr("udp", host)
    if err != nil {
        fmt.Println("Error resolving address:", err)
        os.Exit(1)
    }

    conn, err := net.ListenUDP("udp", addr)
    if err != nil {
        fmt.Println("Error listening:", err)
        os.Exit(1)
    }
    defer conn.Close()

    buffer := make([]byte, 1024)
    n, addr, err := conn.ReadFromUDP(buffer)
    if err != nil {
        fmt.Println("Error reading:", err)
        return
    }

    fmt.Printf("%s\n", buffer[:n])
}

func Start(host string) {
    StartServer(host)
}