#!/usr/bin/node

// This script prints all characters of a Star Wars movie.
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node 100-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;
    getCharacterNames(characterUrls, 0);
  } else {
    console.error(`Error: Status code ${response.statusCode}`);
  }
});

function getCharacterNames(urls, index) {
  if (index < urls.length) {
    request(urls[index], (charError, charResponse, charBody) => {
      if (charError) {
        console.error(charError);
      } else if (charResponse.statusCode === 200) {
        const characterData = JSON.parse(charBody);
        console.log(characterData.name);
        getCharacterNames(urls, index + 1);
      }
    });
  }
}

