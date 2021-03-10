-- Etap9. Odcinek: Funkcje: RANK, DENSE_RANK, PERCENT_RANK

-- null jest na poczatku w rankingu. Jesli dwa wiersze maja taka
-- sama wartosc to maja takie same miejsce w rankingu
SELECT
  *,
  RANK() OVER (ORDER BY rating) AS ranking
FROM
  `bigquery-course-257019.functions.movies`;

-- od najw wartosci do najmniejszej czyli im wiekszy rating
-- tym wyzej jest w rankingu
SELECT
  *,
  RANK() OVER (ORDER BY rating DESC) AS ranking
FROM
  `bigquery-course-257019.functions.movies`;

--  DENSE_RANK() zwraca szereg zwarty czyli nie ma luk w rankingu
SELECT
  *,
  RANK() OVER (ORDER BY rating DESC) AS ranking,
  DENSE_RANK() OVER (ORDER BY rating DESC) AS dense_ranking
FROM
  `bigquery-course-257019.functions.movies`;

--  zachowane jest sortowanie w ostatniej kolumnie ktora zostala podana
SELECT
  *,
  RANK() OVER (ORDER BY rating DESC) AS ranking,
  DENSE_RANK() OVER (ORDER BY rating DESC) AS dense_ranking,
  PERCENT_RANK() OVER (ORDER BY rating DESC) AS percent_ranking,
  RANK() OVER (ORDER BY movie_name) AS movie_name_ranking
FROM
  `bigquery-course-257019.functions.movies`;