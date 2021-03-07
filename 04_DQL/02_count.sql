-- Etap8. Odcinek: Funkcja COUNT()

-- gdyby jakis wiersz mial wszystkie kolumny null
-- to by go nie policzylo.
-- Wystarczy ze ma jedna kolumne niepusta to bedzie policzony.
SELECT
  COUNT(*) AS count_row
FROM
  DQL.bike;

--liczy wszystkie wiersze (nawet jak cale sa nullami)
SELECT
  COUNT(1) AS count_row
FROM
  DQL.bike;

--  wyswietli 992 wiersze bo 8 jest null w kolumnie end_station_id
SELECT
  COUNT(end_station_id) AS count_row
FROM
  DQL.bike;