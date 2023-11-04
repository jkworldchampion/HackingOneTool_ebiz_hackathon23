SELECT c.first_name, c.country, s.status
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN Shippings s ON o.customer_id = s.customer
WHERE o.item = 'Keyboard';