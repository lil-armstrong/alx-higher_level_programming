#!/usr/bin/node
const req = require("request");

const url = process.argv[2];

req.get(url, (err, response) => {
	if (err) {
		console.error(err);
		return;
	}
	if (response.statusCode === 200) {
		const obj = JSON.parse(response?.body);
		const completed = {};

		obj.forEach((task) => {
			if (task.completed) {
				if (task.userId in completed) {
					completed[task.userId]++;
				} else {
					completed[task.userId] = 1;
				}
			}
		});

		console.log(completed);
		return;
	}

	console.error(`Error code: ${response.statusCode}`);
});
