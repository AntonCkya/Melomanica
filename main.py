from fastapi import FastAPI, HTTPException
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware

from routers import user, song, album, genre

app = FastAPI()

app.include_router(user.router)
app.include_router(song.router)
app.include_router(album.router)
app.include_router(genre.router)

origins = [
	
    "http://localhost"
    "https://localhost",
    "http://localhost:8000",
    "https://localhost:8000",
    "http://localhost:3000",
    "https://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/', tags=["root"])
async def test():
	return {"melomanica": "by M8O-306Б-21"}

def custom_openapi():
	if app.openapi_schema:
		return app.openapi_schema
	openapi_schema = get_openapi(
    	title="Melomanica",
		version="beta 0.1",
		description="API к стриминговому сервису \"Melomanica\"\nby Magki Lapki",
		routes=app.routes,
	)
	app.openapi_schema = openapi_schema
	return app.openapi_schema

app.openapi = custom_openapi