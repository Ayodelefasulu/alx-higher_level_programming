#!/usr/bin/node

const x = parseInt(process.argv[2]);

if (!isNaN(x) && x > 0) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else if (x < 0) {
  process.exit();
} else {
  console.log('Missing number of occurrences');
}
