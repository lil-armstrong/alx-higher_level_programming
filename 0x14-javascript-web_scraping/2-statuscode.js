#!/usr/bin/node

/* Script displays the status code of a `GET` request */
const request = require("request");
const url = process.argv[2];
request.get(url, (err, response) => {
	if (err) {
		console.error(err);
		return;
	}
	console.log(`code: ${response && response.statusCode}`);
});
