USE art_gallery;

-- USING JOINS AND ADDING ANOTHER CONSTRAINT

-- Using a left join to match our galleries with shipping and insurance cost
-- For each gallery in each country, we can see the shipping cost and insurance cost for artwork
SELECT galleries.gallery_name, galleries.country, shipping.cost, shipping.insurance_cost
FROM galleries
LEFT JOIN shipping
ON galleries.country = shipping.country;

-- Using multiple joins to match artworks with the galleries they're at, and when they were sent there
SELECT art_works.title, art_works.artist, on_loan.send_date, galleries.gallery_name
FROM on_loan
JOIN art_works ON art_works.art_id = on_loan.art_id
JOIN galleries ON galleries.gallery_id = on_loan.gallery_id;

-- I want to add a new constraint to my artworks table, so that all art_id's have to be unique
-- This is to avoid accidental duplication for my art_id PK when I enter new artworks to my table
ALTER TABLE art_works
ADD CONSTRAINT unique_art_id
UNIQUE (art_id);

-- I want to add a new art_work to mt art_works table
INSERT INTO art_works
(art_id, title, artist)
VALUES
('A11', 'Les Demoiselles dAvignon', 'Pablo Picasso');

-- USING FUNCTIONS

-- I want to see what countries the galleries are in, in alphabetical order
SELECT
g.gallery_name, g.country
FROM galleries g
ORDER BY g.gallery_name;

-- I want to see what transport costs are over 10,000 in increasing order
SELECT
s.country, s.cost
FROM shipping s
WHERE s.cost > 10000
ORDER BY s.cost;

-- I want to see what Picasso artworks I have in my collection
SELECT
a.title, a.artist
FROM art_works a
WHERE a.artist = 'Pablo Picasso';

-- I want to know the average shipping cost for my artworks
SELECT AVG(s.cost) AS average_cost
FROM shipping s;

-- The minimum shipping cost per country
SELECT s.country, MIN(s.cost) AS minimum_cost
FROM shipping s
GROUP BY s.country;

-- I want to know the number of distinct artists I have in my collection
SELECT
COUNT(DISTINCT a.artist)
FROM art_works a;

-- I want to see the year that my artworks will be returned to me
-- But art_id is FK on my on_loan table, so I will use a join to retrieve the art title and artist from my art_works table
SELECT
l.art_id, a.title, a.artist, YEAR(l.return_by) AS return_year
FROM on_loan l
JOIN art_works a ON l.art_id = a.art_id;

-- Using LIKE get the titles of pieces where the artists name begins with 'P'
SELECT a.title, a.artist
FROM art_works a
WHERE a.artist
LIKE 'P%';

-- I want to see how long my artworks are on loan for in years, from lowest to highest
SELECT
	l.art_id,
    l.send_date,
    l.return_by,
	TIMESTAMPDIFF(YEAR, l.send_date, l.return_by) AS loan_length_years
FROM on_loan l
ORDER BY loan_length_years;

-- Adding another gallery
INSERT INTO galleries
(gallery_id, gallery_name, address, country)
VALUES
('GAL07', 'Tate Britain', 'Millbank, London SW1P 4RG', 'United Kingdom');

-- Deciding that I actually don't want to send art to Tate Britain
-- Not for any particular reason, I do really like Tate Britain but tbh I prefer Tate Modern I think the vibes are better there
-- Because I'm in safe mode, I will need to use the key column gallery_id
DELETE FROM galleries
WHERE gallery_ID = 'GAL07';

-- WRITING A STORED FUNCTION

DELIMITER //
CREATE FUNCTION total_cost(cost INT, insurance INT)
RETURNS INT -- From what I understand, decimals are better for calculations, but all my numbers in my table are int
-- If I was to use real data, I would have stored the data as DECIMAL(10,2) and then returned a decimal (but not a float bc the accuracy isn't great)
DETERMINISTIC -- SQL gave me an error bc I didn't include this
-- I looked it up and it is so SQL knows that it should always return the same output given the same inputs, given I am in safe mode
BEGIN
	DECLARE total INT;
    SET total = cost + insurance;
    RETURN total;
END //
DELIMITER ;

-- Retruns the total cost of shipping and insurance of artwork by country in order of cost lowest -> highest
SELECT s.country, total_cost(s.cost, s.insurance_cost) AS total
FROM shipping s
ORDER BY total;