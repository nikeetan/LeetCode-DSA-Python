# Write your MySQL query statement below

select viewer_id as id from views where author_id=viewer_id group by viewer_id having count(viewer_id)>=1 order by viewer_id asc