#!/usr/bin/node
/* Script gets the content of a webpage and stores it in a file */
const req = require("request");
const fs = require("fs");

const url = process.argv[2];
const filePath = process.argv[3];

req.get(url, (err, response, body) => {
	if (err) {
		console.error(err);
		return;
	}

	if (response.statusCode === 200) {
		fs.writeFile(filePath, body, "utf-8", (err) => {
			if (err) {
				console.error(err);
				return;
			}
		});
	}
});
