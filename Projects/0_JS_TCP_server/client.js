const colors = require('colors');
const net = require('net');
const prompt = require('prompt-sync')();

let client = null;

const menuReturn = () => {
    return setTimeout(() => menu(), 1500);
};

const createConnection = () => {
    if (!client) {
        const ADRESS = prompt('Type server adress: ') || '127.0.0.1'
        const PORT = prompt('Type server port: ') || 8000;

        client = new net.Socket();

        client.connect(PORT, ADRESS, () => {
            console.log(`Connected to ${ADRESS}:${PORT}`.bold.green);
        });

        client.on('error', (err) => {
            console.log(`${err}`.bold.red);
            client = null;
            menuReturn();
        })

    } else console.log('You are alredy connected! End connection before new one!'.bold.red);

};

const destroyConnection = () => {
    if (client) {
        client.destroy();
        client = null;
    } else return;
};

const quitProgr = () => {
    if (client) {
        destroyConnection()
    }
    console.log('See you soon!'.rainbow);
};

const sendMessage = () => {
    if (client) {
        const message = prompt('Message to send: ');
        client.write(message);
        client.on('data', (data) => {
            console.log(`Message from server: ${data.toString()}`);
        })
        menuReturn();
    }
    else {
        console.log('First connect to server!'.bold.red);
        menuReturn();
    }
}

const menu = () => {
    console.log(`${client ? 'CONNECTED'.bold.green : 'NOT CONNECTED'.bold.red}`);
    console.log('(c)onnect, (s)end message, (d)isconnect, (q)uit'.bold.white)
    const choose = prompt('Type option: '.bold.white);

    switch (choose) {
        case 'c':
            createConnection();
            menuReturn();
            break;
        case 's':
            sendMessage();
            break;
        case 'd':
            destroyConnection();
            menuReturn();
            break;
        case 'q':
            quitProgr();
            return;
        default:
            menuReturn();
            break;
    }
};

menu();