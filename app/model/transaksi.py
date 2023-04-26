from app import db
from datetime import datetime
from app.model.user import User
from app.model.pembayaran import Pembayaran
from app.model.barang import Barang

class Transaksi(db.Model):
    id = db.Column(db.BigInteger, primary_key = True, autoincrement=True)
    id_user = db.Column(db.BigInteger, db.ForeignKey(User.id, ondelete='CASCADE'))
    id_pembayaran = db.Column(db.BigInteger, db.ForeignKey(Pembayaran.id, ondelete='CASCADE'))
    total_price = db.Column(db.BigInteger, nullable=False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow)
    detail_transaksi = db.relationship('DetailTransaksi', backref='transaksi', lazy=True)

    def __repr__(self):
        return '<Transaksi {}>'.format(self.name)

class DetailTransaksi(db.Model):
    id = db.Column(db.BigInteger, primary_key = True, autoincrement=True)
    id_transaksi = db.Column(db.BigInteger, db.ForeignKey(Transaksi.id, ondelete='CASCADE'), nullable = False)
    id_barang = db.Column(db.BigInteger, db.ForeignKey(Barang.id, ondelete='CASCADE'), nullable = False)
    qty = db.Column(db.BigInteger, nullable=False)
    price = db.Column(db.BigInteger, nullable=False)
    
    def __repr__(self):
        return '<DetailTransaksi {}>'.format(self.name)