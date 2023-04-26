from app.model.barang import Barang
from app import response, app, db
from flask import jsonify, request

# GET DATA
def index():
    try:
        barang = Barang.query.all()
        data = formatArray(barang)
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
        'id_kategori' : data.id_kategori,
        'kode' : data.kode,
        'nama' : data.nama,
        'harga' : data.harga,
        'stok' : data.stok,
        'penjual' : data.penjual,
        'lokasi' : data.lokasi,
        'deskripsi' : data.deskripsi,
        'terjual' : data.terjual,
        'rating' : data.rating,
        'rating_5' : data.rating_5,
        'rating_4' : data.rating_4,
        'rating_3' : data.rating_3,
        'rating_2' : data.rating_2,
        'rating_1' : data.rating_1,
        'rekomendasi' : data.rekomendasi,
    }
    return data


# GET DATA BY DETAIL 
def detail(id):
    try:

        barang = Barang.query.filter_by(id=id).first()
        if not barang:
            return response.badRequest([],'Data Level kosong....')
        
        data = singleObject(barang)

        return response.success(data,'Sukses View Data!')
    except Exception as e:
        return(e)


# POST DATA
def save():
    try:
        id_kategori = request.form.get('id_kategori')
        kode = request.form.get('kode')
        nama = request.form.get('nama')
        harga = request.form.get('harga')
        stok = request.form.get('stok')
        penjual = request.form.get('penjual')
        lokasi = request.form.get('lokasi')
        deskripsi = request.form.get('deskripsi')
        
        input = [
            {
                'id_kategori' : id_kategori,
                'kode' : kode,
                'nama' : nama,
                'harga' : harga,
                'stok' : stok,
                'penjual' : penjual,
                'lokasi' : lokasi,
                'deskripsi' : deskripsi
            }
        ]
        
        barangs = Barang(id_kategori=id_kategori, kode=kode, nama=nama, harga=harga, stok=stok, penjual=penjual, lokasi=lokasi, deskripsi=deskripsi)
        
        db.session.add(barangs)
        db.session.commit()

        return response.success(input,'Sukses Menambahkan Data!')
    except Exception as e:
        return(e)
    

# UPDATE DATA
def ubah(id):
    try:
        id_kategori = request.form.get('id_kategori')
        kode = request.form.get('kode')
        nama = request.form.get('nama')
        harga = request.form.get('harga')
        stok = request.form.get('stok')
        penjual = request.form.get('penjual')
        lokasi = request.form.get('lokasi')
        deskripsi = request.form.get('deskripsi')
        terjual = request.form.get('terjual')
        rating = request.form.get('rating')
        rating_5 = request.form.get('rating_5')
        rating_4 = request.form.get('rating_4')
        rating_3 = request.form.get('rating_3')
        rating_2 = request.form.get('rating_2')
        rating_1 = request.form.get('rating_1')
        rekomendasi = request.form.get('rekomendasi')

        input = [
            {
            'id_kategori' : id_kategori,
            'kode' : kode,
            'nama' : nama,
            'harga' : harga,
            'stok' : stok,
            'penjual' : penjual,
            'lokasi' : lokasi,
            'deskripsi' : deskripsi,
            'terjual' : terjual,
            'rating' : rating,
            'rating_5' : rating_5,
            'rating_4' : rating_4,
            'rating_3' : rating_3,
            'rating_2' : rating_2,
            'rating_1' : rating_1,
            'rekomendasi' : rekomendasi
            }
        ]

        barangs = Barang.query.filter_by(id=id).first()
        barangs.id_kategori = id_kategori
        barangs.kode = kode
        barangs.nama = nama
        barangs.harga = harga
        barangs.stok = stok
        barangs.penjual = penjual
        barangs.lokasi = lokasi
        barangs.deskripsi = deskripsi
        barangs.terjual = terjual
        barangs.rating = rating
        barangs.rating_5 = rating_5
        barangs.rating_4 = rating_4
        barangs.rating_3 = rating_3
        barangs.rating_2 = rating_2
        barangs.rating_1 = rating_1
        barangs.rekomendasi = rekomendasi

        db.session.commit()

        return response.success(input,'Sukses Edit Data!')
    except Exception as e:
        return(e)
    
def hapus(id):
    try:
        barang = Barang.query.filter_by(id=id).first()
        if not barang:
            return response.badRequest([],'Data barang kosong....')
        
        db.session.delete(barang)
        db.session.commit()

        return response.success('','Sukses Hapus Data!')

    except Exception as e:
        print(e)
