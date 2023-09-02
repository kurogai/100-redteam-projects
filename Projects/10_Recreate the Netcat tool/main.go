// main.go
package main

import (
    "os"
    "fmt"
    "go/tcp/serverTcp"
    "go/tcp/clientTcp"
    "go/udp/serverUdp"
    "go/udp/clientUdp"
    "go/scannerPorts"
)


func main() {

    if len(os.Args) == 2 && os.Args[1] == "-l" {
        fmt.Println("Ncat: Failed to resolve default IPv4 address: Name or service not known. QUITTING.")    
    }else if len(os.Args) == 3 && os.Args[1] == "-l" && os.Args[2] == "-p" {
        fmt.Println("Ncat: option requires an argument -- 'p' ")
    }else if len(os.Args) == 4 && os.Args[1] == "-l" && os.Args[2] == "-p" {
        serverTcp.Start(os.Args[3]) 
    }else if len(os.Args) == 2 {
        clientTcp.Connect(os.Args[1])    
    }else  if len(os.Args) == 2 && os.Args[1] == "-lu" {
        fmt.Println("Ncat: Failed to resolve default IPv4 address: Name or service not known. QUITTING.")    
    }else if len(os.Args) == 3 && os.Args[1] == "-lu" && os.Args[2] == "-p" {
        fmt.Println("Ncat: option requires an argument -- 'p' ")
    }else if len(os.Args) == 4 && os.Args[1] == "-lu" && os.Args[2] == "-p" {
        serverUdp.Start(os.Args[3]) 
    }else if len(os.Args) == 4 && os.Args[1] == "-u" && os.Args[2] == "-w1" {
        clientUdp.Connect(os.Args[3])  
    }else if len(os.Args) == 4 && os.Args[1] == "-vz" {
        scannerPorts.Ports(os.Args[2],os.Args[3]);
    }
}