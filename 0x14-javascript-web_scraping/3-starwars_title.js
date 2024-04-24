#!/usr/bin/node
const request = require('request');

// Function to get the title of a Star Wars movie
function getMovieTitle(movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error(`Error: ${response.statusCode}`);
      return;
    }

    const movie = JSON.parse(body);
    console.log(movie.title);
  });
}

// Main execution
if (process.argv.length !== 3) {
  console.error('Usage: ./3-starwars_title.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
getMovieTitle(movieId);
