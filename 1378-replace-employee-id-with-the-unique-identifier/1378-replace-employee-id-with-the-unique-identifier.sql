# Write your MySQL query statement below
select unique_id, name
from employees
LEFT JOIN employeeUNI
using(id);