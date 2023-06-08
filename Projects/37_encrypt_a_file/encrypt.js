const fs = require('fs');

function encryptFile(inputFile) {
    const data = fs.readFileSync(inputFile);
    const buffer = Buffer.from(data);
    const blockBuffer = Buffer.from("vicenteblock098876");

    //Create a buffer to store encrypted output
    const outputBuffer = Buffer.alloc(buffer.length);

    // XOR each byte of the input buffer with the password buffer
    for (let i = 0; i < buffer.length; i++) {
        outputBuffer[i] = buffer[i] ^ blockBuffer[i % blockBuffer.length];
    }

    fs.writeFileSync("encryptFile.vi", outputBuffer);
}

module.exports = encryptFile
