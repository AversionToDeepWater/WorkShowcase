CREATE DATABASE kdrama;
USE kdrama;

-- list of Kdrama
CREATE TABLE kdrama_list (
kdrama_id INT NOT NULL AUTO_INCREMENT,
title VARCHAR(50) NOT NULL,
main_male_lead VARCHAR(50) NOT NULL,
main_female_lead VARCHAR(50) NOT NULL,
watched ENUM('Y','N'),
rating_ten INT DEFAULT NULL,
PRIMARY KEY(kdrama_id)
);

-- list of Kdrama ratings but I do not think this table is necessary
-- CREATE TABLE ratings (
-- kdrama_id INT,
-- year_released YEAR,
-- watched ENUM('Y','N'),
-- rating_ten INT DEFAULT NULL,
-- FOREIGN KEY (kdrama_id) REFERENCES kdrama_list(kdrama_id)
-- );

-- Data to kdrama list
INSERT INTO kdrama_list(kdrama_id, title, main_male_lead, main_female_lead, watched, rating_ten)
VALUES
(1, 'Crash Landing on You', 'Hyun Bin', 'Son Ye-Jin', 'Y', 7),
(2, 'Its Okay not to Be Okay', 'Kim Soo-hyun', 'Seo Yae-Ji', 'Y', 9),
(3, 'Mr. Queen', 'Kim Jung-hyun', 'Shin Hye-sun', 'N', null),
(4, 'Healer', 'Ji Chang-wook', 'Park Min-young', 'N', null),
(5, 'Weightlifting Fairy Kim Bok-joo', 'Nam Joo-hyuk', 'Lee Sung-kyung', 'Y', 8);

-- Data to ratings no longer relevant as I put it all in one table 
-- INSERT INTO ratings (kdrama_id, year_released, watched, rating_ten)
-- VALUES 
-- (1, 2019, 'Y', 7),
-- (2, 2020, 'Y', 9),
-- (3, 2020, 'N', null),
-- (4, 2014, 'N', null),
-- (5, 2016, 'Y', 8);


-- Checking tables look correct on sql
--  SELECT title, main_male_lead, main_female_lead FROM kdrama_list;
-- SELECT * FROM kdrama_list;













