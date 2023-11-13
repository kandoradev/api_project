from fastapi import FastAPI, Body, Response, status
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
        
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i

        
@app.get("/")
async def root():
    return {"message": "I am happy to be here :)"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}
    
def create_a_post(new_post: Post):
    new_id = max(post["id"] for post in my_posts) + 1
    post_dict = new_post.dict()
    post_dict['id'] = new_id
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(new_post: Post):
    return create_a_post(new_post)

@app.delete("/posts/{id}")
def delete_a_post(id: int):
    post = find_post(id)
    if not post:
        return {"detail": f"Post with id {id} not found"}
    index = my_posts.index(post)
    my_posts.pop(index)
    return {"data": "post deleted"}

@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detail": f"Post with id {id} not found"}
    print(post)
    return {"post_detail": post}

