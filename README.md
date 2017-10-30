# movies

This is a list of my personal favorite movies sorted by year.

Check out my favorite movies from:
[2017](lists/2017.md), [2016](lists/2016.md), [2015](lists/2015.md), [2014](lists/2014.md), [2013](lists/2013.md), [2012](lists/2012.md), [2011](lists/2011.md), [2010](lists/2010.md)...

See the `lists` folder to see more years.

### I want my own movies repo!

Awesome sauce! First, fork this project so you have a movies repo of your own. Next, clone your movies repo and clear out all my data. If you're on Linux or macOS it'll look something like this:

```
$ git clone https://github.com/username/movies
$ rm -rf images/* lists/*
```

There's a Python script provided to add movies to your repo, make sure you have imdbpie (`pip3 install imdbpie`) and that you're using Python 3.x. The script will automatically download the movie poster and add it to a list!

```
$ python3 getmovie.py -m "Hook"
Hook (1991)
https://images-na.ssl-images-amazon.com/images/M/MV5BNmJjNTQzMjctMmE2NS00ZmYxLWE1NjYtYmRmNjNiMzljOTc3XkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1__SX214_.jpg
http://www.imdb.com/title/tt0102057

Look right (Y/n)? y
Poster downloaded!
Markdown added!
```
