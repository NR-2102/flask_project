from flask import Flask, render_template, redirect, url_for, request,session

#creating an instance of class
app = Flask(__name__)
app.secret_key="xyz"
#home page
@app.route("/")
def home():
    return render_template("index2.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    if "user" in session:
        return f"<h1>{usr}</h1>"
    else:
        return redirect(url_for("login"))

if __name__ == "__main__":
    app.run()
