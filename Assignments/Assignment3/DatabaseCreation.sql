CREATE DATABASE art_gallery;
USE art_gallery;

CREATE TABLE art_works (
	art_id VARCHAR(10),
    title VARCHAR(60) NOT NULL,
    artist VARCHAR(60) NOT NULL,
    CONSTRAINT pk_art_id PRIMARY KEY (art_id)
    );

CREATE TABLE galleries (
	gallery_id VARCHAR(10),
    gallery_name VARCHAR(60),
    address VARCHAR(60),
    country VARCHAR(30),
    CONSTRAINT pk_gallery_id PRIMARY KEY (gallery_id),
    CONSTRAINT unique_gallery_id UNIQUE (gallery_id, gallery_name)
);

CREATE TABLE on_loan (
	loan_id INTEGER,
    art_id VARCHAR(10),
    gallery_id VARCHAR(10),
    send_date DATE, -- Date format is YYYY-MM-DD
    return_by DATE,
    CONSTRAINT pk_loan_id PRIMARY KEY (loan_id),
    FOREIGN KEY (art_id) REFERENCES art_works(art_id),
    FOREIGN KEY (gallery_id) REFERENCES galleries(gallery_id)
);

CREATE TABLE shipping (
	country VARCHAR(30),
    cost INTEGER,
    insurance_cost INTEGER
);
