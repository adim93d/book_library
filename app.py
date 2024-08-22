
from flask import Flask, render_template, request, redirect, url_for
from data_models import db, Author, Book
from sqlalchemy import asc, desc, or_


COVER_URL = 'https://covers.openlibrary.org/b/isbn/'
COVER_URL_EXTENSION = '-S.jpg'


def cover_search(isbn):
    # isbn_search = input('Enter ISBN:')
    cover_photo = COVER_URL + isbn + COVER_URL_EXTENSION
    return cover_photo


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../data2/library2.sqlite'
db.init_app(app)

@app.route('/')
def home():
    # Retrieve search query and sorting preference from the request arguments
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

    # Apply sorting to the filtered query based on user selection
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

    # Execute the query and fetch all matching books
    books = query.all()

    return render_template('index.html', books=books)


@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    if request.method == 'GET':
        # Render the form to add a new author
        return render_template('add_author.html')

    if request.method == 'POST':
        # Extract form data for the new author
        birth_date = request.form['birth_date']
        date_of_death = request.form['date_of_death']
        author_name = request.form['author_name']
        author = Author(
            author_name=author_name,
            birth_date=birth_date,
            date_of_death=date_of_death
        )
        # Add the new author to the database
        db.session.add(author)
        db.session.commit()
        return 'Author created'


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'GET':
        # Fetch all authors to display in the dropdown list for book assignment
        authors = Author.query.all()
        return render_template('add_book.html', authors=authors)

    if request.method == 'POST':
        # Extract form data for the new book
        isbn = request.form['isbn']
        title = request.form['title']
        publication_year = request.form['publication_year']
        author_id = request.form['author']

        # Create a new book record and add it to the database
        book = Book(
            title=title,
            isbn=isbn,
            publication_year=publication_year,
            author_id=author_id,
            book_cover=cover_search(isbn)
        )
        db.session.add(book)
        db.session.commit()
        return 'Book added'

@app.route('/book/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    # Fetch the book to be deleted
    book = Book.query.get_or_404(book_id)
    author_id = book.author_id

    # Delete the book
    db.session.delete(book)
    db.session.commit()

    # Check if the author has any other books, if not, delete the author
    remaining_books = Book.query.filter_by(author_id=author_id).count()
    if remaining_books == 0:
        author = Author.query.get(author_id)
        db.session.delete(author)
        db.session.commit()

    # Flash a success message and redirect to the homepage
    return redirect(url_for('home'))


if __name__ == '__main__':
    # Run the Flask application on localhost port 5002 with debug mode enabled
    app.run(debug=True, port=5002)

# Uncomment the lines below to create the database tables if they don't exist
# with app.app_context():
#     db.create_all()
