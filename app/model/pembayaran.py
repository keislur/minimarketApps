from app import db

class Pembayaran(db.Model):
    id = db.Column(db.BigInteger, primary_key = True, autoincrement=True)
    pembayaran = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Pembayaran {}>'.format(self.name)