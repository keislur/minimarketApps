from app import response, app, db
from flask import jsonify, request
from flask import render_template

def index():
    return render_template('pelanggan/home.html')

def manage():
    return render_template('admin-kasir/home.html')