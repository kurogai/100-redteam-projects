package scannerPorts


import (
    "fmt"
    "strconv"
    "strings"
    "net"
)


func Ports(host,interval string){

	// String representando o intervalo
    intervalStr := interval

    // Dividir a string nos hífens
    parts := strings.Split(intervalStr, "-")
    if len(parts) != 2 {
        fmt.Println("Intervalo inválido")
        return
    }

    // Converter as partes em números inteiros
    start, err := strconv.Atoi(parts[0])
    if err != nil {
        fmt.Println("Erro ao converter o início do intervalo:", err)
        return
    }

    end, err := strconv.Atoi(parts[1])
    if err != nil {
        fmt.Println("Erro ao converter o final do intervalo:", err)
        return
    }

    // Usar um loop for para contar de start até end
    for i := start; i <= end; i++ {
        ip := host
        address := fmt.Sprintf("%s:%d", ip, i)

        conn, err := net.Dial("tcp", address)
        if err != nil {
            fmt.Printf("The port %d is closed \n", i)
        } else {
            defer conn.Close()
            fmt.Printf("The port %d is open\n", i)
        }
    }
}