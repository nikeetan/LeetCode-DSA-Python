# Write your MySQL query statement below
select E.name,b.bonus from Employee E
left join  Bonus b on E.empId = b.empId where b.bonus is null or b.bonus<1000