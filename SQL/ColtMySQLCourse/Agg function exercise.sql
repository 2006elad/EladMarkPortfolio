SELECT count(*) AS "number of books in db"
FROM books;

SELECT released_year, COUNT(*)
FROM books
GROUP BY released_year
ORDER BY released_year DESC;

SELECT SUM(stock_quantity) as "TOTAL QUANTITY"
FROM books;

SELECT author_fname, author_lname, AVG(released_year)
FROM books
GROUP BY author_fname, author_lname;

SELECT CONCAT(author_fname," ", author_lname) as "full name", pages
FROM books
ORDER BY pages DESC
LIMIT 1;

SELECT released_year, COUNT(*) AS "# books", AVG(pages) as "avg pages"
FROM books
GROUP BY released_year
ORDER BY released_year;
