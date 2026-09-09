# Write your MySQL query statement below
 select e1.name as Employee from employee e join employee e1 on e.id=e1.managerId where e1.salary>e.salary;