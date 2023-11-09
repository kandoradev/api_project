from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional
from fastapi.params import Body
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str 
    published: bool = True
    rating: Optional[int] = None
       
my_posts = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "title of post 2", "content": "content of post 2", "id": 2},
    {"title": "title of post 3", "content": "content of post 3", "id": 3}
]

def find_post(id): 
    for p in my_posts:
        if p["id"] == id:
            return p
        
@app.get("/")
async def root():
    return {"message": "I am happy to be here :)"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}
    
@app.post("/posts{id}")
def create_a_post(new_post: Post):
    post_dict = new_post.dict()
    post_dict['id'] = randrange(0, 100000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.delete("/posts/{id}")
def delete_a_post(id: int):
    post = find_post(post_id)
    index = find_index_post(id)
    myposts.pop(index)
    return {"data": "post deleted"}

@app.get("/posts/{id}")
def get_posts(id: int):
    print(id)
    post = find_post(id)
    print(post)
    return{"post_detail": post}
    