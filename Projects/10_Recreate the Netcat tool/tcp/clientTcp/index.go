package clientTcp

import (
    "fmt"
    "net"
    "os"
)

func Connect(host string) {
    conn, err := net.Dial("tcp", host)
    if err != nil {
        fmt.Println("Error connecting:", err)
        os.Exit(1)
    }
    
    defer conn.Close();
    text := ""
    fmt.Scanln(&text)
    conn.Write([]byte(text))
}