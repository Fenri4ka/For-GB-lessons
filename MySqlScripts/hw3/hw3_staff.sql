USE lesson_3;

SELECT *
FROM staff
ORDER BY salary DESC;

SELECT *
FROM staff
ORDER BY salary ASC;

SELECT salary
FROM staff
LIMIT 5;

SELECT post AS 'Специальность', SUM(salary) AS 'Суммарная зарплата'
FROM staff
GROUP BY post;

SELECT post AS 'Специальность', COUNT(*) AS 'Количество сотрудников'
FROM staff
WHERE post = 'Рабочий' AND age BETWEEN 24 AND 49
GROUP BY post;

SELECT COUNT(DISTINCT post) AS 'Количество специальностей'
FROM staff;

SELECT DISTINCT post
FROM staff
GROUP BY post
HAVING AVG(age) < 30;
-- специальности, у которой средний возраст сотрудников меньше 30 лет нет.

SELECT post, AVG(age)
FROM staff
GROUP BY post;