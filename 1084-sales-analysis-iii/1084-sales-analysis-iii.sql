-- Write your PostgreSQL query statement below
SELECT product_id, product_name
FROM (
    SELECT p.product_id, p.product_name, s.sale_date  
    FROM Product p LEFT JOIN Sales s ON p.product_id = s.product_id
)
GROUP BY product_id, product_name
HAVING MIN(sale_date) >= '2019-01-01' AND MAX(sale_date) <= '2019-03-31'