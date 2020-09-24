/* Write a Javascript script that fetches and lists all movies
title by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
All movie titles must be list in the HTML tag UL#list_movies */
$.get("https://swapi-api.hbtn.io/api/films/?format=json",
function (data, textStatus, jqXHR) {
  if (textStatus === 'success') {
    data.results.map((elemt) => {
        $('#list_movies').append(`<li>${elemt.title}</li>`)
    })
  }
});
