from app.model.user import User
import datetime
from app import response, app, db
from flask import request
from flask_jwt_extended import *
from flask import render_template
from flask import jsonify, redirect, request


# GET DATA
def index():
    users = User.query.all()
    return render_template('admin-kasir/viewUser.html', users = users)

# GET DATA BY DETAIL 
def detail(id):
    user = User.query.filter_by(id=id).first()
    if not user:
        return response.badRequest([],'Data Level kosong....')

    return render_template('admin-kasir/detailUser.html', user = user)

# POST DATA
def save():
    nama = request.form['nama']
    username = request.form['username']
    password = request.form['password']
    id_level = request.form['id_level']
    alamat = request.form['alamat']
    email = request.form['email']
    no_telp = request.form['no_telp']
    users = User(nama=nama, username=username, id_level=id_level, alamat=alamat, email=email, no_telp=no_telp)
    users.setPassword(password)
    db.session.add(users)
    db.session.commit()

    return redirect('/manage/user')

# UPDATE DATA
def ubah(id):

    if request.method == 'POST':
        user = User.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([],'Data Tidak Ada!')
        
        db.session.delete(user)
        db.session.commit()

        nama = request.form['nama']
        username = request.form['username']
        password = request.form['password']
        id_level = request.form['id_level']
        alamat = request.form['alamat']
        email = request.form['email']
        no_telp = request.form['no_telp']
        users = User(nama=nama, username=username, password=password, id_level=id_level, alamat=alamat, email=email, no_telp=no_telp)

        db.session.add(users)
        db.session.commit()
        return redirect('/management/user/<id>')

    return render_template('admin-kasir/editUser.html', users=users)
    
def hapus(id):
    if request.method == 'POST':
        user = User.query.filter_by(id=id).first()

        if not user:
            return response.badRequest([],'Data user kosong....')
        
        db.session.delete(user)
        db.session.commit()
        return redirect('/management/user')

    return render_template('admin-kasir/hapusUser.html')

# Login
def login():
    email = request.form['email']
    password = request.form['password']

    user = User.query.filter_by(email=email).first()

    if not user:
        return response.badRequest([],'Email tidak ditemukan!')

    if not user.checkPassword(password):
        return response.badRequest([],'Password Salah!')

    expires = datetime.timedelta(days=7)
    expires_refresh = datetime.timedelta(days=7)

    access_token = create_access_token(fresh=True, expires_delta=expires)
    refresh_token = create_refresh_token(expires_delta=expires_refresh)

    if user.id_level == 1 or 2:
        return render_template('admin-kasir/home.html')
    if user.id_level == 3:
        return render_template('pelanggan/home.html')    