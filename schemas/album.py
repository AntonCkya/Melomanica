from pydantic import BaseModel

class Album(BaseModel):
    name: str
    artist_id: int

class AlbumSong(BaseModel):
    album_id: int
    song_id: int
