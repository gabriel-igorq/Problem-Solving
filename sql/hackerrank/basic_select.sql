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

-- Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. 
-- Your result cannot contain duplicates.
SELECT DISTINCT city
FROM station
WHERE city REGEXP '^[aeiou]'

-- Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. 
-- Your result cannot contain duplicates
SELECT DISTINCT city
FROM station
WHERE city REGEXP '[aeiou]$'

-- Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) 
-- as both their first and last characters. Your result cannot contain duplicates.
SELECT DISTINCT city
FROM station
WHERE city REGEXP '^[aeiou].*[aeiou]$'

-- Query the list of CITY names from STATION that do not start with vowels. 
-- Your result cannot contain duplicates.
SELECT DISTINCT city
FROM station
WHERE city NOT REGEXP '^[aeiou]'

-- Query the list of CITY names from STATION that do not end with vowels. 
-- Your result cannot contain duplicates.
SELECT DISTINCT city
FROM station
WHERE city NOT REGEXP '[aeiou]$'

-- Query the list of CITY names from STATION that either do not start with vowels or do not end with 
-- vowels. Your result cannot contain duplicates.
SELECT DISTINCT city
FROM station
WHERE city NOT REGEXP '^[aeiou].*[aeiou]$'

-- Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. -- Your result cannot contain duplicates
SELECT DISTINCT city
FROM station
WHERE city REGEXP '^[^aeiou].*[^aeiou]$'

-- Query the Name of any student in STUDENTS who scored higher than 75 Marks. Order your output by the 
-- last three characters of each name. If two or more students both have names ending in the same last 
-- three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.
SELECT name
FROM students
WHERE marks > 75
ORDER BY RIGHT(name, 3), id

-- Write a query that prints a list of employee names (i.e.: the name attribute) from the Employee table in 
-- alphabetical order.
SELECT name
FROM employee
ORDER BY name

-- Write a query that prints a list of employee names (i.e.: the name attribute) for employees in Employee having 
-- a salary greater than $2000 per month who have been employees for less than 10 months. Sort your result by 
-- ascending employee_id.
SELECT name
FROM employee
WHERE salary > 2000 and months < 10
ORDER BY employee_id

-- Write a query identifying the type of each record in the TRIANGLES table using its three side lengths.
SELECT
IF (a+b > c and b+c > a and c+a > b, IF(a=b and b=c, 'Equilateral', IF(a=b or b=c or a=c, 'Isosceles', 'Scalene')), 'Not A Triangle')
FROM triangles