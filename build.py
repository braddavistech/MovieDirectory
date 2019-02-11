# import sqlite3


# conn = sqlite3.connect('movies.sqlite3')
# c = conn.cursor()


# c.execute('''INSERT INTO mymovies_category VALUES (
#             1,
#             "Comedy"
#             )''')
# c.execute('''INSERT INTO mymovies_category VALUES (
#             2,
#             "Sci-Fi"
#             )''')
# c.execute('''INSERT INTO mymovies_category VALUES (
#             3,
#             "Horror"
#             )''')
# c.execute('''INSERT INTO mymovies_category VALUES (
#             4,
#             "Romance"
#             )''')
# c.execute('''INSERT INTO mymovies_category VALUES (
#             5,
#             "Action"
#             )''')
# c.execute('''INSERT INTO mymovies_category VALUES (
#             6,
#             "Thriller"
#             )''')
# c.execute('''INSERT INTO mymovies_category VALUES (
#             7,
#             "Drama"
#             )''')
# c.execute('''INSERT INTO mymovies_category VALUES (
#             8,
#             "Mystery"
#             )''')
# c.execute('''INSERT INTO mymovies_category VALUES (
#             9,
#             "Crime"
#             )''')
# c.execute('''INSERT INTO mymovies_category VALUES (
#             10,
#             "Animation"
#             )''')
# c.execute('''INSERT INTO mymovies_category VALUES (
#             11,
#             "Adventure"
#             )''')
# c.execute('''INSERT INTO mymovies_category VALUES (
#             12,
#             "Fantasy"
#             )''')
# c.execute('''INSERT INTO mymovies_category VALUES (
#             13,
#             "Comedy-Romance"
#             )''')
# c.execute('''INSERT INTO mymovies_category VALUES (
#             14,
#             "Action-Comedy"
#             )''')
# c.execute('''INSERT INTO mymovies_category VALUES (
#             15,
#             "Superhero"
#             )''')
# c.execute('''INSERT INTO mymovies_category VALUES (
#             16,
#             "History"
#             )''')
# c.execute('''INSERT INTO mymovies_category VALUES (
#             17,
#             "War"
#             )''')
# c.execute('''INSERT INTO mymovies_category VALUES (
#             18,
#             "Western"
#             )''')
# c.execute('''INSERT INTO mymovies_movie VALUES (
#             1,
#             "12 Rounds",
#             "Detective Danny Fisher discovers his girlfriend has been kidnapped by an ex-con tied to Fisher's past, and he'll have to successfully complete 12 challenges in order to secure her safe release.",
#             "2009-03-27",
#             "01:48",
#             "https://m.media-amazon.com/images/M/MV5BMTU1MzM1ODkxM15BMl5BanBnXkFtZTcwNDY1MTA0Mg@@._V1_UX182_CR0,0,182,268_AL_.jpg",
#             "https://www.imdb.com/video/imdb/vi3295740697?playlistId=tt1160368&ref_=tt_ov_vi",
#             "moviePath",
#             3.2)''')
# c.execute('''INSERT INTO mymovies_movie VALUES (
#             2,
#             "A Few Good Men",
#             "Military lawyer Lieutenant Daniel Kaffee defends Marines accused of murder. They contend they were acting under orders.",
#             "1992-12-11",
#             "02:18",
#             "https://m.media-amazon.com/images/M/MV5BMmRlZDQ1MmUtMzE2Yi00YTkxLTk1MGMtYmIyYWQwODcxYzRlXkEyXkFqcGdeQXVyNTI4MjkwNjA@._V1_UX182_CR0,0,182,268_AL_.jpg",
#             "https://www.imdb.com/video/imdb/vi2142503193?playlistId=tt0104257&ref_=tt_ov_vi",
#             "moviePath",
#             4.7)''')
# c.execute('''INSERT INTO mymovies_movie VALUES (
#             3,
#             "The A-Team",
#             "A group of Iraq War veterans look to clear their name with the U.S. Military, who suspect the four men of committing a crime for which they were framed.",
#             "2010-06-11",
#             "01:57",
#             "https://m.media-amazon.com/images/M/MV5BMTc4ODc4NTQ1N15BMl5BanBnXkFtZTcwNDUxODUyMw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
#             "https://www.imdb.com/title/tt0429493/videoplayer/vi14943257?ref_=vp_pl_1",
#             "moviePath",
#             4.0)''')
# c.execute('''INSERT INTO mymovies_categorymovie VALUES (
#             1,
#             5,
#             1)''')
# c.execute('''INSERT INTO mymovies_categorymovie VALUES (
#             2,
#             6,
#             1)''')
# c.execute('''INSERT INTO mymovies_categorymovie VALUES (
#             3,
#             7,
#             2)''')
# c.execute('''INSERT INTO mymovies_categorymovie VALUES (
#             4,
#             9,
#             2)''')
# c.execute('''INSERT INTO mymovies_categorymovie VALUES (
#             5,
#             17,
#             2)''')
# c.execute('''INSERT INTO mymovies_categorymovie VALUES (
#             6,
#             1,
#             3)''')
# c.execute('''INSERT INTO mymovies_categorymovie VALUES (
#             7,
#             5,
#             3)''')
# c.execute('''INSERT INTO mymovies_categorymovie VALUES (
#             8,
#             14,
#             3)''')


# conn.commit()