from pydantic import BaseModel

class Artist(BaseModel):
    name: str

class ArtistSong(BaseModel):
    artist_id: int
    song_id: int
