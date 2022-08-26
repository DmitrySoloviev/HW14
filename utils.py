import sqlite3


def load_database():
    conn = sqlite3.connect("netflix.db")
    curs = conn.cursor()
    sqlite_query = ("""
                SELECT *
                FROM netflix
            
                """)
    result = curs.execute(sqlite_query)
    return result


def get_by_title(title):
    result = load_database()
    movie_dict = {}
    try:
        for i in result.fetchall():
            i = list(i)
            if title.lower() == i[2].lower():
                movie_dict['title'] = i[2]
                movie_dict['country'] = i[5]
                movie_dict['release_date'] = i[7]
                movie_dict['genre'] = i[11]
                movie_dict['description'] = i[12]
            else:
                pass
        return movie_dict
    except ValueError:
        raise None


def get_by_year(year_from, year_to):
    result = load_database()
    movie_by_year = []
    try:
        i = 0
        if len(movie_by_year) < 100:
            for i in result.fetchall():
                i = list(i)
                if year_from <= i[7] <= year_to:
                    single_movie_dict = {'title': i[2], 'release_date': i[7]}
                    movie_by_year.append(single_movie_dict)
                else:
                    pass
        else:
            pass
        return movie_by_year
    except ValueError:
        raise None


def get_by_rating(rating):
    if rating == "children":
        rating_one = 'G'
    elif rating == "family":
        conn = sqlite3.connect("netflix.db")
        curs = conn.cursor()
        sqlite_query = ("""
                        SELECT title, rating
                        FROM netflix
                        WHERE rating LIKE 'PG%' OR rating ='G'
                        """)
        result = curs.execute(sqlite_query)
        result = result.fetchall()
        return result
    elif rating == "adult":
        rating_one = 'R'
    else:
        rating_one = 'not'
    conn = sqlite3.connect("netflix.db")
    curs = conn.cursor()
    sqlite_query = ("""
                SELECT title, rating
                FROM netflix
                WHERE rating =?
                """)
    result = curs.execute(sqlite_query, (rating_one,))
    result = result.fetchall()
    return result


def get_by_genre(genre):
    genre = '%' + genre
    conn = sqlite3.connect("netflix.db")
    curs = conn.cursor()
    sqlite_query = ("""
                SELECT title, listed_in
                FROM netflix
                WHERE listed_in LIKE?
                """)
    result = curs.execute(sqlite_query, (genre,))
    result = result.fetchall()
    result_list = []
    for i in result:
        result_dict = {'title': i[0], 'gente': i[1]}
        result_list.append(result_dict)
    if len(result_list) < 1:
        return None
    return result_list


def get_by_two(actor_one, actor_two):
    actors = '%' + actor_one + '%' + actor_two + '%'
    conn = sqlite3.connect("netflix.db")
    curs = conn.cursor()
    sqlite_query = ("""
                SELECT title, "cast"
                FROM netflix
                WHERE "cast" LIKE?
                """)
    result = curs.execute(sqlite_query, (actors,))
    result = result.fetchall()
    if len(result) < 1:
        return None
    return result


def get_by_type(type_, genre, year):
    result = load_database()
    movie_list = []
    try:
        for i in result.fetchall():
            movie_dict = {}
            i = list(i)
            if type_.lower() == i[1].lower():
                if year == i[7]:
                    list_genre = i[11].split(", ")
                    if genre in list_genre:
                        movie_dict = {'title': i[2], 'release_date': i[7], 'genre': i[11]}
            else:
                pass
            if len(movie_dict) > 0:
                movie_list.append(movie_dict)
        return movie_list
    except ValueError:
        raise None

print(get_by_two('Rose McIver', 'Ben Lamb'))
print(get_by_type('Movie', 'Comedies', 2017))
