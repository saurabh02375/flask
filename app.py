import os
from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/admin")
def admin():
    if 'username' in session:
        posts = Post.query.all()
        return render_template("dashboard.html", posts=posts)
    return redirect(url_for('login'))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['username'] = username
            return redirect(url_for('admin'))
        else:
            return "Invalid credentials"
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route("/admin/create", methods=["GET", "POST"])
def create_post():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        new_post = Post(title=title, description=description)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template("create_post.html")

@app.route("/admin/edit/<int:id>", methods=["GET", "POST"])
def edit_post(id):
    if 'username' not in session:
        return redirect(url_for('login'))
    post = Post.query.get_or_404(id)
    if request.method == "POST":
        post.title = request.form["title"]
        post.description = request.form["description"]
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template("edit_post.html", post=post)

@app.route("/admin/delete/<int:id>")
def delete_post(id):
    if 'username' not in session:
        return redirect(url_for('login'))
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('admin'))

def create_user(username, password):
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)


  