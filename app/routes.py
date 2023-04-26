from app import app, response
from app.controller import LevelController
from app.controller import UserController
from app.controller import KategoriController
from app.controller import PembayaranController
from app.controller import BarangController
from app.controller import TransaksiController
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


# ------------------------------------------------ User Controller ------------------------------------------------------
@app.route('/user', methods=['GET', 'POST'])
# @jwt_required()
def users():
    # currentRole = get_jwt_identity().get('id_level')
    # if currentRole == 1:
        if request.method == 'GET':
            return UserController.index()
        else:
            return UserController.save()
    # else:
    #     return response.badRequest([],'Anda tidak memiliki hak akses!')


@app.route('/user/<id>', methods=['GET', 'PUT','DELETE'])
@jwt_required()
def detailUser(id):
    currentRole = get_jwt_identity().get('id_level')
    if currentRole == 1:
        if request.method == 'GET':
            return UserController.detail(id)
        elif request.method == 'PUT':
            return UserController.ubah(id)
        elif request.method == 'DELETE':
            return UserController.hapus(id)
    else:
        return response.badRequest([],'Anda tidak memiliki hak akses!')



# ------------------------------------------------ Level Controller ------------------------------------------------------
@app.route('/level', methods=['GET', 'POST'])
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
        

@app.route('/level/<id>', methods=['GET', 'PUT','DELETE'])
@jwt_required()
def detailLevel(id):
    currentRole = get_jwt_identity().get('id_level')
    if currentRole == 1:
        if request.method == 'GET':
            return LevelController.detail(id)
        elif request.method == 'PUT':
            return LevelController.ubah(id)
        elif request.method == 'DELETE':
            return LevelController.hapus(id)
    else:
        return response.badRequest([],'Anda tidak memiliki hak akses!')
    

# ------------------------------------------------ Kategori Controller ------------------------------------------------------
@app.route('/kategori', methods=['GET', 'POST'])
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


@app.route('/kategori/<id>', methods=['GET', 'PUT','DELETE'])
@jwt_required()
def detailKategori(id):
    currentRole = get_jwt_identity().get('id_level')
    if currentRole == 1:
        if request.method == 'GET':
            return KategoriController.detail(id)
        elif request.method == 'PUT':
            return KategoriController.ubah(id)
        elif request.method == 'DELETE':
            return KategoriController.hapus(id)
    else:
        return response.badRequest([],'Anda tidak memiliki hak akses!')
        
    

# ------------------------------------------------ Pembayaran Controller ------------------------------------------------------
@app.route('/pembayaran', methods=['GET', 'POST'])
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

@app.route('/pembayaran/<id>', methods=['GET', 'PUT','DELETE'])
@jwt_required()
def detailPembayaran(id):
    currentRole = get_jwt_identity().get('id_level')
    if currentRole == 1:
        if request.method == 'GET':
            return PembayaranController.detail(id)
        elif request.method == 'PUT':
            return PembayaranController.ubah(id)
        elif request.method == 'DELETE':
            return PembayaranController.hapus(id)
    else:
        return response.badRequest([],'Anda tidak memiliki hak akses!')


# ------------------------------------------------ Barang Controller ------------------------------------------------------
@app.route('/barang', methods=['GET', 'POST'])
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

@app.route('/barang/<id>', methods=['GET', 'PUT','DELETE'])
@jwt_required()
def detailBarang(id):
    currentRole = get_jwt_identity().get('id_level')
    if currentRole == 1:
        if request.method == 'GET':
            return BarangController.detail(id)
        elif request.method == 'PUT':
            return BarangController.ubah(id)
        elif request.method == 'DELETE':
            return BarangController.hapus(id)
    else:
        return response.badRequest([],'Anda tidak memiliki hak akses!')
    

# ------------------------------------------------ Transaksi Controller ------------------------------------------------------
@app.route('/transaksi', methods=['GET', 'POST'])
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

@app.route('/transaksi/<id>', methods=['GET', 'PUT','DELETE'])
@jwt_required()
def detailTransaksi(id):
    currentRole = get_jwt_identity().get('id_level')
    if currentRole == 1 or 2:
        if request.method == 'GET':
            return TransaksiController.detail(id)
        elif request.method == 'PUT':
            return TransaksiController.ubah(id)
        elif request.method == 'DELETE':
            return TransaksiController.hapus(id)
    else:
        return response.badRequest([],'Anda tidak memiliki hak akses!')