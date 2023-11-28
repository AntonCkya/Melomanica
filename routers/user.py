from fastapi import APIRouter, HTTPException
from datetime import datetime, timedelta

from schemas.user import User as user_schema
from schemas.user import Token as token_schema
import utils.user as user_utils

from jose import jwt

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.post('/register/')
async def register(user: user_schema):
    id = user_utils.register(user)
    return {"id": id[0]}

@router.post('/login/')
async def login(user: user_schema):
    id = user_utils.login(user)
    if id == None or len(id) != 1:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    currtime = datetime.utcnow()
    exp = currtime + timedelta(days=7)
    t = jwt.encode(
        {"id": id[0], "exp": exp},
        str(currtime),
        "HS256"
    )
    if user_utils.get_token != None:
        user_utils.delete_token(id[0])
    token = token_schema(user_id=id[0], token=t)
    user_utils.put_token(token)
    return {"token": t}

@router.post('/logout/', status_code=204)
async def logout(user: user_schema):
    id = user_utils.login(user)
    if id == None or len(id) != 1:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user_utils.delete_token(id[0])
