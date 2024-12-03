with base_cte as(
  select 
  	id, 
  	coalesce(
      (xpath('//total_count/text()', menu_data::xml))[1],
      (xpath('//total_guests/text()', menu_data::xml))[1],
      (xpath('//total_present/text()', menu_data::xml))[1]
 	)::text::int AS guests,
    unnest(xpath('//food_item_id/text()', menu_data::xml))
  from christmas_menus
)
select * from base_cte
where guests > 78