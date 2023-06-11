DROP TABLE IF EXISTS users_old;
CREATE TABLE users_old (
	id INT PRIMARY KEY auto_increment, 
    firstname varchar(50), 
    lastname varchar(50), 
    email varchar(120)
);

DROP PROCEDURE IF EXISTS move_users;
DELIMITER //
CREATE PROCEDURE move_users (IN num INT)
BEGIN
INSERT INTO users_old (firstname, lastname, email)
SELECT firstname, lastname, email
FROM users
WHERE users.id = num;
DELETE FROM users
WHERE id = num;
COMMIT;
END //
DELIMITER ;

CALL move_users(1);

DELIMITER //
CREATE FUNCTION hello()
RETURNS VARCHAR(25)
DETERMINISTIC
BEGIN
DECLARE wellcome_text VARCHAR(25);
SELECT CASE
WHEN CURRENT_TIME BETWEEN '06:00:00' AND '11:59:59' THEN 'Бодрое утро!'
WHEN CURRENT_TIME BETWEEN '12:00:00' AND '17:59:59' THEN 'Бодрый день!'
WHEN CURRENT_TIME BETWEEN '18:00:00' AND '23:59:59' THEN 'Бодрый вечер!'
ELSE 'Бодрой ночи!'
END INTO wellcome_text;
RETURN wellcome_text;

END//
DELIMITER ;

SELECT hello()

DROP TABLE IF EXISTS logs;
CREATE TABLE logs (
add_time DATETIME DEFAULT now(),
table_name VARCHAR(25),
user_id INT NOT NULL)
ENGINE = ARCHIVE;

DROP TRIGGER IF EXISTS users_trigger;
DROP TRIGGER IF EXISTS communities_trigger;
DROP TRIGGER IF EXISTS messages_trigger;

CREATE 
TRIGGER users_trigger
AFTER INSERT ON users FOR EACH ROW
INSERT INTO logs SET table_name = 'users', user_id = (SELECT LAST_INSERT_ID());
 
CREATE 
TRIGGER communities_trigger
AFTER INSERT ON communities FOR EACH ROW
INSERT INTO logs SET table_name = 'communities', user_id = (SELECT LAST_INSERT_ID());

CREATE 
TRIGGER messages_trigger
AFTER INSERT ON messages FOR EACH ROW
INSERT INTO logs SET table_name = 'messages', user_id = (SELECT LAST_INSERT_ID());

INSERT INTO users (id, firstname, lastname, email) VALUES 
(11, 'Василий', 'Пупкин', 'pupkin_vasya666@humans.org');

SELECT * FROM logs;




