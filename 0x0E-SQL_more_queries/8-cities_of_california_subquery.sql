-- list_cities_california.sql

USE hbtn_0d_usa;

SELECT *
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY cities.id ASC;