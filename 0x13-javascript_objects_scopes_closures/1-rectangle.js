#!/usr/bin/node
const {argv}=require('node:process');

module.exports = class Rectangle {
	constructor(w, h){
		this.width = w;
		this.height = h;
	}
}
