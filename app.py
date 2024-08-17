from crypt import methods

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from data_models import db, Author, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../data2/library.sqlite'
db.init_app(app)


@app.route('/')
def home():
    books = Book.query.all()
    return render_template('index.html', books=books)


@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    if request.method == 'GET':
        return render_template('add_author.html')

    if request.method == 'POST':
        birth_date = request.form['birth_date']
        date_of_death = request.form['date_of_death']
        author_name = request.form['author_name']
        author = Author(

            author_name=author_name,
            birth_date=birth_date,
            date_of_death=date_of_death
        )
        db.session.add(author)
        db.session.commit()
        return f'author created'


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'GET':
        authors = Author.query.all()
        return render_template('add_book.html', authors=authors)

    if request.method == 'POST':
        isbn = request.form['isbn']
        title = request.form['title']
        publication_year = request.form['publication_year']
        author_id = request.form['author']

        book = Book(
            title=title,
            isbn=isbn,
            publication_year=publication_year,
            author_id=author_id
        )
        db.session.add(book)
        db.session.commit()
        return 'Book added'


if __name__ == '__main__':
    app.run(debug=True)
#
#
# with app.app_context():
#     db.create_all()
