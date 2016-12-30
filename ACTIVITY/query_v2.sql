drop table if exists activity1;
create temporary table activity1
as
select
Desti_Input,
Desti_TA_Activity,
Desti_TA_ActivityCount1,
@curRank := @curRank + 1 AS rank1
from
(
	SELECT distinct   
	Desti_Input,
	Desti_TA_Activity,
	sum(Desti_TA_ActivityCount) Desti_TA_ActivityCount1
	FROM destination_recommender.TripAdvisorDestinationActivities 
	where Desti_TA_Activity like '%bars%' and Desti_TA_ActivityCount>1
    group by Desti_Input
) a
, (SELECT @curRank := 0) r
ORDER BY  Desti_TA_ActivityCount1 desc;

drop table if exists activity2;
create temporary table activity2
as
select
Desti_Input,
Desti_TA_Activity,
Desti_TA_ActivityCount2,
@curRank := @curRank + 1 AS rank2
from
(
	SELECT distinct   
	Desti_Input,
	Desti_TA_Activity,
	sum(Desti_TA_ActivityCount) Desti_TA_ActivityCount2
	FROM destination_recommender.TripAdvisorDestinationActivities 
	where Desti_TA_Activity like '%beach%' and Desti_TA_ActivityCount>1
    group by Desti_Input
) a
, (SELECT @curRank := 0) r
ORDER BY  Desti_TA_ActivityCount2 desc;

drop table if exists activity3;
create temporary table activity3
as
select
Desti_Input,
Desti_TA_Activity,
Desti_TA_ActivityCount3,
@curRank := @curRank + 1 AS rank3
from
(
	SELECT distinct   
	Desti_Input,
	Desti_TA_Activity,
	sum(Desti_TA_ActivityCount) Desti_TA_ActivityCount3
	FROM destination_recommender.TripAdvisorDestinationActivities 
	where Desti_TA_Activity like '%hiking%' and Desti_TA_ActivityCount>1
    group by Desti_Input
) a
, (SELECT @curRank := 0) r
ORDER BY  Desti_TA_ActivityCount3 desc;

select * from activity1 a1 join activity2 a2 on a2.Desti_Input=a1.Desti_Input join activity3 a3 on a3.Desti_Input=a1.Desti_Input
order by rank1+rank2+rank3 asc