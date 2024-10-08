from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import base64

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

@app.post("/encrypt")
async def encrypt(message: Message):
    encrypted = base64.b64encode(message.message.encode()).decode()
    return {"encrypted_message": encrypted}

@app.post("/decrypt")
async def decrypt(image: UploadFile = File(...)):
    # For now, we'll just return a placeholder message
    return {"decrypted_message": f"This is a placeholder for decryption from {image.filename}"}