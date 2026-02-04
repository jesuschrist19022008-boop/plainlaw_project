from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get_results")
def get_results():
    with open("classified_clauses.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return data
