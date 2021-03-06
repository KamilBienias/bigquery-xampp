-- Etap9. Odcinek: Funkcje daty i czasu

-- Funkcje daty i czasu

-- CURRENT_DATETIME([time_zone]) - zwraca datę i czas, domyślnie UTC
SELECT
  CURRENT_DATE('+2:00') as current_date,
  CURRENT_DATETIME('+2:00') as current_datetime;

-- DATETIME(year, month, day, hour, minute, second) - tworzy obiekt DATETIME
SELECT
  DATETIME(2020, 2, 23, 6, 40, 30) as date;

-- DATETIME_ADD(date, INTERVAL INT64 part)
SELECT
  CURRENT_DATETIME('+2:00') AS now,
  DATETIME_ADD(CURRENT_DATETIME('+2:00'), INTERVAL 5 HOUR) AS after_5_hours,
  DATETIME_ADD(CURRENT_DATETIME('+2:00'), INTERVAL 5 MINUTE) AS after_5_minutes,
  DATETIME_ADD(CURRENT_DATETIME('+2:00'), INTERVAL 5 SECOND) AS after_5_seconds;

-- DATETIME_SUB(date, INTERVAL INT64 part)
SELECT
  CURRENT_DATETIME('+2:00') AS now,
  DATETIME_SUB(CURRENT_DATETIME('+2:00'), INTERVAL 5 HOUR) AS five_hours_ago,
  DATETIME_SUB(CURRENT_DATETIME('+2:00'), INTERVAL 5 MINUTE) AS five_minutes_ago,
  DATETIME_SUB(CURRENT_DATETIME('+2:00'), INTERVAL 5 SECOND) AS five_seconds_ago;
-- DATETIME_DIFF(date1, date2, part)
SELECT
  DATETIME_DIFF(DATETIME '2019-10-22T15:00:00.0', DATETIME '2019-10-21T15:00:00.0', HOUR) AS hour_diff,
  DATETIME_DIFF(DATETIME '2019-10-21T15:47:00.0', DATETIME '2019-10-21T15:00:00.0', MINUTE) AS minute_diff;