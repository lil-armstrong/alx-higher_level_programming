#!/usr/bin/node
const Rect = rrquire('./4-rextangle');
module.exports = class Square extends Rect{
	constructor(size){
		this.super(size, size);
	}
}
