CREATE DATABASE shirts_db;
USE shirts_db;
CREATE TABLE shirts
(
	shirt_id int AUTO_INCREMENT NOT NULL PRIMARY KEY,
    article VARCHAR(100),
    color VARCHAR(100),
    shirt_size VARCHAR(100),
	last_worn int
);

INSERT INTO shirts(article, color, shirt_size, last_worn) VALUES
('t-shirt', 'white', 'S', 10),
('t-shirt', 'green', 'S', 200),
('polo shirt', 'black', 'M', 10),
('tank top', 'blue', 'S', 50),
('t-shirt', 'pink', 'S', 0),
('polo shirt', 'red', 'M', 5),
('tank top', 'white', 'S', 200),
('tank top', 'blue', 'M', 15);
 
INSERT INTO shirts(article, color, shirt_size, last_worn) values ('polo shirt', 'purple', 'M', 50);

select article, color
from shirts;

select article, color, shirt_size, last_worn
from shirts
where shirt_size = 'm';

update shirts set shirt_size ='XS', 
color = 'off white'
where color = 'white';

delete from shirts
where last_worn >= 200;

delete from shirts
where article = "tank top";

delete from shirts;

drop table shirts;