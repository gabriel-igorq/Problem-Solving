-- Query all columns for all American cities in the CITY table with populations larger than 100000. 
-- The CountryCode for America is USA.
SELECT * 
FROM city
WHERE population > 100000 AND countrycode = 'USA'

-- Query the NAME field for all American cities in the CITY table with populations larger than 120000. 
-- The CountryCode for America is USA.
SELECT name
FROM city
WHERE population > 120000 and countrycode = 'USA'

-- Query all columns (attributes) for every row in the CITY table.
SELECT *
FROM city

-- Query all columns for a city in CITY with the ID 1661.
SELECT *
FROM city
WHERE id = 1661

-- Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.
SELECT *
FROM city
WHERE countrycode = 'JPN'

-- Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.
SELECT name
FROM city
WHERE countrycode = 'JPN'

-- Query a list of CITY and STATE from the STATION table.
SELECT city, state
FROM station

-- Query a list of CITY names from STATION for cities that have an even ID number. 
-- Print the results in any order, but exclude duplicates from the answer.
SELECT DISTINCT city
FROM station
WHERE id%2 = 0

-- Find the difference between the total number of CITY entries in the table and the number 
-- of distinct CITY entries in the table. For example, if there are three records in the table 
-- with CITY values 'New York', 'New York', 'Bengalaru', there are 2 different city names: 
-- 'New York' and 'Bengalaru'. The query returns 1
SELECT COUNT(city) - COUNT(DISTINCT city)
FROM station

-- Query the two cities in STATION with the shortest and longest CITY names, 
-- as well as their respective lengths (i.e.: number of characters in the name). 
-- If there is more than one smallest or largest city, choose the one that comes first 
-- when ordered alphabetically.
SELECT city, LENGTH(city)
FROM station
ORDER BY LENGTH(city), city LIMIT 1;

SELECT city, LENGTH(city)
FROM station
ORDER BY LENGTH(city) DESC, city LIMIT 1;