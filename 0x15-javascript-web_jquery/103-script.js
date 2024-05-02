/* global $ */

$(document).ready(() => {
  $('#btn_translate').click(fetchTranslation);
  $('#language_code').keypress((e) => {
    if (e.which === 13) { // Check if ENTER key is pressed
      fetchTranslation();
    }
  });

  function fetchTranslation() {
    const languageCode = $('#language_code').val();

    $.ajax({
      url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`,
      method: 'GET',
      success: function(data) {
        $('#hello').text(data.hello);
      },
      error: function(xhr, status, error) {
        console.error('Error fetching translation:', error);
      }
    });
  }
});
