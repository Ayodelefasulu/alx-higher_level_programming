#!/usr/bin/node
const request = require('request');

// Function to compute the number of completed tasks by user ID
function completedTasksByUser(url) {
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error(`Error: ${response.statusCode}`);
      return;
    }

    const todos = JSON.parse(body);
    const completedTasks = {};

    todos.forEach(todo => {
      if (todo.completed) {
        if (completedTasks[todo.userId]) {
          completedTasks[todo.userId]++;
        } else {
          completedTasks[todo.userId] = 1;
        }
      }
    });

    console.log(completedTasks);
  });
}

// Main execution
if (process.argv.length !== 3) {
  console.error('Usage: ./6-completed_tasks.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];
completedTasksByUser(apiUrl);
