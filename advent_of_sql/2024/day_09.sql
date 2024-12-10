with base_cte as (
  select 
      r.reindeer_name, t.exercise_name, avg(t.speed_record) as avg_speed
  from Reindeers r
  inner join Training_Sessions t
  on r.reindeer_id = t.reindeer_id
  group by 1,2
),
rank_cte as (
  select 
      reindeer_name,
      avg_speed,
      RANK() over (PARTITION BY reindeer_name ORDER BY avg_speed desc) as max_speed
  from base_cte
)
select reindeer_name, round(avg_speed,2) from rank_cte where max_speed = 1
order by 2 desc