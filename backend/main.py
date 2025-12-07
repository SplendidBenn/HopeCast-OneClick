@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1 style="text-align:center;padding:50px;font-family:Arial;color:#d32f2f">
    HopeCast is LIVE! 🎉
    </h1>
    <p style="text-align:center;font-size:18px">
    <a href="/static/index.html">→ Click here for the One-Click Global Button ←</a>
    </p>
    """
