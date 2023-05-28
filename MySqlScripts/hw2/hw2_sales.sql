CREATE TABLE sales
(
ID SERIAL PRIMARY KEY,
order_date date,
count_product INT
);

INSERT INTO sales (order_date, count_product)
VALUES ("2022-01-01", 156), 
("2022-01-02", 180), ("2022-01-03", 21), 
("2022-01-04", 124), ("2022-01-05", 341);

SELECT ID AS "id заказа",
CASE
WHEN count_product < 100
THEN "Маленький заказ"
WHEN count_product BETWEEN 100 AND 300
THEN "Средний заказ"
WHEN count_product > 300
THEN "Большой заказ"
END AS "Тип заказа"
FROM sales; 

ALTER TABLE sales
ADD COLUMN order_type VARCHAR(50);

SET SQL_SAFE_UPDATES = 0;
UPDATE sales
SET order_type = 'Маленький заказ' 
WHERE count_product < 100;
UPDATE sales
SET order_type = 'Средний заказ' 
WHERE count_product BETWEEN 100 AND 300;
UPDATE sales
SET order_type = 'Большой заказ' 
WHERE count_product > 300;

SELECT id AS 'id заказа', order_type AS 'Тип заказа'
FROM sales;

