from app import db
from app.model.kategori import Kategori

class Barang(db.Model):
    id = db.Column(db.BigInteger, primary_key = True, autoincrement=True)
    id_kategori = db.Column(db.BigInteger, db.ForeignKey(Kategori.id, ondelete='CASCADE'))
    kode = db.Column(db.BigInteger, nullable=False)
    nama = db.Column(db.String(50), nullable=False)
    harga = db.Column(db.BigInteger, nullable=False)
    stok = db.Column(db.BigInteger, nullable=False)
    penjual = db.Column(db.String(50), nullable=False)
    lokasi = db.Column(db.String(50), nullable=False)
    deskripsi = db.Column(db.String(250), nullable=False)
    terjual = db.Column(db.BigInteger, nullable=False, default = 0)
    rating = db.Column(db.BigInteger, nullable=False, default = 0)
    rating_5 = db.Column(db.BigInteger, nullable=False, default = 0)
    rating_4 = db.Column(db.BigInteger, nullable=False, default = 0)
    rating_3 = db.Column(db.BigInteger, nullable=False, default = 0)
    rating_2 = db.Column(db.BigInteger, nullable=False, default = 0)
    rating_1 = db.Column(db.BigInteger, nullable=False, default = 0)
    rekomendasi = db.Column(db.String(50), nullable=False, default = "Belum ada penilaian")

    def __repr__(self):
        return '<Barang {}>'.format(self.name)