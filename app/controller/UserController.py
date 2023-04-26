from app.model.user import User
import datetime
from app import response, app, db
from flask import request
from flask_jwt_extended import *
from flask_login import logout_user
from flask_jwt_extended import unset_jwt_cookies

# GET DATA
def index():
    try:
        user = User.query.all()
        data = formatArray(user)
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
        'nama' : data.nama,
        'username' : data.username,
        'id_level' : data.id_level,
        'alamat' : data.alamat,
        'email' : data.email,
        'no_telp' : data.no_telp
    }

    return data

# GET DATA BY DETAIL 
def detail(id):
    try:

        user = User.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([],'Data Level kosong....')
        
        data = singleObject(user)

        return response.success(data,'Sukses View Data!')
    except Exception as e:
        return(e)


# POST DATA
def save():
    try:
        nama = request.form.get('nama')
        username = request.form.get('username')
        password = request.form.get('password')
        id_level = request.form.get('id_level')
        alamat = request.form.get('alamat')
        email = request.form.get('email')
        no_telp = request.form.get('no_telp')

        input = [
            {
                'nama' : nama,
                'username' : username,
                'id_level': id_level,
                'email' : email,
                'alamat' : alamat,
                'no_telp' : no_telp
            }
        ]        

        users = User(nama=nama, username=username, id_level=id_level, alamat=alamat, email=email, no_telp=no_telp)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()

        return response.success(input,'Sukses Menambahkan Data!')
    except Exception as e:
        return(e)
    

# UPDATE DATA
def ubah(id):
    try:
        nama = request.form.get('nama')
        username = request.form.get('username')
        password = request.form.get('password')
        id_level = request.form.get('id_level')
        alamat = request.form.get('alamat')
        email = request.form.get('email')
        no_telp = request.form.get('no_telp')

        input = [
            {
                'nama' : nama,
                'username' : username,
                'password' : password,
                'id_level': id_level,
                'email' : email,
                'alamat' : alamat,
                'no_telp' : no_telp
            }
        ]

        users = User.query.filter_by(id=id).first()
        users.nama = nama
        users.username = username
        users.id_level = id_level
        users.alamat = alamat
        users.email = email
        users.no_telp = no_telp
        users.setPassword(password)

        db.session.commit()

        return response.success(input,'Sukses Edit Data!')
    except Exception as e:
        return(e)
    
def hapus(id):
    try:
        user = User.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([],'Data user kosong....')
        
        db.session.delete(user)
        db.session.commit()

        return response.success('','Sukses Hapus Data!')

    except Exception as e:
        print(e)

# Login
def login():
    try:
        email = request.form.get('email')
        password = request.form.get('password')
    
        user = User.query.filter_by(email=email).first()

        if not user:
            return response.badRequest([],'Email tidak ditemukan!')

        if not user.checkPassword(password):
            return response.badRequest([],'Password Salah!')

        data = singleObject(user)

        expires = datetime.timedelta(days=7)
        expires_refresh = datetime.timedelta(days=7)

        access_token = create_access_token(data, fresh=True, expires_delta=expires)
        refresh_token = create_refresh_token(data, expires_delta=expires_refresh)

        return response.success({
            'data' : data,
            'access_token' : access_token,
            'refresh_token' : refresh_token
        },'Sukses login!')
    except Exception as e:
        print(e)