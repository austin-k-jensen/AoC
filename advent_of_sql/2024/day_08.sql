WITH RECURSIVE base_cte(staff_id,staff_name,level,path) as(
  select 
  	staff_id, staff_name,1 as level, concat(manager_id)
  from staff 
  where staff_id = 1
  
  union all
  
  select 
  	s.staff_id, s.staff_name,level+1, concat(path,s.manager_id)
  from staff s
  inner join base_cte b
  	on b.staff_id = s.manager_id
 )
 select * from base_cte
 order by 3 desc