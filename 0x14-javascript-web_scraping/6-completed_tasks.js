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
		const users_with_completed_tasks = {};

		obj.forEach((task) => {
			if (task.completed) {
				if (task.userId in users_with_completed_tasks) {
					users_with_completed_tasks[task.userId]++;
				} else {
					users_with_completed_tasks[task.userId] = 1;
				}
			}
		});

		console.log(users_with_completed_tasks);
		return;
	}

	console.error(`Error code: ${response.statusCode}`);
});
