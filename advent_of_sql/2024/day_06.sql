select c.name,g.name,g.price
from children c
inner join gifts g
	on c.child_id = g.child_id
where g.price > (select avg(price) from gifts)
order by 3