from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
from backend.core.summarizer import TCSummarizer


app = FastAPI()
templates = Jinja2Templates(directory="frontend/templates")
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

summarizer = TCSummarizer()

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    show = request.query_params.get("show")
    summary = request.query_params.get("summary") if show == "1" else None
    url = request.query_params.get("url") if show == "1" else None
    error = request.query_params.get("error")
    return templates.TemplateResponse("index.html", {"request": request, "summary": summary, "error": error, "url": url})

@app.post("/summarize", response_class=HTMLResponse)
def summarize(request: Request, url: str = Form(...)):

    try:
        summary = summarizer.summarize(url)
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "summary": summary, "error": None, "url": url}
        )
    except Exception as e:
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "summary": None, "error": f"An error occurred: {str(e)}", "url": url}
        )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=False) 