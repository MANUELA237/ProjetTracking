from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'


class Projet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=False)
    date_debut = db.Column(db.String(200), nullable=False)
    date_fin = db.Column(db.String(200), nullable=False)
    equipe = db.Column(db.String(200), nullable=False)
    client = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Projet {self.nom}>'


class Taches(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=False)
    date_debut = db.Column(db.String(200), nullable=False)
    date_fin = db.Column(db.String(200), nullable=False)
    projet = db.Column(db.String(200), nullable=False)
    employes = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Taches {self.nom}>'


class Equipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(120), unique=True, nullable=False)
    specialite = db.Column(db.String(200), nullable=False)
    employes = db.relationship('Employes', backref='equipe', lazy=True)

    def __repr__(self):
        return f'<Equipes {self.nom}>'



class Employes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    poste = db.Column(db.String(120), nullable=False)
    equipe_id = db.Column(db.Integer, db.ForeignKey('equipes.id'), nullable=False)

    def __repr__(self):
        return f'<Employes {self.nom}>'


class Rapports(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=False)
    date_debut = db.Column(db.String(200), nullable=False)
    date_fin = db.Column(db.String(200), nullable=False)
    equipe = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<rapports {self.nom}>'
