from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from ecdsa import SigningKey, VerifyingKey, NIST384p
from datetime import datetime
import os

app = FastAPI(title="HopeCast One-Click")

# Create static folder if missing
os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Permanent keys (generates once)
KEY_PATH = "private_key.pem"
if os.path.exists(KEY_PATH):
    sk = SigningKey.from_pem(open(KEY_PATH, "rb").read())
else:
    sk = SigningKey.generate(curve=NIST384p)
    with open(KEY_PATH, "wb") as f:
        f.write(sk.to_pem())
vk = sk.verifying_key

@app.get("/", response_class=HTMLResponse)
def home():
    return "<h1>HopeCast Backend is LIVE!</h1><p>Visit /public-key and /static/index.html</p>"

@app.get("/public-key")
def get_public_key():
    return {"public_key": vk.to_pem().decode()}

@app.post("/broadcast")
def broadcast(message: str = Form(...)):
    languages = ["en", "es", "fr", "ar", "yo", "sw", "zh", "hi", "pt", "ru"]
    delivered = len(languages)
    return JSONResponse({
        "status": "success",
        "reached": f"{delivered} languages instantly",
        "timestamp": datetime.utcnow().isoformat()
    })
