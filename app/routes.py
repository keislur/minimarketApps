from app import app, response
from app.controller import LevelController
from app.controller import UserController
from app.controller import KategoriController
from app.controller import PembayaranController
from app.controller import BarangController
from app.controller import TransaksiController
from app.controller import HomeController
from flask import render_template
from flask import request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

# Homepage
@app.route('/')
def index():
    return "Hello World"

# Autentikasi
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return response.success(current_user, 'Sukses!')


# ------------------------------------------------ Autentikasi User ------------------------------------------------------
# Login
@app.route('/login', methods=['POST'])
def logins():
    return UserController.login()

# Logout
# @app.route('/logout', methods=['POST'])
# def logouts():
#     return UserController.logout()


# ------------------------------------------------ Home Kasir & Admin ------------------------------------------------------
@app.route('/management', methods=['GET'])
def manage():
    currentRole = get_jwt_identity().get('id_level')
    if currentRole == 1 or 2:
        return HomeController.manage()
    else:
        return response.badRequest([],'Anda tidak memiliki hak akses!')


# ------------------------------------------------ User Controller ------------------------------------------------------
@app.route('/management/user', methods=['GET', 'POST'])
@jwt_required()
def users():
    currentRole = get_jwt_identity().get('id_level')
    if currentRole == 1:
        if request.method == 'GET':
            return UserController.index()
        else:
            return UserController.save()
    else:
        return response.badRequest([],'Anda tidak memiliki hak akses!')


@app.route('/management/user/<id>', methods=['GET', 'POST'])
@jwt_required()
def detailUser(id):
    currentRole = get_jwt_identity().get('id_level')
    if currentRole == 1:
        if request.method == 'GET':
            return UserController.detail(id)
        elif request.method == 'POST':
            return UserController.ubah(id)
    else:
        return response.badRequest([],'Anda tidak memiliki hak akses!')
    
@app.route('/management/user/<id>/delete', methods=['GET','POST'])
@jwt_required()
def hapusUser(id):
    currentRole = get_jwt_identity().get('id_level')
    if currentRole == 1:
        return UserController.hapus(id)
    else:
        return response.badRequest([],'Anda tidak memiliki hak akses!')

    
# ------------------------------------------------ Level Controller ------------------------------------------------------
@app.route('/management/level', methods=['GET', 'POST'])
@jwt_required()
def levels():
    currentRole = get_jwt_identity().get('id_level')
    if currentRole == 1:
        if request.method == 'GET':
            return LevelController.index()
        else:
            return LevelController.save()
    else:
        return response.badRequest([],'Anda tidak memiliki hak akses!')
        

@app.route('/management/level/<id>', methods=['GET', 'POST'])
@jwt_required()
def detailLevel(id):
    currentRole = get_jwt_identity().get('id_level')
    if currentRole == 1:
        if request.method == 'GET':
            return LevelController.detail(id)
        elif request.method == 'POST':
            return LevelController.ubah(id)
    else:
        return response.badRequest([],'Anda tidak memiliki hak akses!')
    
@app.route('/management/level/<id>/delete', methods=['GET','POST'])
@jwt_required()
def hapusLevel(id):
    currentRole = get_jwt_identity().get('id_level')
    if currentRole == 1:
        return LevelController.hapus(id)
    else:
        return response.badRequest([],'Anda tidak memiliki hak akses!')
    

# ------------------------------------------------ Kategori Controller ------------------------------------------------------
@app.route('/management/kategori', methods=['GET', 'POST'])
@jwt_required()
def Kategoris():
    currentRole = get_jwt_identity().get('id_level')
    if currentRole == 1:
        if request.method == 'GET':
            return KategoriController.index()
        else:
            return KategoriController.save()
    else:
        return response.badRequest([],'Anda tidak memiliki hak akses!')

@app.route('/management/kategori/<id>', methods=['GET', 'POST'])
@jwt_required()
def detailKategori(id):
    currentRole = get_jwt_identity().get('id_level')
    if currentRole == 1:
        if request.method == 'GET':
            return KategoriController.detail(id)
        elif request.method == 'POST':
            return KategoriController.ubah(id)
    else:
        return response.badRequest([],'Anda tidak memiliki hak akses!')

@app.route('/management/kategori/<id>/delete', methods=['GET','POST'])
@jwt_required()
def hapusKategori(id):
    currentRole = get_jwt_identity().get('id_level')
    if currentRole == 1:
        return KategoriController.hapus(id)
    else:
        return response.badRequest([],'Anda tidak memiliki hak akses!')
        
    
# ------------------------------------------------ Pembayaran Controller ------------------------------------------------------
@app.route('/management/pembayaran', methods=['GET', 'POST'])
@jwt_required()
def Pembayarans():
    currentRole = get_jwt_identity().get('id_level')
    if currentRole == 1:
        if request.method == 'GET':
            return PembayaranController.index()
        else:
            return PembayaranController.save()
    else:
        return response.badRequest([],'Anda tidak memiliki hak akses!')

@app.route('/management/pembayaran/<id>', methods=['GET', 'POST'])
@jwt_required()
def detailPembayaran(id):
    currentRole = get_jwt_identity().get('id_level')
    if currentRole == 1:
        if request.method == 'GET':
            return PembayaranController.detail(id)
        elif request.method == 'POST':
            return PembayaranController.ubah(id)
    else:
        return response.badRequest([],'Anda tidak memiliki hak akses!')

@app.route('/management/pembayaran/<id>/delete', methods=['GET','POST'])
@jwt_required()
def hapusPembayaran(id):
    currentRole = get_jwt_identity().get('id_level')
    if currentRole == 1:
        return PembayaranController.hapus(id)
    else:
        return response.badRequest([],'Anda tidak memiliki hak akses!')
    

# ------------------------------------------------ Barang Controller ------------------------------------------------------
@app.route('/management/barang', methods=['GET', 'POST'])
@jwt_required()
def Barangs():
    currentRole = get_jwt_identity().get('id_level')
    if currentRole == 1:
        if request.method == 'GET':
            return BarangController.index()
        else:
            return BarangController.save()
    else:
        return response.badRequest([],'Anda tidak memiliki hak akses!')

@app.route('/management/barang/<id>', methods=['GET', 'POST'])
@jwt_required()
def detailBarang(id):
    currentRole = get_jwt_identity().get('id_level')
    if currentRole == 1:
        if request.method == 'GET':
            return BarangController.detail(id)
        elif request.method == 'POST':
            return BarangController.ubah(id)
    else:
        return response.badRequest([],'Anda tidak memiliki hak akses!')
    
@app.route('/management/barang/<id>/delete', methods=['GET','POST'])
@jwt_required()
def hapusBarang(id):
    currentRole = get_jwt_identity().get('id_level')
    if currentRole == 1:
        return BarangController.hapus(id)
    else:
        return response.badRequest([],'Anda tidak memiliki hak akses!')


# ------------------------------------------------ Transaksi Controller ------------------------------------------------------
@app.route('/management/transaksi', methods=['GET', 'POST'])
@jwt_required()
def Transaksis():
    currentRole = get_jwt_identity().get('id_level')
    if currentRole == 1 or 2:
        if request.method == 'GET':
            return TransaksiController.index()
        else:
            return TransaksiController.save()
    else:
        return response.badRequest([],'Anda tidak memiliki hak akses!')

@app.route('/management/transaksi/<id>', methods=['GET', 'POST'])
@jwt_required()
def detailTransaksi(id):
    currentRole = get_jwt_identity().get('id_level')
    if currentRole == 1 or 2:
        if request.method == 'GET':
            return TransaksiController.detail(id)
        elif request.method == 'POST':
            return TransaksiController.ubah(id)
    else:
        return response.badRequest([],'Anda tidak memiliki hak akses!')
    
@app.route('/management/transaksi/<id>/delete', methods=['GET','POST'])
@jwt_required()
def hapusTransaksi(id):
    currentRole = get_jwt_identity().get('id_level')
    if currentRole == 1:
        return TransaksiController.hapus(id)
    else:
        return response.badRequest([],'Anda tidak memiliki hak akses!')