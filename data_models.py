from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa

db = SQLAlchemy()


class Author(db.Model):
    __tablename__ = 'authors'

    author_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    author_name = sa.Column(sa.String)
    birth_date = sa.Column(sa.Date)
    date_of_death = sa.Column(sa.Date)


class Book(db.Model):
    __tablename__ = 'books'

    book_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    isbn = sa.Column(sa.Integer)
    title = sa.Column(sa.String)
    publication_year = sa.Column(sa.Integer)
    author_id = sa.Column(sa.Integer, sa.ForeignKey('authors.author_id'))