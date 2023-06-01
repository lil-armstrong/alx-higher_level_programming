/* global $ */
$.ajax({
  type: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  success: (character) => {
    $('div#character').html(character?.name);
  }
});
