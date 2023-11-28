from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from datetime import datetime, timedelta

from schemas.song import Song as song_schema
from schemas.artist import Artist as artist_schema
from schemas.user import TokenStr as tokenstr

from utils.login import login_check

import utils.song as song_utils

from jose import jwt

router = APIRouter(
    prefix="/song",
    tags=["song"]
)

@router.get('/get/id/')
async def get_song(id: int, token: str):
    login_check(token)
    songlist = song_utils.get_song(id)
    return {
        "id": id,
        "name": songlist[0],
        "duration": songlist[1],
        "artist": songlist[2]
    }

@router.get('/get/name/')
async def get_song_name(token: str, name: str | None = None):
    if name == None:
        name = ""
    login_check(token)
    songlist = song_utils.get_song_name(name)
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
    return song

@router.get('/get/artist/')
async def get_song_artist(name: str, token: str):
    login_check(token)
    songlist = song_utils.get_song_artist(name)
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
    return song

@router.get('/get/file/')
async def get_song_file(id: int, token: str):
    #Расчет на то, что в БД и на сервере все песни есть в одинаковом количестве
    #Так что нет проверки на наличие песни у сервера, если она есть у БД
    login_check(token)
    if song_utils.get_song(id) == None:
        raise HTTPException(status_code=404, detail="Song not found")
    return FileResponse(f"songs/{id}.mp3")


@router.post('/add/', status_code=204)
async def add_song(song_id: int, token: str):
    login_check(token)
    info = jwt.get_unverified_claims(token)
    song_utils.add_song(info['id'], song_id)

@router.delete('/remove/', status_code=204)
async def remove_song(song_id: int, token: str):
    login_check(token)
    info = jwt.get_unverified_claims(token)
    song_utils.remove_song(info['id'], song_id)

@router.get('/get/my/')
async def get_my_song(token: str):
    login_check(token)
    info = jwt.get_unverified_claims(token)
    songlist = song_utils.get_my_song(info['id'])
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
    return song

