$(function () {
        $.ajax({
               type: 'GET',
                url: 'https://swapi-api.hbtn.io/api/films/?format=json',
                success: function (films) {
                        $.each(films.results, function (i, movie) {
                                $('ul#list_movies').append('<li>' + movie.title + '</li>');
                        });
                }
        });
}); 
