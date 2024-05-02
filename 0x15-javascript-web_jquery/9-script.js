/* global $ */

$(document).ready(() => {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    success: function(data) {
      $('#hello').text(data.hello);
    },
    error: function(xhr, status, error) {
      console.error('Error fetching translation:', error);
    }
  });
});
