from app import response, app, db
from flask import jsonify, request
from app.model.transaksi import Transaksi, DetailTransaksi
from datetime import datetime

def index():
    transaksis = Transaksi.query.all()
    output = []

    for transaksi in transaksis:
        data = {}
        data['id'] = transaksi.id
        data['user'] = transaksi.id_user
        data['pembayaran'] = transaksi.id_pembayaran
        data['total_price'] = transaksi.total_price
        data['created_at'] = transaksi.created_at
        data['updated_at'] = transaksi.updated_at
        detail_transaksi = []
        for dt in transaksi.detail_transaksi:
            detail_transaksi.append({
                'id': dt.id,
                'id_barang': dt.id_barang,
                'qty': dt.qty,
                'price': dt.price
            })
        data['detail_transaksi'] = detail_transaksi
        output.append(data)

    return response.success(output,'View data!')

def save():
    id_user = request.json['id_user']
    id_pembayaran = request.json['id_pembayaran']
    total_price = request.json['total_price']
    detail_transaksi = request.json['detail_transaksi']

    new_transaksi = Transaksi(
        id_user = id_user,
        id_pembayaran = id_pembayaran,
        total_price = total_price
    )

    for dt in detail_transaksi:
        id_barang = dt['id_barang']
        qty = dt['qty']
        price = dt['price']

        new_detail_transaksi = DetailTransaksi(
            id_barang = id_barang,
            qty = qty,
            price = price
        )
        new_transaksi.detail_transaksi.append(new_detail_transaksi)
    
    db.session.add(new_transaksi)
    db.session.commit()

    return response.success('','Sukses menambahkan data!')

def detail(id):
        transaksi = Transaksi.query.filter_by(id=id).first()
        if not transaksi:
            return response.badRequest([],'Transaksi tidak ditemukan!')

        data = {}
        data['id'] = transaksi.id
        data['user'] = transaksi.id_user
        data['pembayaran'] = transaksi.id_pembayaran
        data['total_price'] = transaksi.total_price
        data['created_at'] = transaksi.created_at
        data['updated_at'] = transaksi.updated_at
        detail_transaksi = []
        for dt in transaksi.detail_transaksi:
            detail_transaksi.append({
                'id': dt.id,
                'id_barang': dt.id_barang,
                'qty': dt.qty,
                'price': dt.price
            })
        data['detail_transaksi'] = detail_transaksi

        return response.success(data,'Sukses edit data!')

def ubah(id):
    transaksi = Transaksi.query.filter_by(id=id).first()

    if not transaksi:
        return response.badRequest([], 'Transaksi tidak ditemukan!')

    id_user = request.json['id_user'] if 'id_user' in request.json else transaksi.id_user
    id_pembayaran = request.json['id_pembayaran'] if 'id_pembayaran' in request.json else transaksi.id_pembayaran
    total_price = request.json['total_price'] if 'total_price' in request.json else transaksi.total_price
    detail_transaksi = request.json['detail_transaksi'] if 'detail_transaksi' in request.json else []

    transaksi.id_user = id_user
    transaksi.id_pembayaran = id_pembayaran
    transaksi.total_price = total_price

    # hapus detail transaksi yang ada saat ini
    for dt in transaksi.detail_transaksi:
        db.session.delete(dt)

    # tambahkan detail transaksi baru
    for dt in detail_transaksi:
        id_barang = dt['id_barang']
        qty = dt['qty']
        price = dt['price']

        new_detail_transaksi = DetailTransaksi(
            id_barang=id_barang,
            qty=qty,
            price=price
        )

        transaksi.detail_transaksi.append(new_detail_transaksi)

    transaksi.updated_at = datetime.utcnow()
    db.session.commit()

    return response.success('', 'Sukses mengubah data!')

def hapus(id):
    transaksi = Transaksi.query.filter_by(id=id).first()

    if not transaksi:
        return response.badRequest([], 'Transaksi tidak ditemukan!')

    db.session.delete(transaksi)
    db.session.commit()

    return response.success('', 'Transaksi berhasil dihapus!')