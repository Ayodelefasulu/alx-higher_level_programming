#!/usr/bin/node
const fs = require('fs');
const request = require('request');

// Function to get the contents of a webpage and store it in a file
function requestAndStore(url, filePath) {
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error(`Error: ${response.statusCode}`);
      return;
    }

    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(`The content has been successfully written to ${filePath}.`);
    });
  });
}

// Main execution
if (process.argv.length !== 4) {
  console.error('Usage: ./5-request_store.js <URL> <file_path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

requestAndStore(url, filePath);
