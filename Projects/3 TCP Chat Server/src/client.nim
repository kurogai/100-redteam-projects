import os
import strformat
import strutils
import threadpool
import asyncdispatch
import asyncnet
import protocol

if paramCount() < 3:

  quit("Specify Server Address and Port, e.g. ./client localhost port username")

let serverAddr = paramStr(1)
let port = paramStr(2)
let username = paramStr(3)
var socket = newAsyncSocket()

proc connect(socket: AsyncSocket, serverAddr: string) {.async.} =
  echo(&"[*] Connecting to {serverAddr}")
  await socket.connect(serverAddr, port.parseInt.Port)
  echo("[+] Connected!")
  while true:
    let line = await socket.recvLine()
    let parsed = parseMessage(line)
    echo(&"{parsed.username}$> {parsed.message}")

asyncCheck connect(socket, serverAddr) 
var messageFlowVar = spawn stdin.readLine()
while true:
  if messageFlowVar.isReady():
    asyncCheck socket.send(createMessage(username, ^messageFlowVar))
    messageFlowVar = spawn stdin.readLine()
  asyncdispatch.poll()