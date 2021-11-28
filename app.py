from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get('/')
async def root():
  return {"message":"hello world"}

# string parameter

@app.get('/posts/{item}')
async def root2(item : int):
  return {"message":item}



# query parameter

@app.post('/posts')
async def root4(obj):
  return {"message":obj}


# body data

# json model
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.post('/body')
async def root3(obj:Item):
  return obj


if __name__ == '__main__':
  uvicorn.run(app,port=8000,host="0.0.0.0")