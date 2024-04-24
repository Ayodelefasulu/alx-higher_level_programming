#!/usr/bin/node
const request = require('request');

// Function to count the number of movies where "Wedge Antilles" is present
function countMoviesWithCharacter(url) {
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error(`Error: ${response.statusCode}`);
      return;
    }

    const films = JSON.parse(body).results;
    const characterId = '18'; // ID of "Wedge Antilles" character

    // Filter movies where "Wedge Antilles" is present
    const moviesWithCharacter = films.filter(film =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    );

    console.log(moviesWithCharacter.length);
  });
}

// Main execution
if (process.argv.length !== 3) {
  console.error('Usage: ./4-starwars_count.js <api_url>');
  process.exit(1);
}

const apiUrl = process.argv[2];
countMoviesWithCharacter(apiUrl);
