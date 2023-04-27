from app import response, app, db
from flask import jsonify, request
from app.model.transaksi import Transaksi, DetailTransaksi
from app.model.barang import Barang
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
    total_price = 0
    detail_transaksi = request.json['detail_transaksi']

    new_transaksi = Transaksi(
        id_user = id_user,
        id_pembayaran = id_pembayaran,
        total_price = total_price
    )

    for dt in detail_transaksi:
        id_barang = dt['id_barang']
        qty = dt['qty']
        barang = Barang.query.filter_by(id=id_barang).first()
        price = barang.harga * qty
        total_price += price
        if not barang:
            return response.badRequest([], 'Barang tidak ditemukan!')
        
        new_detail_transaksi = DetailTransaksi(
            id_barang = id_barang,
            qty = qty,
            price = price
        )
        new_transaksi.detail_transaksi.append(new_detail_transaksi)
    
    new_transaksi.total_price = total_price

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
    new_detail_transaksi_list = []
    for dt in detail_transaksi:
        id_barang = dt['id_barang']
        barang = Barang.query.filter_by(id=id_barang).first()
        qty = dt['qty']
        price = barang.harga * qty

        new_detail_transaksi = DetailTransaksi(
            id_barang=id_barang,
            qty=qty,
            price=price
        )

        new_detail_transaksi_list.append(new_detail_transaksi)

    # hitung total harga baru berdasarkan detail transaksi yang baru
    total_price = sum(dt.price for dt in new_detail_transaksi_list)
    transaksi.detail_transaksi = new_detail_transaksi_list
    transaksi.total_price = total_price

    transaksi.updated_at = datetime.utcnow()
    db.session.commit()

    return response.success('', 'Sukses mengubah data!')
    
def hapus(id):
    transaksi = Transaksi.query.filter_by(id=id).first()

    if not transaksi:
        return response.badRequest([], 'Transaksi tidak ditemukan!')
    
    # Remove all detail transaksi associated with the transaksi
    for dt in transaksi.detail_transaksi:
        db.session.delete(dt)

    db.session.delete(transaksi)
    db.session.commit()

    return response.success('', 'Transaksi berhasil dihapus!')