-- Etap10. Odcinek: Wyrazenie IFNULL oraz NULLIF

-- IFNULL(expr, null_result)
SELECT * FROM functions.movies;

SELECT *, IFNULL(duration, 0) AS duration_not_null FROM functions.movies;

--jak natrafi na 'Killer' to wstawi null
-- NULLIF(expr, expr_to_match)
SELECT *, NULLIF(movie_name, 'Killer') AS killer_flag FROM functions.movies;