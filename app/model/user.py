from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app.model.level import Level

class User(db.Model):
    id = db.Column(db.BigInteger, primary_key = True, autoincrement=True)
    nama = db.Column(db.String(50), nullable = False)
    username = db.Column(db.String(50), index = True, unique = True, nullable = False)
    password = db.Column(db.String(250), nullable=False)
    id_level = db.Column(db.BigInteger, db.ForeignKey(Level.id, ondelete='CASCADE'))
    alamat = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    no_telp = db.Column(db.BigInteger, nullable=False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.name)
    
    def setPassword(self,password):
        self.password = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.password, password)