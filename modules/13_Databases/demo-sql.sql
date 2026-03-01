-- INSERT INTO bands (name, genre, country)
-- VALUES ('The Rolling Stones', 'Rock', 'United States')

-- SELECT * FROM bands

-- INSERT INTO musicians (name, birth_year, instrument)
-- VALUES ('Mick Jagger', 1943, 'Vocals')

-- SELECT * FROM musicians

-- ONE BAND --> MANY musicians

-- INSERT INTO musicians (name, birth_year, instrument, band_id)
-- VALUES('Keith Richards', 1943, 'Guitar', 1)

-- UPDATE musicians
-- SET band_id = 1

-- UPDATE albums
-- SET price = 29.99
-- WHERE id = 5

-- SELECT * FROM musicians
-- SELECT id, name FROM musicians

-- SELECT * FROM musicians 
-- WHERE band_id = 1

-- SELECT * FROM musicians 
-- WHERE birth_year > 1940

 -- SELECT * FROM musicians 
 -- WHERE band_id = 1 AND birth_year < 1950
 
-- SELECT * FROM musicians
-- WHERE name = 'Mick Jagger' OR name = 'Keith Richards'

 -- SELECT * FROM musicians
 -- WHERE (name = 'Mick Jagger' OR name = 'Keith Richards') AND birth_year > 1940
 
 -- SELECT * FROM bands
 -- SELECT * FROM albums
 -- SELECT * FROM musicians
 
 -- SELECT * FROM albums 
 -- WHERE band_id IN (1,2,3)
 -- EQUIVALENT TO: WHERE band_id = 2 OR band_id = 1 OR band_id = 3
 
 -- SELECT * FROM albums
 -- WHERE name LIKE '%A%e%'
 
-- SELECT b.name AS 'Band Name', a.name AS 'Album Name'
-- FROM albums a
-- JOIN bands b ON a.band_id = b.id

-- SELECT b.name AS 'Band Name', a.name AS 'Album Name'
-- FROM albums a
-- JOIN bands b ON a.band_id = b.id
-- WHERE a.release_year < 1980 AND b.formed_year > 1960

-- DO NOT DO:
-- SELECT * FROM albums
-- WHERE band_id IN (SELECT id FROM bands WHERE name = 'Pink Floyd')
-- DO:
-- SELECT albums.* FROM albums
-- JOIN bands ON albums.band_id = bands.id
-- WHERE bands.name = 'Pink Floyd'

-- ORDER
-- SELECT * FROM bands
-- WHERE country = 'USA'
-- ORDER BY genre, name ASC

-- Aggregators
-- SELECT COUNT(*), country FROM bands
-- GROUP BY country

-- SELECT SUM(copies_sold), band_id FROM albums
-- GROUP BY band_id
-- ORDER BY SUM(copies_sold)

-- DELETE FROM albums WHERE id = 23
-- SELECT * FROM albums
-- UPDATE albums 
-- SET is_deleted = 1
-- WHERE id = 23

-- SELECT * FROM albums WHERE is_deleted = 0

-- select * from musicians
-- band: 1
-- musician: 1, 2
-- band: 2, musician: 1
-- INSERT INTO bands_to_musicians(band_id, musician_id) VALUES(1, 1);
-- INSERT INTO bands_to_musicians(band_id, musician_id) VALUES(1, 2);
-- INSERT INTO bands_to_musicians(band_id, musician_id) VALUES(2, 1);
/*
SELECT bands.name, bands_to_musicians.from_year, bands_to_musicians.to_year, musicians.* FROM musicians
JOIN bands_to_musicians ON bands_to_musicians.musician_id = musicians.id
JOIN bands ON bands_to_musicians.band_id = bands.id
WHERE band_id = 1
*/
-- UPDATE bands_to_musicians
-- SET 
--   from_year = 1973,
--  to_year = 2010
-- WHERE
--  band_id = 1 AND musician_id = 2

INSERT INTO band_profiles (band_id, bio, url)
VALUES (1, 'Lorem ipsum dolor sit amet','https://therollingstones.com')

SELECT * from bands
JOIN band_profiles on bands.id = band_profiles.band_id
WHERE id = 1











