from app import db

class Level(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    level = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Level {}>'.format(self.name)