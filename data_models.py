from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa

db = SQLAlchemy()


class Author(db.Model):
    __tablename__ = 'authors'

    # Primary key for the Author table
    author_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)

    # Author's name, birth date, and date of death
    author_name = sa.Column(sa.String)
    birth_date = sa.Column(sa.String)
    date_of_death = sa.Column(sa.String)

    # Establish a one-to-many relationship with the Book model
    books = db.relationship('Book', back_populates='author')


class Book(db.Model):
    __tablename__ = 'books'

    # Primary key for the Book table
    book_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)

    # Book details: ISBN, title, publication year, and book cover URL
    isbn = sa.Column(sa.String)
    title = sa.Column(sa.String)
    publication_year = sa.Column(sa.Integer)

    # Foreign key linking to the Author table
    author_id = sa.Column(sa.Integer, sa.ForeignKey('authors.author_id'))

    # URL of the book cover image
    book_cover = sa.Column(sa.String)

    # Establish the inverse relationship with the Author model
    author = db.relationship('Author', back_populates='books')
