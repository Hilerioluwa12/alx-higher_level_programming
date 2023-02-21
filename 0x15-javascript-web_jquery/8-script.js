$.get('http://swapi.co/api/films?format=json', function (data) => {
  const i = data.results;
  for (const elem of object.values(i)) {
    $('ul#list_movies').append('<li>' + elem.title + '</li>');
  }
});
