const net = require('net');
const colors = require('colors');
server = net.createServer();

server.on('connection', (s) => {
    const remoteAddress = s.remoteAddress + ':' + s.remotePort;
    console.log(`client connected ${remoteAddress}`.green);

    s.on('data', (data) => {
        console.log(`From ${remoteAddress} - ${data}`.yellow)
        s.write(`Message from server!`);
    });

    s.on('close', () => {
        console.log(`Client ${remoteAddress} disconnected`.white);
    })

    s.on('error', (err) => {
        console.log(`${remoteAddress} error: ${err.message}`.red);
    })
});


server.listen(8000, () => {
    console.log('Server on...')
});