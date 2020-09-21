#!/usr/bin/node
/* Write a function that returns the number of occurrences in a list */
exports.nbOccurences = function (list, searchElemnt) {
  return list.filter((val) => val === searchElemnt).length;
};
