1. SELECT * FROM park WHERE park_visitors < 1000000
2. SELECT COUNT(DISTINCT city) FROM park
3. SELECT SUM(park_visitors) FROM park WHERE city = 'San Francisco'
4. SELECT name, park_visitors FROM park ORDER BY park_visitors DESC LIMIT 5