/* global $ */
$(() => {
  const codeInput = $('input#language_code');

  const btn = $('input#btn_translate');
  const target = $('div#hello');

  btn.click(() => {
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${codeInput.val()}`;

    $.ajax({
      type: 'GET',
      url,
      success: (tr) => {
        target.text(tr.hello);
      },
      error: console.error
    });
  });
});
