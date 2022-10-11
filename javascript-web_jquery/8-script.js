$.get("https://swapi-api.hbtn.io/api/films/?format=json", (data, status) => {
    if (status === "success") {
        const results = data.results;
        results.forEach(film => {
            $('ul#list_movies').append(`<li>${film.title}</li>`);
        });
    }
})