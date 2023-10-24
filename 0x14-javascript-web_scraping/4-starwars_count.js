#!/usr/bin/node

/*
 *  script that prints the number 
 *  of movies where the character 
 *  “Wedge Antilles” is present.
 */

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node 4-starwars_count.js <API_URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];
const characterId = 18; // Wedge Antilles' character ID

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    const count = films.filter((film) =>
      film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
    ).length;

    console.log(count);
  } else {
    console.error(`Error: Status code ${response.statusCode}`);
  }
});

