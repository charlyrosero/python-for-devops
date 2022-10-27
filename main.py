import re
from unittest import result
from fastapi import FastAPI
import uvicorn
from library.logic import *
from fastapi.responses import JSONResponse


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "wikipedia API. call /search or /wiki"}


@app.get("/search/{value}")
async def search(value: str):
    """Page to search in wikipedia"""
    result = findwiki(value)
    return {"Result": result}


@app.get("/wiki/{value}")
async def page(value: str):
    """Page to search in wikipedia"""
    result = wiki(value)

    return result


@app.get("/phrase/{value}")
async def pra(value: str):
    """Retrieve wikipedia page and return phrases"""
    result = phrase(value)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8090, host="0.0.0.0")
