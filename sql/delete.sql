set sql_safe_updates = 0;
use lesson;
create table weibo_temp select * from weibo;
delete from weibo
where post  in (select  post  from weibo_temp  group  by  post having count(*)>1   )
and rowid not in (select min(rowid) from  weibo_temp  group by post having count(*)>1);
drop table weibo_temp