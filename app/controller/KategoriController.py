from app.model.kategori import Kategori
from app import response, app, db
from flask import jsonify, redirect, request
from flask import render_template

# GET DATA
def index():
    kategoris = Kategori.query.all()
    return render_template('admin-kasir/viewKategori.html', kategoris = kategoris)

# GET DATA BY DETAIL 
def detail(id):
    kategori = Kategori.query.filter_by(id=id).first()
    if not kategori:
        return response.badRequest([],'Data Tidak Ada!')
    
    return render_template('admin-kasir/detailKategori.html', kategori=kategori)

# POST DATA
def save():
    kategori = request.form['kategori']
    kategoris = Kategori(kategori=kategori)
    db.session.add(kategoris)
    db.session.commit()

    return redirect('/management/kategori')
    
# UPDATE DATA
def ubah(id):
    kategori = Kategori.query.filter_by(id=id).first()
    if request.method == 'POST':
        if not kategoris:
            return response.badRequest([],'Data Tidak Ada!')
        
        db.session.delete(kategori)
        db.session.commit()

        kategori = request.form['kategori']
        kategoris = Kategori(kategori=kategori)

        db.session.add(kategori)
        db.session.commit()
        return redirect('/management/kategori/<id>')

    return render_template('admin-kasir/editKategori.html', kategoris=kategoris)

def hapus(id):
    kategori = Kategori.query.filter_by(id=id).first()
    if request.method == 'POST':
        if not kategori:
            return response.badRequest([],'Data kategori kosong....')

        db.session.delete(kategori)
        db.session.commit()
        return redirect('/management/kategori')
    return render_template('admin-kasir/hapusKategori.html')