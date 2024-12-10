with base_cte as (
  select
      date,
      sum(CASE WHEN drink_name = 'Eggnog' THEN quantity ELSE NULL END) AS Eggnog,
      sum(CASE WHEN drink_name = 'Hot Cocoa' THEN quantity ELSE NULL END) AS HotCocoa,
      sum(CASE WHEN drink_name = 'Peppermint Schnapps' THEN quantity ELSE NULL END) AS PeppermintSchnapps
  from drinks
  group by date
)
Select * from base_cte
where Eggnog = 198
and HotCocoa = 38
and PeppermintSchnapps = 298