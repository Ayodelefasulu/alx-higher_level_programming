#!/usr/bin/node
const request = require('request');

// Function to print all characters of a Star Wars movie
function printMovieCharacters(movieId) {
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
    const characters = movie.characters;

    characters.forEach(characterUrl => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error(error);
          return;
        }

        if (response.statusCode !== 200) {
          console.error(`Error: ${response.statusCode}`);
          return;
        }

        const character = JSON.parse(body);
        console.log(character.name);
      });
    });
  });
}

// Main execution
if (process.argv.length !== 3) {
  console.error('Usage: ./100-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
printMovieCharacters(movieId);
