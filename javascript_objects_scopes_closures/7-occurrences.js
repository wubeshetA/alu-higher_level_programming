#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let ocurrences = 0;
  list.forEach(element => {
    if (element === searchElement) { ocurrences++; }
  });
  return ocurrences;
};
