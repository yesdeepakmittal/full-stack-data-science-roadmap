from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

def next_roll_no():
    return max(s.roll for s in students) + 1

class Students(BaseModel):
    roll: int = Field(default_factory=next_roll_no, alias="roll_no")
    name: str
    city: str

students = [
    Students(roll_no=1, name="Deepak", city="Meerut"),
    Students(roll_no=2, name="Avika-Sharma", city="Meerut"),
    Students(roll_no=3, name="Sarvagya-Mittal", city="Meerut"),
    Students(roll_no=4, name="Janaki-Mittal", city="Meerut"),
    Students(roll_no=99, name="delete-me", city="NA")
]

@app.get("/students")
async def get_students():
    return students

@app.post("/students", status_code=201)
async def add_student(student: Students):
    students.append(student)
    return student

@app.delete('/students/<str:no>')
async def delete_krdo(no):
    print(no)
    # for idx,s in enumerate(students):
    #     print(s)
    #     if s.roll == no:
    #         print(s.roll)
    #         students.pop(idx)
    #         return 'delete done'
    return 'delete not done'