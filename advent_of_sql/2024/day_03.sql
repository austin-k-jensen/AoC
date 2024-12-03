with base_cte as(
  select 
  	id, 
  	coalesce(
      (xpath('//total_count/text()', menu_data::xml))[1],
      (xpath('//total_guests/text()', menu_data::xml))[1],
      (xpath('//total_present/text()', menu_data::xml))[1]
 	)::text::int AS guests,
    unnest(xpath('//food_item_id/text()', menu_data::xml))::text as food_item_id
  from christmas_menus
)
select 
  food_item_id,
  count(*) as cnt 
from base_cte
where guests > 78
group by food_item_id
order by cnt desc