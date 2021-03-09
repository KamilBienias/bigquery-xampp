-- Etap8. Odcinek: Sortowanie: Instrukcja ORDER BY

SELECT * FROM `bigquery-course-257019.DQL.bike`;
SELECT * FROM `bigquery-course-257019.DQL.bike` ORDER BY bike_id;
SELECT * FROM `bigquery-course-257019.DQL.bike` ORDER BY bike_id ASC;
SELECT * FROM `bigquery-course-257019.DQL.bike` ORDER BY bike_id DESC;
SELECT * FROM `bigquery-course-257019.DQL.bike` ORDER BY duration DESC LIMIT 3;
-- 3 wiersze po trzech pierwszych
SELECT * FROM `bigquery-course-257019.DQL.bike` ORDER BY duration DESC LIMIT 3 OFFSET 3;

SELECT * FROM `bigquery-course-257019.DQL.bike` ORDER BY end_station_id, duration;
SELECT * FROM `bigquery-course-257019.DQL.bike` ORDER BY end_station_id DESC, duration DESC;
-- zamiast nazwy kolumny moge jej numer od lewej
SELECT * FROM `bigquery-course-257019.DQL.bike` ORDER BY 5 DESC, 2 DESC;
-- tutaj sa trzy kolumny wiec numeracja wzgledem nich
SELECT rental_id, end_station_id, duration FROM `bigquery-course-257019.DQL.bike` ORDER BY 2 DESC, 3 DESC;