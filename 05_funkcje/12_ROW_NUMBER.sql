-- Etap9. Odcinek: Funkcja ROW_NUMBER()

-- Funkcja ROW_NUMBER()
SELECT *, ROW_NUMBER() OVER (ORDER BY total_bill) AS row_num FROM functions.tips;

SELECT *, ROW_NUMBER() OVER (PARTITION BY day ORDER BY total_bill DESC) AS row_num FROM functions.tips;
SELECT *, ROW_NUMBER() OVER (PARTITION BY day, time ORDER BY total_bill DESC) AS row_num FROM functions.tips;
SELECT *, ROW_NUMBER() OVER (PARTITION BY day, time, sex ORDER BY total_bill DESC) AS row_num FROM functions.tips;

-- 3 najwieksze rachynki dla kazdego dnia
SELECT
  *
FROM
  (SELECT *, ROW_NUMBER() OVER (PARTITION BY day ORDER BY total_bill DESC) AS row_num FROM functions.tips)
WHERE
  row_num IN (1, 2, 3);

-- nie bedzie wyswietlac ostatniej kolumny
SELECT
  * EXCEPT(row_num)
FROM
  (SELECT *, ROW_NUMBER() OVER (PARTITION BY day ORDER BY total_bill DESC) AS row_num FROM functions.tips)
WHERE
  row_num IN (1, 2, 3);