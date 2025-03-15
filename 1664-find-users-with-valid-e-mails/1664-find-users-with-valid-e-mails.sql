# Write your MySQL query statement below
select * from users where mail regexp '^[a-zA-Z]+[A-Za-z0-9_\.\-]*@leetcode\\.com$'