students = [
    {"roll_no": 1, "name": "Deepak", "city": "Meerut"},
    {"roll_no": 2, "name": "Avika-Sharma", "city": "Meerut"},
    {"roll_no": 3, "name": "Sarvagya-Mittal", "city": "Meerut"},
    {"roll_no": 4, "name": "Janaki-Mittal", "city": "Meerut"},
]
def next_roll_no():
    return max(d['roll_no'] for d in students) + 1

def all_students():
    return students

def add_student(rqst):
    for d in students:
        if d['name'] == rqst.get('name'):
            return {"Error":"Student already present in record"}, 406
    new_student = {'roll_no':next_roll_no(), 'name':rqst.get('name'), 'city':rqst.get('city','NA')}
    students.append(new_student)
    return new_student, 201

def only_student(roll_no):
    for d in students:
        if d['roll_no'] == roll_no:
            return d,200
    return {'Error':f"Student Not Found with roll no {roll_no}"}, 404

def update_student(roll_no,rqst):
    for d in students:
        if d['roll_no'] == roll_no:
            d['name'] = rqst.get('name',d.get('name'))
            d['city'] = rqst.get('city',d.get('city'))
        return {'record updated'}, 200
    return {'record not found'}, 404

def delete_record(roll_no):
    return 'Mai delete nhi krunga!'