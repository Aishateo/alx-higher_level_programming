#!/usr/bin/node
/* eslint-disable semi */
/* eslint-disable no-console */

class Rectangle {	
	constructor(w, h) {
		if (w <= 0 || h <= 0) {
			return {};
		}

		/* Initialize instance attributes
		 * only if w and h are positive integers
		 */
		this.width = w;
		this.height = h;
	}
}

module.exports = Rectangle;
