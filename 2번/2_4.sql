SELECT
  country AS 나라,
  COUNT(*) AS 고객수,
  AVG(age) AS 평균나이
FROM Customers
GROUP BY country
ORDER BY AVG(age) DESC;
