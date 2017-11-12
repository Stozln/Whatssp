from flask import Flask, session, request, redirect, url_for

from flask import render_template
from flask import flash


app=Flask(__name__)


usuarios=["admin"]
passwords=["1234"]


@app.route("/registrarse",methods=['GET','POST'])

def registrarse():
	global usuarios, password

	if request.method=="POST":
		if request.form["usuarios"]!="" and request.form["password"]!="" and request.form["password2"]!="":

			usuario=request.form["usuarios"]
			password=request.form["password"]
			password2=request.form["password2"]

			if password==password2:


				if usuario in usuarios:
					print("NO SE ENCUENTRA DISPONIBLE")
				else:
					usuarios.append(usuario)
					passwords.append(password)
					return redirect(url_for("login"))


	return render_template("registrarse.html")


@app.route("/",methods=['GET','POST'])
def login():
	global usuarios, password

	if request.method=="POST":
		if request.form["usuarios"]!="" and request.form["password"]!="":
			usuario=request.form["usuarios"]
			password=request.form["password"]

			if usuario in usuarios and password in passwords:
				i=usuarios.index(usuario)
				if password == passwords[i]:
					return redirect(url_for("session"))
				else:
					print("key invalida")
			else:
				print("usuario invalido")

	return render_template("login.html")
@app.route("/session",methods=['GET','POST'])

def session():
	return render_template("session.html")

if __name__=="__main__":
	app.run(debug=True)