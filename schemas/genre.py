from pydantic import BaseModel

class Genre(BaseModel):
    name: str

class GenreSong(BaseModel):
    genre_id: int
    song_id: int
