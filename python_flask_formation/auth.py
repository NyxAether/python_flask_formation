from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from tinydb import where

from . import db
from .models import User

bp = Blueprint("auth", __name__, url_prefix="/auth")


# Routes blueprint


@bp.route("/login", methods=["GET"])
def login():
    if "username" in request.args:
        # Récupérer les identifiants du formulaire
        username = request.args["username"]
        password = request.args["password"]

        # Vérifier que l'utilisateur existe
        users = db.table("users").search(where("username") == username)
        if users != []:
            if users[0]["password"] == password:
                login_user(User(username))
                return redirect(url_for("index"))
    return render_template("login.html")


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))
