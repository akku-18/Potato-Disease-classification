from fastapi import FastAPI, File, UploadFile
import uvicorn
from typing import Annotated


app = FastAPI()

@app.get("/ping")
async def ping():
    return "Hello i am alive"

@app.post("/predict")
async def predict(
        file: UploadFile = File(...)
):
    pass

@app.post("/files")
async def UploadImage(file: bytes = File(...)):
    with open('image.jpg','wb') as image:
        image.write(file)
        image.close()
    return 'got it'


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port = 8000)
