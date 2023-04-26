from app.model.pembayaran import Pembayaran
from app import response, app, db
from flask import jsonify, request

# GET DATA
def index():
    try:
        pembayaran = Pembayaran.query.all()
        data = formatArray(pembayaran)
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
        'pembayaran' : data.pembayaran
    }
    return data

# GET DATA BY DETAIL 
def detail(id):
    try:

        pembayarans = Pembayaran.query.filter_by(id=id).first()
        if not pembayarans:
            return response.badRequest([],'Data Level kosong....')
        
        data = singleObject(pembayarans)

        return response.success(data,'Sukses View Data!')
    except Exception as e:
        return(e)

# POST DATA
def save():
    try:
        pembayaran = request.form.get('pembayaran')
        
        input = [
            {
                'pembayaran' : pembayaran
            }
        ]
        
        pembayarans = Pembayaran(pembayaran=pembayaran)
        db.session.add(pembayarans)
        db.session.commit()

        return response.success(input,'Sukses Menambahkan Data!')
    except Exception as e:
        return(e)
    

# UPDATE DATA
def ubah(id):
    try:
        pembayaran = request.form.get('pembayaran')

        input = [
            {
                'pembayaran' : pembayaran
            }
        ]

        pembayarans = Pembayaran.query.filter_by(id=id).first()
        pembayarans.pembayaran = pembayaran

        db.session.commit()

        return response.success(input,'Sukses Edit Data!')
    except Exception as e:
        return(e)
    
def hapus(id):
    try:
        pembayaran = Pembayaran.query.filter_by(id=id).first()
        if not pembayaran:
            return response.badRequest([],'Data pembayaran kosong....')
        
        db.session.delete(pembayaran)
        db.session.commit()

        return response.success('','Sukses Hapus Data!')

    except Exception as e:
        print(e)