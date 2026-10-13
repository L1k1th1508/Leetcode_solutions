# Write your MySQL query statement below
SELECT id 
FROM (
    SELECT 
        id,
        recordDate,
        temperature,
        LAG(temperature) OVER (ORDER BY recordDate ASC) AS prev_temp,
        lag(recordDate) over (order by recordDate ASC) as prev_date 
    FROM weather 
) as subquerry where temperature>prev_temp and Datediff(recordDate,prev_date)=1;