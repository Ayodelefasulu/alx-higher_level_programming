#!/usr/bin/node
const fs = require('fs');

// Function to read and print the content of a file
function printFileContent(filePath) {
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
}

// Main execution
if (process.argv.length !== 3) {
  console.error('Usage: ./0-readme.js <file_path>');
  process.exit(1);
}

const filePath = process.argv[2];
printFileContent(filePath);
