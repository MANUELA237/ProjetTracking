from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable = False)
    password = db.Column(db.String(200), nullable = False)


    def __repr__(self):
        return f'<User {self.email}>'

class Projet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable = False)
    date_debut= db.Column(db.String(200), nullable = False)
    date_fin = db.Column(db.String(200), nullable=False)
    equipe = db.Column(db.String(200), nullable=False)


    def __repr__(self):
        return f'<Projet {self.nom}>'

