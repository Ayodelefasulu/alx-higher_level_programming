/* global $ */

$(document).ready(() => {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function(data) {
      const movies = data.results;
      const listElement = $('#list_movies');
      
      movies.forEach(movie => {
        const title = $('<li>').text(movie.title);
        listElement.append(title);
      });
    },
    error: function(xhr, status, error) {
      console.error('Error fetching movies data:', error);
    }
  });
});
