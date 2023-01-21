from flask import Flask, request, jsonify

app = Flask(__name__)

students = [
    {"roll_no": 1, "name": "Deepak", "city": "Meerut"},
    {"roll_no": 2, "name": "Avika-Sharma", "city": "Meerut"},
    {"roll_no": 3, "name": "Sarvagya-Mittal", "city": "Meerut"},
    {"roll_no": 4, "name": "Janaki-Mittal", "city": "Meerut"},
]

def next_roll_no():
    return max(student["roll_no"] for student in students) + 1

@app.get("/students")
def get_students():
    return jsonify(students)

@app.post("/students")
def add_student():
    if request.is_json:
        student = request.get_json()
        student["roll_no"] = next_roll_no()
        students.append(student)
        return student, 201
    return {"error": "Incompatible data format"}, 415

@app.delete('/students/<int:no>')
def delete_krdo(no):
    for idx,value in enumerate(students):
        if value['roll_no'] == no:
            students.pop(idx)
            return 'happy'
    return 'not happy'