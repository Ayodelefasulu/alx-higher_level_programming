/* global $ */

$(document).ready(() => {
  $('#add_item').click(() => {
    const newItem = $('<li>').text('Item');
    $('.my_list').append(newItem);
  });

  $('#remove_item').click(() => {
    $('.my_list li:last-child').remove();
  });

  $('#clear_list').click(() => {
    $('.my_list').empty();
  });
});
