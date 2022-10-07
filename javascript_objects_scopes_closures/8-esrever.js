#!/usr/bin/node
exports.esrever = function (list) {
  const result = [];
  let i = list.length - 1;
  for (i; i > 0; i--) {
    result.push(list[i]);
  }
  return result;
};
