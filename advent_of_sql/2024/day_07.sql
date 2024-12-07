with base_cte as (
  select
      elf_id,
      primary_skill,
      RANK() over (PARTITION BY primary_skill ORDER BY years_experience desc,elf_id) as max_y,
      RANK() over (PARTITION BY primary_skill ORDER BY years_experience,elf_id) as min_y
  from workshop_elves
)
select 
	mx.elf_id,
    mn.elf_id,
    mx.primary_skill
from (select * from base_cte where max_y = 1) mx
inner join (select * from base_cte where min_y = 1) mn
	on mx.primary_skill = mn.primary_skill
order by 3