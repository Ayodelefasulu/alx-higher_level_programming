#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (!isNaN(size) && size > 0) {
  for (let i = 0; i < size; i++) {
    let line = '';
    for (let j = 0; j < size; j++) {
      line += 'X';
    }
    console.log(line);
  }
} else if (size < 0) {
  process.exit();
} else {
  console.log('Missing size');
}
