import asyncdispatch
import asyncnet
import os
import strformat
import strutils

type
  Client = ref object
   socket: AsyncSocket
   netAddr: string
   id: int
   connected: bool

  Server = ref object
   socket: AsyncSocket
   clients: seq[Client]

if paramCount() < 1:
  quit("Specify Port, e.g. ./server port")

let port = paramStr(1)
echo &"[+] Server starting on Port {port}"

proc newServer(): Server = Server(socket: newAsyncSocket(), clients: @[])
proc `$`(client: Client): string =
  &"({$client.id}@{client.netAddr})"

proc processMessages(server: Server, client: Client) {.async.} =
  while true:
    let line = await client.socket.recvLine()
    if line.len == 0:
      echo(&"{client} disconnected!")
      client.connected = false
      client.socket.close()
      return
    echo(&"{client}$> {line}")

    for c in server.clients:
      if c.id!=client.id and c.connected:
        await c.socket.send(line & "\c\l")

proc loop(server: Server, port = port.parseInt) {.async.} =
  server.socket.bindAddr(port.Port)
  server.socket.listen()

  while true:
    let (netAddr, clientSocket) = await server.socket.acceptAddr()
    echo(&"[+] Accepted Connection From: {netAddr}")
    let client = Client(
      socket: clientSocket,
      netAddr: netAddr,
      id: server.clients.len,
      connected: true
    )
    server.clients.add(client)
    asyncCheck processMessages(server, client)

var server = newServer()
waitFor loop(server)
