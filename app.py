from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
  return {"message":"hello world"}


@app.get('/posts/{item}')
async def root(item : int):
  return {"message":item}


# body 

@app.post('/posts')
async def root(obj):
  return {"message":obj}