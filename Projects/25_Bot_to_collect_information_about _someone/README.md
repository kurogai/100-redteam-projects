# Bot to Collect Information about Someone using Google / Bing / Yahoo!

This code is a bot that uses Puppeteer to collect information about someone from multiple search engines, including Google, Bing, and Yahoo!. It performs a search using a specified search term, retrieves the search results, and saves them to separate files.

## Prerequisites

Before running the code, make sure you have the following dependencies installed:

- Node.js
- Puppeteer
- `fs` module (built-in)
- `util` module (built-in)
- Nodemon (optional, for automatic script restart)

## Installation

To install the required dependencies, run the following command in your project directory:

```
npm install
```

## Usage

1. Modify the search functions `searchGoogle`, `searchBing`, and `searchYahoo` to use Puppeteer and perform the search for the given search term. These functions should return an array of search results.

2. Replace the placeholders `searchGoogle`, `searchBing`, and `searchYahoo` in the code with your actual implementations of the search functions.

3. Run the code using one of the following commands:

```
npm start
```
or
```
nodemon index.js
```

If you choose to use `npm start`, make sure you have the following script defined in your `package.json` file:

```json
"scripts": {
  "start": "node index.js"
}
```

4. The code will execute the search functions for each search engine, retrieve the search results, and log the titles and links to the console.

5. Additionally, the search results will be saved to separate files: `peopleInformation_google.txt`, `peopleInformation_bing.txt`, and `peopleInformation_yahoo.txt`.

## Output

The code will log the following information to the console:

- Titles and links of the search results from Google.
- Titles and links of the search results from Bing.
- Titles and links of the search results from Yahoo.

The search results will also be saved to separate JSON files: `peopleInformation_google.txt`, `peopleInformation_bing.txt`, and `peopleInformation_yahoo.txt`.

Note: You can modify the search term and file names as per your requirements.

## Troubleshooting

If you encounter any issues while running the code, please ensure that:

- Puppeteer is properly installed and configured.
- The search functions (`searchGoogle`, `searchBing`, `searchYahoo`) are implemented correctly and return the expected results.
- The file write permissions are set correctly for the directory where the code is executed.
- The required dependencies (`fs`, `util`, `nodemon`) are installed.

If you have any further questions or need assistance, please don't hesitate to ask.
