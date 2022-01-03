from db import *
from models import *
from flask import render_template,request
from flask_login import login_required, current_user

##############################
######### PROFILE  ###########
##############################

@app.route("/p")
@login_required
def own_profile():
    return render_template("profil.html", user=current_user, chat=False)


@app.route("/p/<string:id>")
@login_required
def profil(id):
    "page profil de base n'importe qui peut y accèder du moment qu'il a accès à l'id de l'utilisateur"
    usr = users.User.query.get(id)
    if usr == None:
        return '404'
    chat = True
    if id == current_user.id:
        chat = False
    print(chat)
    return render_template("profil.html", user=usr, chat=chat)

@app.route("/pe",methods=['GET','POST'])
@login_required
def profilmodif():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("mail")
        numero = request.form.get("numero")
        rue = request.form.get("rue")
        ville = request.form.get("ville")
        codepostal = request.form.get("codepostal")
        adressemodif = adresses.Adresse.query.filter_by(id=current_user.id_adresse).first()
        if not users.User.query.filter_by(username=username).first():
            utilisateur = users.User.query.get(current_user.id)
            print(username)
            utilisateur.username = username
            db.session.commit()
            print("commit lol")
            

        
    adressereelle = adresses.Adresse.query.filter_by(id=current_user.id_adresse).first()
    return render_template("profilmodif.html",user=current_user,adressereelle=adressereelle)