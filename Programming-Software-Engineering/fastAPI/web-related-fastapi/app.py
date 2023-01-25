from fastapi import FastAPI

app = FastAPI()

# Accessing raw request data
from fastapi import Request,status
@app.get('/requestdata',status_code=status.HTTP_200_OK)
async def get_rqst_data(rqst: Request):
    return {'url path': [rqst.url.path,rqst.url.hostname]}

from fastapi.responses import HTMLResponse,RedirectResponse

# redirecting to another URL
@app.get('/anotherurl')
async def anotherurl():
    return RedirectResponse('/checkhtml',status_code=status.HTTP_301_MOVED_PERMANENTLY)

html = '''
<html>
<body>
<h1>Hello, world</h1>
<p>redirected to another url</p>
</body>
</html>
'''
@app.get('/checkhtml',response_class=HTMLResponse)
async def checkhtml():
    return html