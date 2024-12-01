with base_cte as(
  select
      ch.name,
      json_value(wl.wishes,'$.first_choice') as primary_wish,
      json_value(wl.wishes,'$.second_choice') as backup_wish,
      json_value(wl.wishes,'$.colors[0]') as favorite_color,
      jsonb_array_length(json_query(wl.wishes,'$.colors')) as color_count,
      case tcp.difficulty_to_make
          when 1 then 'Simple Gift'
          when 2 then 'Moderate Gift'
          else 'Complex Gift'
          end as gift_complexity,
      case tcp.category
          when 'outdoor' then 'Outside Workshop'
          when 'educational' then 'Learning Workshop'
          else 'General Workshop'
          end as workshop_assignment
  from children  ch
  left join wish_lists wl
      on ch.child_id = wl.child_id
  left join toy_catalogue tcp
      on json_value(wl.wishes,'$.first_choice') = tcp.toy_name
  order by 1
  limit 5
)
select concat(name,',',primary_wish,',',backup_wish,',',favorite_color,',',color_count,',',gift_complexity,',',workshop_assignment) from base_cte