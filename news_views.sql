-- Connect to data base

\c news

-- Create view article_view
CREATE VIEW article_view AS SELECT title, author, count(*) AS views From articles, log WHERE log.path
like concat('%', articles.slug) GROUP BY articles.title, articles.author ORDER BY views DESC;

-- Create view error_view
CREATE VIEW error_view AS SELECT DATE(TIME), round(100.0*sum(case log.status WHEN '200 OK' THEN 0 ELSE 1 END)/
count(log.status),2)AS "Percent Error" FROM log GROUP BY DATE (TIME) ORDER BY "Percent Error" DESC;

