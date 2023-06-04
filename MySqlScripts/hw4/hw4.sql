SELECT COUNT(*) AS 'Лайки' FROM likes 
WHERE user_id IN (
SELECT user_id FROM profiles WHERE ABS(YEAR(birthday) - 2023) <= 12);

SELECT gender AS 'Пол', COUNT(*) AS 'Лайки' FROM profiles
JOIN likes ON likes.user_id = profiles.user_id
GROUP BY gender;
-- женщины ставят больше лайков

SELECT DISTINCT CONCAT(firstname, ' ', lastname) AS 'Не отправляли сообщений' FROM users
WHERE NOT EXISTS (
SELECT from_user_id FROM messages
WHERE messages.from_user_id = users.id);

SELECT from_user_id AS 'id', (
SELECT concat(firstname, ' ', lastname) 
FROM users
WHERE id = messages.from_user_id) AS 'Друг',
COUNT(*) AS 'Сообщений'
FROM messages
WHERE to_user_id = 1 AND from_user_id IN (
SELECT initiator_user_id 
FROM friend_requests 
WHERE (target_user_id = 1) AND status ='approved'
UNION
SELECT target_user_id 
FROM friend_requests 
WHERE (initiator_user_id = 1) AND status ='approved' 
)
GROUP BY from_user_id
ORDER BY Сообщений DESC
LIMIT 1;