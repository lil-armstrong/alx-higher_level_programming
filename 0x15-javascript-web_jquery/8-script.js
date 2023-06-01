/* global $ */
$.ajax({
  type: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: (movies) => {
    $.each(movies.results, (index, movie) => {
      $('div#list_movies').append(`<li>${movie?.title}</li>`);
    });
  }
});
