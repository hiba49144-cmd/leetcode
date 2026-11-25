SELECT
    machine_id,
    ROUND(
        AVG(timestamp::NUMERIC) FILTER (WHERE activity_type = 'end') - 
        AVG(timestamp::NUMERIC) FILTER (WHERE activity_type = 'start'),
    3) AS processing_time
FROM activity
GROUP BY machine_id