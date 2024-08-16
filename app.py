from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from data_models import db, Author, Book
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.sqlite'
db.init_app(app)


@app.route('/')
def home():
    return 'Welcome to the library'


@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    if request.method == 'GET':
        return render_template('add_author.html')

    if request.method == 'POST':
        birth_date = datetime.datetime.strptime(request.form['birth_date'], '%Y-%m-%d').date()
        date_of_death = datetime.datetime.strptime(request.form['date_of_death'], '%Y-%m-%d').date()
        author = Author(
            author_name=request.form['author_name'],
            birth_date=birth_date,
            date_of_death=date_of_death)
        db.session.add(author)
        db.session.commit()
        return f'author created'


if __name__ == '__main__':
    app.run(debug=True)


# with app.app_context():
#     db.create_all()
