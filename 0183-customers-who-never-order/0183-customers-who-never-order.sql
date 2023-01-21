# Write your MySQL query statement below
select c.name as 'Customers'
from Customers c
where c.id not in (select o.customerId
                  from Orders o);