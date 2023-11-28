CREATE TABLE IF NOT EXISTS Users
(
    id INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    login VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(200) NOT NULL
);

CREATE TABLE IF NOT EXISTS Token
(
    user_id INT NOT NULL REFERENCES Users(id) ON DELETE CASCADE,
    token VARCHAR(200) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Artist
(
    id INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    name VARCHAR(200) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Song
(
    id INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    duration INT NOT NULL,
    artist_id INT NOT NULL REFERENCES Artist(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS User_Song
(
    user_id INT NOT NULL REFERENCES Users(id) ON DELETE CASCADE,
    song_id INT NOT NULL REFERENCES Song(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, song_id)
);

CREATE TABLE IF NOT EXISTS Genre(
    id INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Genre_Song(
    genre_id int REFERENCES Genre(id) ON DELETE CASCADE,
    song_id int REFERENCES Song(id) ON DELETE CASCADE,
    PRIMARY KEY (genre_id, song_id)
);

CREATE TABLE IF NOT EXISTS Album(
    id INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    artist_id INT NOT NULL REFERENCES Artist(id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Album_Song(
    album_id INT NOT NULL REFERENCES Album(id) ON DELETE CASCADE,
    song_id INT NOT NULL REFERENCES Song(id) ON DELETE CASCADE,
    PRIMARY KEY (album_id, song_id)
);
