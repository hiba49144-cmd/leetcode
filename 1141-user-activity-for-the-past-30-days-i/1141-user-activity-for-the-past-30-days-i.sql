-- Write your PostgreSQL query statement below
select activity_date as day,count(distinct(user_id) )as active_users
from Activity
where activity_date BETWEEN '2019-07-27'::DATE - INTERVAL '29 days' and '2019-07-27'::DATE
group by activity_date;
