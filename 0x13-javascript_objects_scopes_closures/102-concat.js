#!/usr/bin/node
/* eslint-disable semi */
/* eslint-disable no-unused-vars */

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const destinationFile = process.argv[4];

// Read content from fileA
const contentA = fs.readFileSync(fileA, 'utf-8');

// Read content from fileB
const contentB = fs.readFileSync(fileB, 'utf-8');

// Concatenate contents of fileA and fileB
const concatenatedContent = contentA + contentB;

// Write concatenated content to destination file
fs.writeFileSync(destinationFile, concatenatedContent);

console.log('Concatenation successful!');
