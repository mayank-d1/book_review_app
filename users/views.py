from app import app
from flask import render_template

print(app)
@app.route("/register", methods=["POST", "GET"])
def register(request):
    if request.methods == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        name = request.form.get("name")
    else:
        render_template("register.html")

