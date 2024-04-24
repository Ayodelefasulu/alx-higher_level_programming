#!/usr/bin/node
const request = require('request');

// Function to get characters of a Star Wars movie
function getMovieCharacters(movieId) {
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
    const characterUrls = movie.characters;

    // Array to store character names
    const characterNames = [];

    // Function to recursively retrieve character names
    function getCharacterName(index) {
      if (index === characterUrls.length) {
        // All character names retrieved, print them
        characterNames.forEach(name => console.log(name));
        return;
      }

      request(characterUrls[index], (error, response, body) => {
        if (error) {
          console.error(error);
          return;
        }

        if (response.statusCode !== 200) {
          console.error(`Error: ${response.statusCode}`);
          return;
        }

        const character = JSON.parse(body);
        characterNames.push(character.name);

        // Call the function recursively for the next character
        getCharacterName(index + 1);
      });
    }

    // Start retrieving character names
    getCharacterName(0);
  });
}

// Main execution
if (process.argv.length !== 3) {
  console.error('Usage: ./101-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
getMovieCharacters(movieId);

