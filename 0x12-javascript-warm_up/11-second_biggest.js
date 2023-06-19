#!/usr/bin/node
const numbers = process.argv.slice(2).map(Number);

function findSecondBiggest(arr) {
  if (arr.length <= 1)
    return 0;
  let max = Math.max(...arr);
  arr = arr.filter(num => num !== max);
  return Math.max(...arr);
}

console.log(findSecondBiggest(numbers));
