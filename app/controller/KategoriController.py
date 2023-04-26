from app.model.kategori import Kategori
from app import response, app, db
from flask import jsonify, request

# GET DATA
def index():
    try:
        kategori = Kategori.query.all()
        data = formatArray(kategori)
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
        'kategori' : data.kategori
    }
    return data


# GET DATA BY DETAIL 
def detail(id):
    try:

        kategoris = Kategori.query.filter_by(id=id).first()
        if not kategoris:
            return response.badRequest([],'Data Level kosong....')
        
        data = singleObject(kategoris)

        return response.success(data,'Sukses View Data!')
    except Exception as e:
        return(e)

# POST DATA
def save():
    try:
        kategori = request.form.get('kategori')
        
        input = [
            {
                'kategori' : kategori
            }
        ]
        
        kategoris = Kategori(kategori=kategori)
        
        db.session.add(kategoris)
        db.session.commit()

        return response.success(input,'Sukses Menambahkan Data!')
    except Exception as e:
        return(e)
    

# UPDATE DATA
def ubah(id):
    try:
        kategori = request.form.get('kategori')

        input = [
            {
                'kategori' : kategori
            }
        ]

        kategoris = Kategori.query.filter_by(id=id).first()
        kategoris.kategori = kategori

        db.session.commit()

        return response.success(input,'Sukses Edit Data!')
    except Exception as e:
        return(e)
    
def hapus(id):
    try:
        kategori = Kategori.query.filter_by(id=id).first()
        if not kategori:
            return response.badRequest([],'Data kategori kosong....')
        
        db.session.delete(kategori)
        db.session.commit()

        return response.success('','Sukses Hapus Data!')

    except Exception as e:
        print(e)
