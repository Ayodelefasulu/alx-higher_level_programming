#!/usr/bin/node
const request = require('request');

// Function to display the status code of a GET request
function displayStatusCode(url) {
  request(url, (error, response) => {
    if (error) {
      console.error(error);
      return;
    }
    console.log('code:', response.statusCode);
  });
}

// Main execution
if (process.argv.length !== 3) {
  console.error('Usage: ./2-statuscode.js <URL>');
  process.exit(1);
}

const url = process.argv[2];
displayStatusCode(url);
