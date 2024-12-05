select
	production_date,
    toys_produced,
    LAG(toys_produced,1) over (ORDER BY production_date) as previous_day_production,
    toys_produced - (LAG(toys_produced,1) over (ORDER BY production_date)) as production_change,
    (toys_produced - (LAG(toys_produced,1) over (ORDER BY production_date)))*100.00 / 
    	((LAG(toys_produced,1) over (ORDER BY production_date))) as production_change_percentage 
from toy_production
order by 5 desc