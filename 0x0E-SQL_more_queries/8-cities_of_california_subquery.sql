-- lists all citites of California
SELECT cities.id, cities.name
FROM states, cities
WHERE cities.state_id = states.id AND states.name="California"
ORDER BY cities.id ASC;
