from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
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
    return  render_template('projet.html')

@bp.route('/taches')
def taches():
    return  render_template('taches.html')

@bp.route('/equipes')
def equipes():
    return  render_template('equipes.html')

@bp.route('/employes')
def employes():
    return  render_template('employes.html')

@bp.route('/rapports')
def rapports():
    return  render_template('rapports.html')


