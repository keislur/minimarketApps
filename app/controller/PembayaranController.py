from app.model.pembayaran import Pembayaran
from app import response, app, db
from flask import jsonify, redirect, request
from flask import render_template

# GET DATA
def index():
    pembayarans = Pembayaran.query.all()
    return render_template('admin-kasir/viewPembayaran.html', pembayarans = pembayarans)

# GET DATA BY DETAIL 
def detail(id):
    pembayaran = Pembayaran.query.filter_by(id=id).first()
    if not pembayaran:
        return response.badRequest([],'Data Tidak Ada!')
    
    return render_template('admin-kasir/detailPembayaran.html', pembayaran=pembayaran)

# POST DATA
def save():
    pembayaran = request.form['pembayaran']
    pembayarans = Pembayaran(pembayaran=pembayaran)
    db.session.add(pembayarans)
    db.session.commit()

    return redirect('/management/pembayaran')
    
# UPDATE DATA
def ubah(id):
    pembayaran = Pembayaran.query.filter_by(id=id).first()
    if request.method == 'POST':
        if not pembayarans:
            return response.badRequest([],'Data Tidak Ada!')
        
        db.session.delete(pembayaran)
        db.session.commit()

        pembayaran = request.form['pembayaran']
        pembayarans = Pembayaran(pembayaran=pembayaran)

        db.session.add(pembayaran)
        db.session.commit()
        return redirect('/management/pembayaran/<id>')

    return render_template('admin-kasir/editPembayaran.html', pembayarans=pembayarans)

def hapus(id):
    pembayaran = Pembayaran.query.filter_by(id=id).first()
    if request.method == 'POST':
        if not pembayaran:
            return response.badRequest([],'Data pembayaran kosong....')

        db.session.delete(pembayaran)
        db.session.commit()
        return redirect('/management/pembayaran')
    return render_template('admin-kasir/hapusPembayaran.html')