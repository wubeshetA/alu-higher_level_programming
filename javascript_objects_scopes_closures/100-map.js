#!/usr/bin/node
const list = require('./100-data').list;

const new_list = list.map((item, index) => item * index);
console.log(list);
console.log(new_list);
