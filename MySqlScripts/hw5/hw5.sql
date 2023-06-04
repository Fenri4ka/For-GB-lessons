CREATE OR REPLACE VIEW view_users_20 AS 
SELECT CONCAT(firstname, ' ', lastname) AS 'Младше 20 лет', 
CASE(gender)
WHEN 'm' THEN 'Мужской'
WHEN 'f' THEN 'Женский'
END AS 'Пол', hometown AS 'Город'
FROM users
JOIN profiles ON users.id = profiles.user_id
WHERE ABS(YEAR(birthday) - 2023) < 20
GROUP BY user_id;

SELECT DENSE_RANK() OVER (ORDER BY COUNT(from_user_id) DESC) AS 'Рейтинг',
CONCAT(firstname, ' ', lastname) AS 'Пользователь',
COUNT(from_user_id) AS 'Сообщений'
FROM users
JOIN messages ON users.id = messages.from_user_id
GROUP BY users.id;

SELECT *,
TIMEDIFF(created_at, LAG(created_at) OVER w) AS 'Разница дат'
FROM messages
WINDOW w AS(ORDER BY created_at);