/* global $ */

$(document).ready(() => {
  $('#add_item').click(() => {
    const newItem = $('<li>').text('Item');
    $('.my_list').append(newItem);
  });
});
