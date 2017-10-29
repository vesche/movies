#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Little script to generate markdown and download poster for my movies repo.
# Ensure to run from this folder as it uses local paths.
# https://github.com/vesche/movies
#

import argparse
import os
import sys

try:
    from imdbpie import Imdb
    imdb = Imdb()
except ImportError:
    print('Error: Requires the imdbpie library.')
    sys.exit(1)


def lookup_movie(title, year=None):
    results = imdb.search_for_title(title)
    if year:
        for m in results:
            if year == m['year']:
                return m
    return results[0]


def get_parser():
    parser = argparse.ArgumentParser(description='genmd')
    parser.add_argument('-m', '--movie',
                        help='name of a movie',
                        required=True, type=str)
    parser.add_argument('-y', '--year',
                        help='year of movie (optional)',
                        type=str)
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    title = args['movie']
    year = args['year']

    result = lookup_movie(title, year)
    movie = imdb.get_title_by_id(result['imdb_id'])

    movie_title = movie.title
    movie_year = movie.year
    movie_poster = movie.cover_url
    movie_url = 'http://www.imdb.com/title/{}'.format(result['imdb_id'])

    print('{} ({})'.format(movie_title, movie_year))
    print(movie_poster)
    print(movie_url)

    cont = input('\nLook right (Y/n)? ')
    if cont.lower().startswith('n'):
        print('Ok, stopped.')
        sys.exit(1)

    image_name = '{}_{}.jpg'.format('_'.join(movie_title.split()), movie_year)
    os.system('wget -O images/"{}" "{}"'.format(image_name, movie_poster))
    print('Poster downloaded!')

    # print('\nMarkdown:')
    # print('[![{}](../images/{})]({})'.format(movie_title, image_name, movie_url))

    markdown = ' [![{}](../images/{})]({})'.format(movie_title, image_name, movie_url)

    with open('lists/{}.md'.format(movie_year), 'a') as f:
        f.write(markdown)
    print('Markdown added!')


if __name__ == '__main__':
    main()
