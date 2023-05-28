CREATE TABLE orders
(id SERIAL PRIMARY KEY,
employee_id VARCHAR(5) NOT NULL,
amount DECIMAL(5,2),
order_status VARCHAR(15)
);

INSERT INTO orders(employee_id, amount, order_status)
VALUES ('e03', 15.00, 'OPEN'), ('e01', 25.50, 'OPEN'),
('e05', 100.70, 'CLOSED'), ('e02', 22.18, 'OPEN'), ('e04', 9.50, 'CANCELLED');

SELECT *,
CASE
WHEN order_status = 'OPEN' OR 'CLOSED' OR 'CANCELLED'
THEN 'Order is open'
WHEN order_status = 'CANCELLED'
THEN 'Order is cancelled'
WHEN order_status = 'CLOSED' 
THEN 'Order is closed'
END AS 'full_order_status'
FROM orders;
