/* global $ */
$(() => {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: (tr) => {
      $('div#hello').text(tr.hello);
    },
    error: console.error
  });
});
