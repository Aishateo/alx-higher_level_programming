#!/usr/bin/node
/* eslint-disable semi */
/* eslint-disable no-console */

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0) {
      // If w or h is not a positive integer, create an empty object
      return Rectangle.createEmpty();
    }

    // Initialize instance attributes only if w and h are positive integers
    this.width = w;
    this.height = h;
  }

  // Static method to create an empty object
  static createEmpty() {
    return {};
  }
}

module.exports = Rectangle;
