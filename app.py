from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
  return {"message":"hello world"}


@app.get('/posts/{item}')
async def root(item):
  return {"message":item}