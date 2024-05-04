from fastapi import FastAPI, File, UploadFile
import uvicorn

app = FastAPI()

@app.get("/ping")
async def ping():
    return "Hello i am alive"

@app.post("/predict")
async def predict(
        file: UploadFile = File(...)
):
    pass

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}



if __name__ == '__main__':
    uvicorn.run(app,host='localhost', port = 8000)
