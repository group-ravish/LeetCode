# Write your MySQL query statement below
select user_id, count(DISTINCT follower_id) as followers_count
from Followers
group by user_id;