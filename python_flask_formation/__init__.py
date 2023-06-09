from flask import Flask, redirect, render_template
from flask_login import LoginManager, login_required, current_user
from tinydb import TinyDB, where
from .models import User


# Démarrer l'application flask
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Création de la base de données
db = TinyDB("python_flask_formation/db.json")

# Création du login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"


# Recherche utilisateur
@login_manager.user_loader
def load_user(username):
    if db.table("users").search(where("username") == username) != []:
        return User(username)
    else:
        return None


# Blueprint auth
from . import auth

app.register_blueprint(auth.bp)


# Route index
@app.route("/")
@login_required
def index():
    print(current_user.get_id())
    return redirect("genre/rock")


@app.route("/genre/<genre>")
@login_required
def view_genres(genre):
    genres = db.table("genres").all()
    current_genre = db.table("genres").search(where("id") == genre)[0]
    artists_by_genre = db.table("artists").search(where("genreId") == genre)
    return render_template(
        "index.html",
        genres=genres,
        current_genre=current_genre,
        artists=artists_by_genre,
    )
