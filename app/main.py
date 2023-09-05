from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
from .import models
from .database import engine
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Schema Models/ Pydantic Models define the structure of a request and response
# this ensure that when a user wants to create a post, the request will only go through
# if it has a "title" and "content" in the body.


while True:

    try:
        conn = psycopg2.connect(host='localhost', database='fastapi',
                                user='postgres', password='Postgres',
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful!")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)

my_posts = [{"title": "title of post 1",
             "content": "content of post 1", "id": 1},
            {"title": "favorite foods", "content": "I like pizza", "id": 2}]


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
