#!/usr/bin/node
function addMeMaybe (nb, func) {
  nb += 1;
  func(nb);
}

module.exports = { addMeMaybe };
