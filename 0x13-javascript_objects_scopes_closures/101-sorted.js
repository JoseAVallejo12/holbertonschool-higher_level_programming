#!/usr/bin/node
/* script that imports a dictionary of occurrences
by user id and computes a dictionary of user ids by occurrence. */
const { dict } = require('./101-data');
values = Object.values(dict).reduce((val)=> val in values)
keys = Object.keys(dict)
console.log(values)

/* list = [];
for (const key in Object.keys(dict)) {
    newObj[key] = Object.values(dict).map((val) => val == dict[key] )
};
console.log(newObj) */