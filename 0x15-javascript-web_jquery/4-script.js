/* global $ */

const toggler = $('div#toggle_header');
const header = $('header');

toggler.click(() => {
  header.toggleClass('green red');
});
