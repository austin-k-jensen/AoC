with base_cte as (
  select id, chr(value) as _chr
  from (
    SELECT id, value FROM letters_a
    UNION ALL
    SELECT id, value FROM letters_b
  )
  where (
    value between 65 and 90 
    or value between 97 and 122
    or value in (32,33,34,39,40,41,44,45,46,58,59,63)
  )
  order by id
)
select string_agg(_chr,'') from base_cte;

--Without CTE
select string_agg(chr(value),'')
from (
  SELECT id, value FROM letters_a
  UNION ALL
  SELECT id, value FROM letters_b
  order by id
)
where (
  value between 65 and 90 
  or value between 97 and 122
  or value in (32,33,34,39,40,41,44,45,46,58,59,63)
);