from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from datetime import datetime, timedelta

from schemas.song import Song as song_schema
from schemas.artist import Artist as artist_schema
from schemas.user import TokenStr as tokenstr

from utils.login import login_check

import utils.genre as genre_utils
import utils.song as song_utils

router = APIRouter(
    prefix="/genre",
    tags=["genre"]
)

@router.get('/get/id/')
async def get_genre_name(id: int, token: str):
    login_check(token)
    g = genre_utils.get_genre_name(id)
    return {
        "id": g[0],
        "name": g[1]
    }

@router.get('/get/songs/')
async def get_genre_songs(id: int, token: str):
    login_check(token)
    g = genre_utils.get_genre_name(id)
    songs = genre_utils.get_genre_songs(id)
    songlist = []
    for s in songs:
        songlist.append(
            {
                "id": s[0],
                "name": s[1],
                "duration": s[2],
                "artist": s[3]
            }
        )
    return {
        "id": g[0],
        "genre_name": g[1],
        "songs": songlist
    }

@router.get('/get/genre/')
async def get_song_genres(id: int, token: str):
    login_check(token)
    song = song_utils.get_song(id)
    genres = genre_utils.get_song_genres(id)
    genrelist = []
    for g in genres:
        genrelist.append(
            {
                "id": g[0],
                "name": g[1]
            }
        )
    return {
        "id": id,
        "song_name": song[0],
        "duration": song[1],
        "artist": song[2],
        "genres": genrelist
    }
