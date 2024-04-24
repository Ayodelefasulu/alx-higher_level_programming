#!/usr/bin/node
const fs = require('fs');

// Function to write a string to a file
function writeToFile(filePath, content) {
  fs.writeFile(filePath, content, 'utf8', (err) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log('The file has been successfully written.');
  });
}

// Main execution
if (process.argv.length !== 4) {
  console.error('Usage: ./1-writeme.js <file_path> <string_to_write>');
  process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];

writeToFile(filePath, content);
