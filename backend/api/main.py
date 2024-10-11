from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from PIL import Image
import io
from core.steganography import encode_message, decode_message

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/encode")
async def encode(image: UploadFile = File(...), message: str = Form(...), password: str = Form(...)):
    try:
        contents = await image.read()
        img = Image.open(io.BytesIO(contents))
        encoded_img = encode_message(img, message, password)
        
        img_byte_arr = io.BytesIO()
        encoded_img.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        return Response(content=img_byte_arr, media_type="image/png", headers={"Content-Disposition": "attachment; filename=encoded_image.png"})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/decode")
async def decode(image: UploadFile = File(...), password: str = Form(...)):
    try:
        contents = await image.read()
        img = Image.open(io.BytesIO(contents))
        decoded_message, message_size = decode_message(img, password)
        return {"message": decoded_message, "size": message_size}
    except Exception as e:
        print(f"Decoding error: {str(e)}")  # Add this line for server-side logging
        raise HTTPException(status_code=400, detail=f"Decoding failed: {str(e)}")
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)