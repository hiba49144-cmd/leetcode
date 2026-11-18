-- Write your PostgreSQL query statement below
select p.product_name, sum(o.unit) as unit
from Products p JOIN Orders o
ON p.product_id = o.product_id
WHERE o.order_date >= '2020-02-01' AND o.order_date < '2020-03-01'
group by p.product_name
HAVING SUM(o.unit) >= 100;