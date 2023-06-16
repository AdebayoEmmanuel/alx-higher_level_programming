#!/usr/bin/node
const list = require('./100-data').list;
let mappedVal = list.map((x) => x * list.indexOf(x));
console.log(JSON.stringify(list));
console.log(JSON.stringify(mappedVal));