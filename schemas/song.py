from pydantic import BaseModel

class Song(BaseModel):
    name: str
    duration: int
    artist: str
