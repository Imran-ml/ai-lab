# fastapi-proxy/main.py

import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import httpx
from pydantic import BaseModel

LLAMA_CPP_SERVER_URL = os.getenv("LLAMA_CPP_URL", "http://llama-cpp:8080/v1/chat/completions")

app = FastAPI(
    title="SmolVLM Camera Proxy",
    description="A proxy server to forward requests from a web UI to a llama.cpp server.",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class FrameProcessRequest(BaseModel):
    instruction: str
    imageBase64URL: str

@app.get("/", response_class=HTMLResponse)
async def read_root():

    try:
        with open("index.html") as f:
            return HTMLResponse(content=f.read(), status_code=200)
    except FileNotFoundError:
        return HTMLResponse(content="<h1>index.html not found</h1>", status_code=404)

@app.post("/process_frame")
async def process_frame(request: FrameProcessRequest):

    try:
        payload = {
            "max_tokens": 100,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": request.instruction},
                        {"type": "image_url", "image_url": {"url": request.imageBase64URL}}
                    ]
                }
            ]
        }

        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(LLAMA_CPP_SERVER_URL, json=payload)
            response.raise_for_status()
            data = response.json()
            model_response = data.get("choices", [{}])[0].get("message", {}).get("content", "No response content found.")
            return {"response": model_response}

    except httpx.RequestError as exc:
        print(f"Error requesting {exc.request.url!r}: {exc}")
        raise HTTPException(
            status_code=503,
            detail=f"Could not connect to the llama.cpp server at {LLAMA_CPP_SERVER_URL}. Is it running and has the model loaded?"
        )
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise HTTPException(status_code=500, detail=str(e))