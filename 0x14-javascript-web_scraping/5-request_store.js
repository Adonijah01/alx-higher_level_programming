#!/usr/bin/node

/*
 * script that gets the contents 
 * of a webpage and stores it in a file
 */

const request = require('request');
const fs = require('fs');

if (process.argv.length !== 4) {
  console.error('Usage: node 5-request_store.js <URL> <file_path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      } else {
        console.log(`Data has been written to ${filePath}`);
      }
    });
  } else {
    console.error(`Error: Status code ${response.statusCode}`);
  }
});

