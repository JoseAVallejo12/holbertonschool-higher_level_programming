#!/usr/bin/node
/* Function that returns the reversed version of a list: */
exports.esrever = function (list) {
  const listNew = [];
  for (let i = list.length - 1; i >= 0; i--) {
    listNew.push(list[i]);
  }
  return listNew;
};
