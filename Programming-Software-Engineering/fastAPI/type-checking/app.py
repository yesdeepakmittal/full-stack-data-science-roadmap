from fastapi import FastAPI

app = FastAPI()

# Allow only certain datatype parameters to be passed in making HTTP request
@app.get("/test/{id}")
async def testing_datatype_fastapi(id: int):
    '''
        In fastAPI, if you will pass any value other than permitted datatype(int)
        in making this GET request[!curl http://localhost:8000/test/wrong_data], you will get error. 
    '''
    return {"id": id}


from enum import Enum
class OnlyPermittedTypeValue(str,Enum):
    '''
    Inheriting Enum & str class to configure to accept only certain kind of data in HTTP request
    '''
    value1 = 'v1'
    value2 = 'v2'
    value3 = 'v3'
    
@app.get('/{value_type}/{n}')
def only(value_type: OnlyPermittedTypeValue, n:int):
    return {'value':value_type, 'n':n}

#parameter specific validation
from fastapi import Path

@app.get('/test/{n}')
async def fixing_default_val(n: int = Path(...,le=10)):   #constraint for setting default value not applied with ...
    return {'n':n}

@app.get('/woe/{n}')
async def fn(n: int = Path(lt=5)):      #default value set
    return {'n':n}

@app.get("/name/{my_name}")
async def str_validation(my_name: str = Path(..., min_length=6, max_length=6)):
    return {"name": my_name}

#query parameter validation
@app.get("/studentrecord")
async def get_student_record(name: str = 'NA', city: str = 'NA'):
    return {"name": name, "city": city}

@app.get('/studentrecord2')
async def get_student_record2(name: OnlyPermittedTypeValue = 'v1', city: str = ''):
    return {"name": name, "city": city}

