from app.model.level import Level
from app import response, app, db
from flask import jsonify, redirect, request
from flask import render_template

# GET DATA
def index():
    levels = Level.query.all()
    return render_template('admin-kasir/viewLevel.html', levels = levels)

# GET DATA BY DETAIL 
def detail(id):
    level = Level.query.filter_by(id=id).first()
    if not level:
        return response.badRequest([],'Data Tidak Ada!')
    
    return render_template('admin-kasir/detailLevel.html', level=level)

# POST DATA
def save():
        level = request.form['level']
        levels = Level(level=level)
        db.session.add(levels)
        db.session.commit()

        return redirect('/management/level')
    
# UPDATE DATA
def ubah(id):
    level = Level.query.filter_by(id=id).first()
    if request.method == 'POST':
        if not levels:
            return response.badRequest([],'Data Tidak Ada!')
        
        db.session.delete(level)
        db.session.commit()

        level = request.form['level']
        levels = Level(level=level)

        db.session.add(level)
        db.session.commit()
        return redirect('/management/level/<id>')

    return render_template('admin-kasir/editLevel.html', levels=levels)

def hapus(id):
    level = Level.query.filter_by(id=id).first()
    if request.method == 'POST':
        if not level:
            return response.badRequest([],'Data level kosong....')

        db.session.delete(level)
        db.session.commit()
        return redirect('/management/level')
    return render_template('admin-kasir/hapusLevel.html')