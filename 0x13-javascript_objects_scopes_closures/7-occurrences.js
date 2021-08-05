#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let numberOcurr = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      numberOcurr += 1;
    }
  }
  return numberOcurr;
};
