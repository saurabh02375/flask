import os
from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from sqlalchemy import text

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)

class Banner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    title2 = db.Column(db.String(200), nullable=False)
    description2 = db.Column(db.Text, nullable=False)
    title3 = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(200), nullable=True)
    title4 = db.Column(db.String(200), nullable=False)

@app.route("/")
def home():
    return render_template("front/home.html")

@app.route("/admin")
def admin():
    if 'username' in session:
        posts = Post.query.all()
        return render_template("admin/dashboard.html", posts=posts)
    return redirect(url_for('login'))

@app.route('/posts')
def posts():
    posts = Post.query.all()
    return render_template('admin/post/index.html', posts=posts)

@app.route('/banners')
def banners():
    banners = Banner.query.all()
    homebanner = Banner.query.filter_by(slug='home').first()
    aboutus = Banner.query.filter_by(slug='aboutus').first()
    return render_template('admin/banner/index.html', homebanner=homebanner, aboutus=aboutus)

@app.route('/admin/banner/store', methods=["POST"])
def store_banner():
    slug = request.form.get('slug', " ")
    title = request.form.get('title', " ")
    description = request.form.get('description', " ")
    title2 = request.form.get('title2', " ")
    description2 = request.form.get('description2', " ")
    title3 = request.form.get('title3', " ")
    title4 = request.form.get('title4', " ")

    if slug == 'home':
        homebanner = Banner.query.filter_by(slug=slug).first()
        if homebanner:
            homebanner.title = title
            homebanner.description = description
            homebanner.title2 = title2
            homebanner.description2 = description2
            homebanner.title3 = title3
            homebanner.title4 = title4
        else:
            homebanner = Banner(slug=slug, title=title, description=description, title2=title2, description2=description2, title3=title3, title4=title4)
            db.session.add(homebanner)
    elif slug == 'aboutus':
        aboutus = Banner.query.filter_by(slug=slug).first()
        if aboutus:
            aboutus.title = title
            aboutus.description = description
            aboutus.title2 = title2
            aboutus.description2 = description2
            aboutus.title3 = title3
            aboutus.title4 = title4
        else:
            aboutus = Banner(slug=slug, title=title, description=description, title2=title2, description2=description2, title3=title3, title4=title4)
            db.session.add(aboutus)

    db.session.commit()
    return redirect(url_for('banners'))

@app.route('/drop-alembic-version-table')
def drop_alembic_version_table():
    db.session.execute(text('DROP TABLE IF EXISTS alembic_version'))
    db.session.commit()
    return "Alembic version table dropped"

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
    return render_template("admin/login.html")

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route("/post-create", methods=["GET", "POST"])
def create_post():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        new_post = Post(title=title, description=description)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('posts'))
    return render_template("admin/post/create.html")

@app.route("/post/edit/<int:id>", methods=["GET", "POST"])
def edit_post(id):
    if 'username' not in session:
        return redirect(url_for('login'))
    post = Post.query.get_or_404(id)
    if request.method == "POST":
        post.title = request.form["title"]
        post.description = request.form["description"]
        db.session.commit()
        return redirect(url_for('posts'))
    return render_template("admin/post/edit.html", post=post)

@app.route("/admin/post-delete/<int:id>")
def delete_post(id):
    if 'username' not in session:
        return redirect(url_for('login'))
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('posts'))

def create_user(username, password):
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(debug=True)


  
=======
    app.run(debug=True)
>>>>>>> c8c9431c96745e8c2d705ebc8424594d02b59141
