USE art_gallery;

INSERT INTO art_works
(art_id, title, artist)
VALUES
('A01', 'Guernica', 'Pablo Picasso'),
('A02', 'Nude Descending a Staircase, No.2', 'Marcel Duchamp'),
('A03', 'The Persistence of Memory', 'Salvador Dali'),
('A04', 'Broadway Boogie Woogie', 'Piet Mondrian'),
('A05', 'Campbells Soup Can', 'Andy Warhol'),
('A06', 'Nighthawks', 'Edward Hopper'),
('A07', 'I and the Village', 'Marc Chagall'),
('A08', 'Christinas World', 'Andrew Wyeth'),
('A09', 'Amercian Gothic', 'Grant wood'),
('A10', 'The Kiss', 'Gustav Klimt');

INSERT INTO galleries
(gallery_id, gallery_name, address, country)
VALUES
('GAL01','Tate Modern', 'Bankside, London SE1 9TG', 'United Kingdom'),
('GAL02', 'Reina Sofia', 'C. de Sta. Isabel, 52, Centro, 28012, Madrid', 'Spain'),
('GAL03', 'Singapore Art Museum', '39 Keppel Rd, Tanjong Pagar Distripark', 'Singapore'),
('GAL04', 'Museum of Contemporary Art', '140 George St, The ROCKS NSW, 2000', 'Australia'),
('GAL05', 'Museum of Modern Art', '11 W 53rd St, New York, NY 10019', 'United Sates'),
('GAL06', 'MAC/CCB Museu de Arte Contemporanea', 'Parca do Imperio, 1449-003, Lisboa', 'Portugal');

INSERT INTO on_loan
(loan_id, art_id, gallery_id, send_date, return_by)
VALUES
(1,'A01','GAL02','2017-05-19','2025-08-19'),
(2,'A04','GAL05','2024-07-30','2027-09-30'),
(3,'A05','GAL01','2012-02-01','2030-12-01'),
(4,'A08','GAL04','2015-06-15','2026-10-15');

INSERT INTO shipping
(country, cost, insurance_cost)
VALUES
('Australia', 75000, 38900),
('Portugal', 7650, 13900),
('Singapore', 87000, 46500),
('Spain', 4500, 12500),
('United Kingdom', 3460, 14500),
('United Sates', 57800, 79800);