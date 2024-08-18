from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa

db = SQLAlchemy()


class Author(db.Model):
    __tablename__ = 'authors'

    author_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    author_name = sa.Column(sa.String)
    birth_date = sa.Column(sa.String)
    date_of_death = sa.Column(sa.String)


class Book(db.Model):
    __tablename__ = 'books'

    book_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    isbn = sa.Column(sa.String)
    title = sa.Column(sa.String)
    publication_year = sa.Column(sa.Integer)
    author_id = sa.Column(sa.Integer, sa.ForeignKey('authors.author_id'))
    book_cover = sa.Column(sa.String)