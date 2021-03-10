-- Etap9. Odcinek: Tworzenie wlasnych funkcji

-- jedna zmienna (u niego functions to nazwa bazy danych)
-- Przyjmowanym parametrem jest x a typem paramertu INT64
CREATE FUNCTION functions.multiply_by_5(x INT64) AS (x * 5);

SELECT functions.multiply_by_5(10) AS result;

-- wielu zmiennych
CREATE FUNCTION functions.calculate_area(x FLOAT64, y FLOAT64) AS ( x * y);

SELECT functions.calculate_area(3.5, 4.2) AS result;