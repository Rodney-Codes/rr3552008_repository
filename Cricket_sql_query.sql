with cte as
(
	select td.team_name, pd.player_name, role, sum(runs_scored) as trs, sum(wickets_took) as twt, 
	case
	when role="Batter"
	then row_number() over (partition by td.team_name, role="batter" order by sum(runs_scored) desc)
	else 0
	end as row1,
	case 
	when role="Pitcher"
	then row_number() over (partition by td.team_name, role="Pitcher" order by sum(wickets_took) desc) 
	else 0
	end as row2
	from player_details as pd
	join match_details as md on pd.player_id=md.player_id and md.team_id=pd.team_id
	join team_details as td on pd.team_id=td.team_id
	group by td.team_name, pd.player_name, role
)
select c1.team_name, c1.player_name, c1.trs, c2.player_name, c2.twt
from cte as c1
join cte as c2 on c1.team_name=c2.team_name
where c1.row1=1 and c2.row2=1

/*
with cte1 as 
(
	select team_name, player_name, trs
	from
	(
		select td.team_name, pd.player_name, sum(runs_scored) as trs
		from player_details as pd
		join match_details as md on pd.player_id=md.player_id and md.team_id=pd.team_id
		join team_details as td on pd.team_id=td.team_id
		where role="Batter" and td.team_name="Australia"
		group by td.team_name, pd.player_name
		order by trs desc limit 1
	) t1
	union
	select team_name, player_name, trs
	from
	(
		select td.team_name, pd.player_name, sum(runs_scored) as trs
		from player_details as pd
		join match_details as md on pd.player_id=md.player_id and md.team_id=pd.team_id
		join team_details as td on pd.team_id=td.team_id
		where role="Batter" and td.team_name="England"
		group by td.team_name, pd.player_name
		order by trs desc limit 1
	) t2
),
cte2 as
(
	select team_name, player_name, twt
	from
	(
		select td.team_name, pd.player_name, sum(wickets_took) as twt
		from player_details as pd
		join match_details as md on pd.player_id=md.player_id and md.team_id=pd.team_id
		join team_details as td on pd.team_id=td.team_id
		where role="Pitcher" and td.team_name="Australia"
		group by td.team_name, pd.player_name
		order by twt desc limit 1
	) t3
	union
	select team_name, player_name, twt
	from
	(
		select td.team_name, pd.player_name, sum(wickets_took) as twt
		from player_details as pd
		join match_details as md on pd.player_id=md.player_id and md.team_id=pd.team_id
		join team_details as td on pd.team_id=td.team_id
		where role="Pitcher" and td.team_name="England"
		group by td.team_name, pd.player_name
		order by twt desc limit 1
	) t4
)

select cte1.team_name, cte1.player_name, cte1.trs, cte2.player_name, cte2.twt
from cte1
join cte2 on cte1.team_name=cte2.team_name
*/