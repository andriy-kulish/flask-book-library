from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(32))

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.name


books_authors = Table(
    "books_authors",
    Base.metadata,
    Column("fk_book", Integer, ForeignKey("books.id")),
    Column("fk_author", Integer, ForeignKey("authors.id")),
)


class Book(Base):
    __tablename__ = "books"
    __searchable__ = ['title']

    id = Column("id", Integer, primary_key=True)
    title = Column("title", String(50), nullable=False)

    authors = relationship(
        "Author",
        backref="books",
        secondary=books_authors
    )

    def __init__(self, title=None):
        self.title = title

    def __repr__(self):
        return '<Book %r>' % self.title


class Author(Base):
    __tablename__ = "authors"
    __searchable__ = ['name']

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(50), nullable=False)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Author %r>' % self.name
