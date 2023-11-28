from jose import jwt, exceptions
from fastapi import HTTPException
from datetime import datetime, timedelta
import utils.user as user_utils

def login_check(token):
	try:
		info = jwt.get_unverified_claims(token)
	except exceptions.JWTError:
		raise HTTPException(status_code=400, detail="Bad Token")
	if user_utils.get_token(info['id'])[0] != token:
		raise HTTPException(status_code=403, detail="Token incorrect")
	if info["exp"] < datetime.utcnow().timestamp():
		raise HTTPException(status_code=403, detail="Token expired")
