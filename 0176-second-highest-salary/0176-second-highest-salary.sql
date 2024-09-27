# Write your MySQL query statement below
-- 

select max(salary) as secondHighestSalary from employee e where e.salary <>(select max(salary) from employee);



