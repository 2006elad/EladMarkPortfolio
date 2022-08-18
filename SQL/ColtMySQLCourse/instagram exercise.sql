-- 1
SELECT *
FROM USERS
ORDER BY created_at
LIMIT 5;

-- 2
SELECT dayname(created_at) as "day name", COUNT(*) as "count"
FROM users
GROUP BY dayofweek(created_at)
ORDER BY count DESC;

-- 3
SELECT username
FROM users LEFT JOIN photos ON users.id = photos.user_id
WHERE photos.user_id IS NULL;

-- 4
SELECT username, users.id as "id of creator", photos.id as "photo id", COUNT(*) as likes
FROM (users JOIN photos ON users.id = photos.user_id) JOIN likes ON likes.photo_id = photos.id
GROUP BY users.id, photos.id
ORDER BY likes DESC
LIMIT 1;

-- 5
SELECT 
    ROUND((SELECT 
                    COUNT(*)
                FROM
                    PHOTOS) / (SELECT 
                    COUNT(*)
                FROM
                    USERS),
            2) AS 'avg user';
            
-- 6
SELECT tags.id, tag_name, COUNT(*) as total
FROM tags JOIN photo_tags ON tags.id = photo_tags.tag_id
GROUP BY tags.id
ORDER BY total DESC
LIMIT 5;

-- 7
WITH table1(username, total) AS
(
	SELECT username, COUNT(*)
	FROM (users JOIN photos ON users.id = photos.user_id) JOIN likes ON likes.photo_id = photos.id
	GROUP BY users.id
)
SELECT username
FROM table1
WHERE total = (SELECT COUNT(*) FROM photos)
