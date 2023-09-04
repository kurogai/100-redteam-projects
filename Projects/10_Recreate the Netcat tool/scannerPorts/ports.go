package scannerPorts

import (
    "fmt"
    "strconv"
    "strings"
    "net"
)

func Ports(host, interval string) {
    // String representing the range
    intervalStr := interval

    // Split the string at hyphens
    parts := strings.Split(intervalStr, "-")
    if len(parts) != 2 {
        fmt.Println("Invalid interval")
        return
    }

    // Convert the parts into integers
    start, err := strconv.Atoi(parts[0])
    if err != nil {
        fmt.Println("Error converting the start of the interval:", err)
        return
    }

    end, err := strconv.Atoi(parts[1])
    if err != nil {
        fmt.Println("Error converting the end of the interval:", err)
        return
    }

    // Use a for loop to iterate from start to end
    for i := start; i <= end; i++ {
        ip := host
        address := fmt.Sprintf("%s:%d", ip, i)

        conn, err := net.Dial("tcp", address)
        if err != nil {
            fmt.Printf("Port %d is closed\n", i)
        } else {
            defer conn.Close()
            fmt.Printf("Port %d is open\n", i)
        }
    }
}
