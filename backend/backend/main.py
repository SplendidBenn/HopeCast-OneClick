from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
import base64
from ecdsa import SigningKey, VerifyingKey, NIST384p
from datetime import datetime
import os

app = FastAPI(title="HopeCast One-Click Backend")

# Mount static files later
app.mount("/static", StaticFiles(directory="static"), name="static")

# Permanent keys
KEY_PATH = "private_key.pem"
if os.path.exists(KEY_PATH):
    sk = SigningKey.from_pem(open(KEY_PATH).read())
else:
    sk = SigningKey.generate(curve=NIST384p)
    with open(KEY_PATH, "wb") as f:
        f.write(sk.to_pem())
vk = sk.verifying_key

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>HopeCast Backend LIVE</h1>
    <p>Visit <a href="/public-key">/public-key</a> to get your verification key.</p>
    <p>Visit <a href="/docs">/docs</a> for API.</p>
    """

@app.get("/public-key")
def get_public_key():
    return {"public_key": vk.to_pem().decode()}

@app.post("/broadcast")
def broadcast(message: str = Form(...)):
    # Mock broadcast to many languages
    languages = ["en", "es", "fr", "ar", "yo", "sw", "zh", "hi", "pt", "ru"]
    delivered = 0
    for lang in languages:
        payload = base64.b64encode(f"[{lang}] {message}".encode())
        signature = sk.sign(payload)
        delivered += 1  # In real: send via FCM/WhatsApp
    
    return JSONResponse({
        "status": "success",
        "reached": f"{delivered} languages",
        "timestamp": datetime.utcnow().isoformat(),
        "proof": "Signed with your permanent key"
    })
