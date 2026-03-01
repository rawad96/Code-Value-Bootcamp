-- query 1
SELECT r.* FROM restaurants r
ORDER BY r.name ASC

-- query 2
SELECT i.* FROM items i
WHERE i.price > 40
ORDER BY i.name DESC

-- query 3
SELECT r.* FROM restaurants r
WHERE r.name  LIKE '%burger%'

-- query 4
SELECT o.* FROM orders o
WHERE o.status = 'delivered' OR o.status = 'cancelled'

-- query 5
SELECT i.* FROM items i
WHERE i.category = 'dessert'
ORDER BY i.price ASC

-- query 6
SELECT c.* FROM customers c
WHERE c.registration_date  LIKE '%2024%'

-- query 7
SELECT restu.*, rating.* FROM rating
JOIN restaurants restu ON restu.id = rating.restaurant_id
WHERE rating.rating_number > 3.9 AND restu.is_active = 1

-- query 8
SELECT r.name, c.name, o.* FROM orders o
JOIN restaurants r ON r.id = o.restaurant_id
JOIN customers c ON c.id = o.customer_id

-- query 9
SELECT r.id AS restaurant_id, COUNT(m.item_id) AS number_of_items
FROM restaurants r
JOIN menu m ON r.id = m.restaurant_id
GROUP BY r.id
ORDER BY number_of_items DESC

-- query 10
SELECT rating.*, restu.name AS resuarant_name, c.name AS customer_name FROM rating rating
JOIN restaurants restu ON restu.id = rating.restaurant_id
JOIN customers c ON c.id = rating.customer_id

-- query 11
SELECT o.id AS order_id, c.name AS customer_name, r.name AS restaurant_name, SUM(i.price * oi.quantity) AS total FROM orders o
JOIN customers c ON c.id = o.customer_id
JOIN restaurants r ON r.id = o.restaurant_id
JOIN order_items oi ON oi.order_id = o.id
JOIN items i ON i.id = oi.item_id
GROUP BY o.id, r.name, c.name
ORDER BY o.id;

-- query 12
SELECT r.name AS restaurant_name, i.name AS item_name, i.price
FROM restaurants r
JOIN menu m ON m.restaurant_id = r.id
JOIN items i ON i.id = m.item_id
WHERE i.price = (SELECT MAX(it.price) FROM menu mn
    JOIN items it ON it.id = mn.item_id
    WHERE mn.restaurant_id = r.id)
ORDER BY r.name;

-- query 13
SELECT o.status, COUNT(*) AS total_orders FROM orders o
GROUP BY o.status
ORDER BY total_orders DESC;

-- query 14
SELECT c.* FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
WHERE o.id IS NULL;

-- query 15
SELECT r.name AS restaurant_name, AVG(rating.rating_number) AS average_rating, COUNT(rating.id) AS total_reviews FROM restaurants r
JOIN rating rating ON rating.restaurant_id = r.id
GROUP BY r.id, r.name
HAVING COUNT(rating.id) >= 3
ORDER BY average_rating DESC;

-- query 16
SELECT c.id AS customer_id, c.name AS customer_name, SUM(i.price * oi.quantity) AS total_spent FROM customers c
JOIN orders o ON o.customer_id = c.id
JOIN order_items oi ON oi.order_id = o.id
JOIN items i ON i.id = oi.item_id
GROUP BY c.id, c.name
ORDER BY total_spent DESC
LIMIT 3;

-- query 17
SELECT c.id AS customer_id, c.name AS customer_name, COUNT(DISTINCT o.restaurant_id) AS different_restaurants
FROM customers c
JOIN orders o ON o.customer_id = c.id
GROUP BY c.id, c.name
HAVING COUNT(DISTINCT o.restaurant_id) > 3;

-- query 18
WITH monthly_orders AS (
    SELECT o.id AS order_id,
           o.restaurant_id,
           o.date_time
    FROM orders o
    WHERE o.status = 'delivered'
      AND o.date_time >= DATE_FORMAT(CURDATE(), '%Y-%m-01')
)
, monthly_revenue AS (
    SELECT mo.order_id,
           SUM(i.price * oi.quantity) AS revenue,
           r.cuisine_type
    FROM monthly_orders mo
    JOIN order_items oi ON oi.order_id = mo.order_id
    JOIN items i ON i.id = oi.item_id
    JOIN restaurants r ON r.id = mo.restaurant_id
    GROUP BY mo.order_id, r.cuisine_type
)
, cuisine_revenue AS (
    SELECT cuisine_type,
           SUM(revenue) AS total_revenue
    FROM monthly_revenue
    GROUP BY cuisine_type
    ORDER BY total_revenue DESC
    LIMIT 1
)
SELECT
    (SELECT COUNT(*) FROM restaurants WHERE is_active = 1) AS total_active_restaurants,
    (SELECT COUNT(*) FROM customers) AS total_customers,
    (SELECT COUNT(*) FROM monthly_orders) AS total_delivered_orders,
    (SELECT SUM(revenue) FROM monthly_revenue) AS total_revenue,
    (SELECT AVG(revenue) FROM monthly_revenue) AS average_order_value,
    (SELECT cuisine_type FROM cuisine_revenue) AS top_cuisine_type;


