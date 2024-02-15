-- list_cities_california.sql

SELECT cities.id, cities.name
FROM cities
WHERE state.id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY cities.id ASC;
