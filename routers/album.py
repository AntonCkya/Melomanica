from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from datetime import datetime, timedelta

from schemas.song import Song as song_schema
from schemas.artist import Artist as artist_schema
from schemas.user import TokenStr as tokenstr

from utils.login import login_check

import utils.album as album_utils

router = APIRouter(
    prefix="/album",
    tags=["album"]
)

@router.get('/get/id/')
async def get_album(id: int, token: str):
    login_check(token)
    album_meta = album_utils.get_album(id)
    songlist = album_utils.get_songs_album(id)
    song = []
    for s in songlist:
        song.append(
            {
                "id": s[0],
                "name": s[1],
                "duration": s[2],
                "artist": s[3]
            }
        )
    return {
        "name" : album_meta[0],
        "artist" : album_meta[1],
        "songs": song
    }

@router.get('/get/name/')
async def get_album_name(token: str, name: str | None = None):
    if name == None:
        name = ""
    login_check(token)
    album_meta = album_utils.get_album_name(name)
    albumlist = []
    for s in album_meta:
        albumlist.append(
            {
                "id": s[0],
                "name" : s[1],
                "artist" : s[2]
            }
        )
    return albumlist

@router.get('/get/artist/')
async def get_album_artist(token: str, name: str | None = None):
    if name == None:
        name = ""
    login_check(token)
    album_meta = album_utils.get_album_artist(name)
    albumlist = []
    for s in album_meta:
        albumlist.append(
            {
                "id": s[0],
                "name" : s[1],
                "artist" : s[2]
            }
        )
    return albumlist
