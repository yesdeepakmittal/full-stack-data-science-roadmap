# Exposing files using fastapi

path = 'C:\\Users\\deepak-mittal\\Desktop\\private\\full-stack-data-science-roadmap\\Programming-Software-Engineering\\fastAPI\\how-to-run-fastapi-app.txt'

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get('/test')
async def fn():
    return FileResponse(path=path)