from app.model.level import Level
from app import response, app, db
from flask import jsonify, request

# GET DATA
def index():
    try:
        level = Level.query.all()
        data = formatArray(level)
        return response.success(data, "Success!")
    except Exception as e:
        print(e)

def formatArray(datas):
    array = []

    for i in datas:
        array.append(singleObject(i))

    return array

def singleObject(data):
    data = {
        'id' : data.id,
        'level' : data.level
    }
    return data

# GET DATA BY DETAIL 
def detail(id):
    try:

        levels = Level.query.filter_by(id=id).first()
        if not levels:
            return response.badRequest([],'Data Level kosong....')
        
        data = singleObject(levels)

        return response.success(data,'Sukses View Data!')
    except Exception as e:
        return(e)

# POST DATA
def save():
    try:
        level = request.form.get('level')
        input = [
            {
                'level' : level
            }
        ]
        
        levels = Level(level=level)
        
        db.session.add(levels)
        db.session.commit()

        return response.success(input,'Sukses Menambahkan Data!')
    except Exception as e:
        return(e)
    
# UPDATE DATA
def ubah(id):
    try:
        level = request.form.get('level')

        input = [
            {
                'level' : level
            }
        ]

        levels = Level.query.filter_by(id=id).first()
        levels.level = level

        db.session.commit()

        return response.success(input,'Sukses Edit Data!')
    except Exception as e:
        return(e)
    
def hapus(id):
    try:
        level = Level.query.filter_by(id=id).first()
        if not level:
            return response.badRequest([],'Data Level kosong....')
        
        db.session.delete(level)
        db.session.commit()

        return response.success('','Sukses Hapus Data!')

    except Exception as e:
        print(e)