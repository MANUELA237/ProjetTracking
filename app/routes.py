from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Projet, Taches, Equipes, Employes,Rapports
from . import db

bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Vérification des informations d'identification
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['username'] = user.nom  # Stocker le nom d'utilisateur dans la session
            return redirect(url_for('main.dashboard', username=user.nom))
        else:
            flash("Identifiants invalides.")  # Message d'erreur si les identifiants sont incorrects

    return render_template('index.html')


@bp.route('/inscrire', methods=['GET', 'POST'])
def inscription():
    if request.method == 'POST':
        nom = request.form['nom']
        email = request.form['email']
        password = request.form['password']
        confirmpassword = request.form['confirmer']

        # Vérification des mots de passe
        if password != confirmpassword:
            return render_template('inscription.html', error="Les mots de passe ne correspondent pas.")

        # Vérification de l'email existant
        if User.query.filter_by(email=email).first():
            return render_template('inscription.html', error="Cet email est déjà utilisé.")

        # Création d'un nouvel utilisateur
        new_user = User(nom=nom, email=email, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('inscription.html')


"""@bp.route('/bienvenue/<username>')
def bienvenue(username):
    return render_template('bienvenue.html', username=username)"""


@bp.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('main.index'))  # Rediriger vers la page d'accueil si non connecté
    return render_template('dashboard.html', username=session['username'])


@bp.route('/logout')
def logout():
    session.pop('username', None)
    flash("Vous êtes déconnecté.")  # Message de déconnexion
    return redirect(url_for('main.index'))  # Rediriger vers la page d'accueil après déconnexion


@bp.route('/projet')
def projet():

    # Récupérer tous les projets
    projet = Projet.query.all()
    return render_template('projet.html', projets=projet)


@bp.route('/taches')
def taches():
    return render_template('taches.html')


@bp.route('/equipes')
def equipes():
    return render_template('equipes.html')


@bp.route('/employes')
def employes():
    return render_template('employes.html')


@bp.route('/rapports')
def rapports():
    # Récupérer tous les projets
    rapport = Rapports.query.all()
    return render_template('rapports.html', rapports=rapport)



@bp.route('/modalprojet', methods=['POST', 'GET'])
def modalprojet():
    if request.method == 'POST':
        nom = request.form['nom']
        description = request.form['description']
        date_debut = request.form['date_debut']
        date_fin = request.form['date_fin']
        equipe = request.form['equipe']
        client = request.form['client']


        # verification du projet existant
        if Projet.query.filter_by(nom=nom).first():
            return render_template('projet.html', error="ce pojet existe deja")

        # creation d un nouveau projet
        new_projet = Projet(nom=nom, description=description, date_debut=date_debut, date_fin=date_fin, equipe=equipe, client=client)
        db.session.add(new_projet)
        db.session.commit()

        return redirect(url_for('main.projet'))
    return render_template('projet.html')


@bp.route('/modaltaches', methods=['POST', 'GET'])
def modaltaches():
    if request.method == 'POST':
        nom = request.form['nom']
        description = request.form['description']
        date_debut = request.form['date_debut']
        date_fin = request.form['date_fin']
        projet = request.form['projet']
        employes = request.form['employes']

        # Vérification du projet existant
        if Taches.query.filter_by(nom=nom).first():  # Utilisation correcte du modèle
            return render_template('taches.html', error="cette tache existe déjà")

        # Création d'une nouvelle tâche
        new_taches = Taches(nom=nom, description=description, date_debut=date_debut, date_fin=date_fin, projet=projet,
                            employes=employes)
        db.session.add(new_taches)
        db.session.commit()

        return redirect(url_for('main.taches'))
    return render_template('taches.html')


@bp.route('/modalequipes', methods=['POST', 'GET'])
def modalequipes():
    if request.method == 'POST':
        nom = request.form['nom']
        specialite = request.form['specialite']
        employe_ids = request.form.getlist('employes')  # Récupérer les IDs des employés sélectionnés

        # Vérification d'une équipe existante
        if Equipes.query.filter_by(nom=nom).first():  # Utilisation correcte du modèle
            return render_template('equipes.html', error="cette équipe existe déjà")

        # Création d'une nouvelle équipe
        new_equipes = Equipes(nom=nom, employes=employes, specialite=specialite,)
        db.session.add(new_equipes)
        db.session.commit()

        # Lier les employés à l'équipe
        for employe_id in employe_ids:
            employe = Employes.query.get(employe_id)
            if employe:
                employe.equipe_id = new_equipes.id  # Lier l'employé à l'équipe
                db.session.commit()

        return redirect(url_for('main.equipes'))
    return render_template('equipes.html')


@bp.route('/modalemployes', methods=['POST', 'GET'])
def modalemployes():
    if request.method == 'POST':
        nom = request.form['nom']
        email = request.form['email']
        poste = request.form['poste']

        # Vérification d'un employé existant
        if Employes.query.filter_by(nom=nom).first():  # Utilisation correcte du modèle
            return render_template('employes.html', error="cet employé existe déjà")

        # Création d'un nouvel employé
        new_employes = Employes(nom=nom, email=email, poste=poste)
        db.session.add(new_employes)
        db.session.commit()

        return redirect(url_for('main.employes'))
    return render_template('employes.html')


