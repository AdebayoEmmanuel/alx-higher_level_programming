#!/usr/bin/node

if (parseInt(process.argv[2])) {
  for (let i = 0; i <= process.argv[2] - 1; i++) {
    console.log('x'.repeat(process.argv[2]));
  }
} else {
  console.log('Missing size');
}
