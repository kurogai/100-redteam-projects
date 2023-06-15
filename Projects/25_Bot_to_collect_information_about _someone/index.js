const fs = require('fs');
const util = require('util');
const writeFile = util.promisify(fs.writeFile);

const searchGoogle = require('./googleSearch');
const searchBing = require('./bingSearch');
const searchYahoo = require('./yahooSearch');
const searchTerm = 'heber julio';

(async () => {
  try {
    const googleResults = await searchGoogle(searchTerm);
    const bingResults = await searchBing(searchTerm);
    const yahooResults = await searchYahoo(searchTerm);

    console.log('Response of the Google:');
    console.log('------------------');
    console.log('------------------');
    for (let result of googleResults) {
      console.log('Title:', result.title);
      console.log('Link:', result.link);
    }


    console.log('------------------');
    console.log('------------------');
    console.log('------------------');
    console.log('------------------');
    console.log('------------------');


    await writeFile('peopleInformation_google.txt', JSON.stringify(googleResults));

    console.log('Response of the Bing:');
    console.log('------------------');
    console.log('------------------');

    for (let result of bingResults) {
      console.log('Title:', result.title);
      console.log('Link:', result.link);
    }


    console.log('------------------');
    console.log('------------------');
    console.log('------------------');
    console.log('------------------');
    console.log('------------------');
    
    await writeFile('peopleInformation_bing.txt', JSON.stringify(bingResults));

    console.log('Response of the Yahoo:');
    console.log('------------------');
    console.log('------------------');

    for (let result of yahooResults) {
      console.log('Title:', result.title);
      console.log('Link:', result.link);
      console.log('------------------');
    }
    await writeFile('peopleInformation_yahoo.txt', JSON.stringify(yahooResults));
  } catch (error) {
    console.error('wrong in :', error);
  }
})();
