CREATE TABLE authors (
	id INTEGER NOT NULL,
	name VARCHAR(50) NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE users (
	id INTEGER NOT NULL,
	name VARCHAR(50),
	email VARCHAR(120),
	password VARCHAR(32),
	PRIMARY KEY (id),
	UNIQUE (name),
	UNIQUE (email)
);
CREATE TABLE books (
	id INTEGER NOT NULL,
	title VARCHAR(50) NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE books_authors (
	fk_book INTEGER,
	fk_author INTEGER,
	FOREIGN KEY(fk_book) REFERENCES books (id),
	FOREIGN KEY(fk_author) REFERENCES authors (id)
);
INSERT INTO users (name, email, password) VALUES ('root', 'root@gmail.com', 'pass');
INSERT INTO authors (name) VALUES ('Стругацкий А.');
INSERT INTO authors (name) VALUES ('Стругацкий Б.');
INSERT INTO authors (name) VALUES ('Маркес Г.');
INSERT INTO authors (name) VALUES ('Азимов А.');
INSERT INTO authors (name) VALUES ('Пушкин А.С.');
INSERT INTO authors (name) VALUES ('По Е.');
INSERT INTO books (title) VALUES ('Понедельник начинается в субботу');
INSERT INTO books (title) VALUES ('100 лет одиночества');
INSERT INTO books (title) VALUES ('Я - робот');
INSERT INTO books (title) VALUES ('Евгений Онегин');
INSERT INTO books (title) VALUES ('Золотой жук');
INSERT INTO books_authors (fk_book, fk_author) VALUES (1, 1);
INSERT INTO books_authors (fk_book, fk_author) VALUES (1, 2);
INSERT INTO books_authors (fk_book, fk_author) VALUES (2, 3);
INSERT INTO books_authors (fk_book, fk_author) VALUES (3, 4);
INSERT INTO books_authors (fk_book, fk_author) VALUES (4, 5);
INSERT INTO books_authors (fk_book, fk_author) VALUES (5, 6);
