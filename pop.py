import uvicorn
from fastapi import FastAPI, File

from main import router

app = FastAPI()

app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
