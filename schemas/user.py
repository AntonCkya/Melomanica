from pydantic import BaseModel, validator

class User(BaseModel):
    login: str
    password: str
    
    @validator('password')
    def password_validator(cls, password):
        if len(password) < 8:
            raise ValueError('password length less than 8')
        return password

class Token(BaseModel):
    user_id: int
    token: str

class TokenStr(BaseModel):
    token: str

class UserSong(BaseModel):
    user_id: int
    song_id: int

