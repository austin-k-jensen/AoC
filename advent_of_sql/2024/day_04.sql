select
	toy_id,
	cardinality(array(select unnest(new_tags) except select unnest(previous_tags))) as added_tags,
    cardinality(array(select unnest(new_tags) intersect select unnest(previous_tags))) as unchanged_tags,
	cardinality(array(select unnest(previous_tags) except select unnest(new_tags))) as removed_tags
from toy_production
order by 2 desc