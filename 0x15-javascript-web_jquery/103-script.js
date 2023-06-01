/* global $ */
$(() => {
  const codeInput = $('input#language_code');

  const btn = $('input#btn_translate');
  const target = $('div#hello');

  codeInput.keypress((e) => {
    const keycode = e.keyCode ?? e.which;

    if (keycode === '13') fetchAndPrintTranslation();
  });

  btn.click(fetchAndPrintTranslation);

  function fetchAndPrintTranslation () {
    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${codeInput.val()}`;

    $.ajax({
      type: 'GET',
      url,
      success: (tr) => {
        target.text(tr.hello);
      },
      error: console.error
    });
  }
});
