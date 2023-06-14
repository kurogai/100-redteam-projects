const puppeteer = require('puppeteer');

async function searchGoogle(query) {
  const googleBrowser = await puppeteer.launch({ headless: "new" });
  const googlePage = await googleBrowser.newPage();
  googlePage.setDefaultNavigationTimeout(60000);
  await googlePage.goto(`https://www.google.com/search?q=${query}`);

  // Please wait for the search results from Google to load.
  await googlePage.waitForSelector('#search');

  // extract the titles and links from the google search results,
  const googleResults = await googlePage.evaluate(() => {
    const resultElements = document.querySelectorAll('.g');
    const results = [];
    for (let element of resultElements) {
      const titleElement = element.querySelector('h3');
      const linkElement = element.querySelector('a');
    
      const title = titleElement ? titleElement.innerText : '';
      const link = linkElement ? linkElement.href : '';
      results.push({ title, link });
    }
    return results;
  });

  //await googleBrowser.close();

  return googleResults;
}

module.exports = searchGoogle;
