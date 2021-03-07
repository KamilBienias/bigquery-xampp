-- Etap8. Odcinki: Grupowanie i Sortowanie: GROUP BY oraz ORDER BY
-- oraz HAVING

-- SELECT ... FROM ... WHERE ... GROUP BY ...
SELECT
  end_station_id,
  count(*) as count_station
FROM
  DQL.bike
GROUP BY
  end_station_id;

-- SELECT ... FROM ... WHERE ... GROUP BY ... ORDER BY ...
SELECT
  end_station_id,
  count(*) as count_station
FROM
  DQL.bike
GROUP BY
  end_station_id
ORDER BY
  count_station;

-- SELECT ... FROM ... WHERE ... GROUP BY ... ORDER BY ... LIMIT ...
SELECT
  end_station_id,
  count(*) as count_station
FROM
  DQL.bike
GROUP BY
  end_station_id
ORDER BY
  count_station DESC
LIMIT 20;

-- Cz.2
-- SELECT ... FROM ... WHERE ... GROUP BY ... ORDER BY ... LIMIT ...
SELECT -- kolumny uzyte w SELECT musza sie znalezc w GROUP BY
  end_station_id,
  end_station_name,
  count(*) as count_station
FROM
  DQL.bike
GROUP BY -- kolumny uzyte w SELECT musza sie znalezc w GROUP BY
  end_station_id,
  end_station_name
ORDER BY
  count_station DESC
LIMIT 20;

-- SELECT ... FROM ... WHERE ... GROUP BY ... ORDER BY ... LIMIT ...
SELECT
  end_station_id,
  end_station_name,
  count(*) as count_station
FROM
  DQL.bike
WHERE
  duration > 50
GROUP BY
  end_station_id,
  end_station_name
ORDER BY
  count_station DESC
LIMIT 20;

-- Odcinek: HAVING
-- SELECT ... FROM ... WHERE ... GROUP BY ... HAVING ... ORDER BY ... LIMIT ...
SELECT
  end_station_id,
  end_station_name,
  count(*) as count_station
FROM
  DQL.bike
WHERE
  duration > 50
GROUP BY
  end_station_id,
  end_station_name
HAVING  -- HAVING musi zawierac warunek z funkcja agregujaca
  count_station >= 7  -- bierze stacje ktore pojawily sie minimum 7 razy
ORDER BY
  count_station DESC;

-- SELECT ... FROM ... WHERE ... GROUP BY ... HAVING ... ORDER BY ... LIMIT ... OFFSET ...
SELECT
  end_station_id,
  end_station_name,
  count(*) as count_station
FROM
  DQL.bike
WHERE
  duration > 50
GROUP BY
  end_station_id,
  end_station_name
HAVING
  count_station >= 5
ORDER BY
  count_station DESC
LIMIT
  10
OFFSET -- pomija 3 pierwsze wiersze, czyli wyswietla stacje od 4 miejsca
  3;