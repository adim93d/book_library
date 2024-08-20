from crypt import methods

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from data_models import db, Author, Book
import book_information
from sqlalchemy import asc, desc, or_

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../data2/library2.sqlite'
db.init_app(app)

@app.route('/')
def home():
    search_query = request.args.get('search_query', '')
    sort_by = request.args.get('sort_by', 'book_id')

    # Base query with a join to include author information
    query = Book.query.join(Author)

    # Filter by search query (partial search with ilike)
    if search_query:
        query = query.filter(or_(
            Book.title.ilike(f'%{search_query}%'),
            Author.author_name.ilike(f'%{search_query}%')
        ))

    # Apply sorting to the filtered query
    if sort_by == 'book_id':
        query = query.order_by(asc(Book.book_id))
    elif sort_by == 'title_asc':
        query = query.order_by(asc(Book.title))
    elif sort_by == 'title_desc':
        query = query.order_by(desc(Book.title))
    elif sort_by == 'year_asc':
        query = query.order_by(asc(Book.publication_year))
    elif sort_by == 'year_desc':
        query = query.order_by(desc(Book.publication_year))

    books = query.all()

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
            author_id=author_id,
            book_cover=book_information.cover_search(isbn)
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
