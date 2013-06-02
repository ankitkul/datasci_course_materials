CREATE TABLE D AS
select term,row_num,rowid-1 as col_num,count from X
union
select Y.term as term,Y.row_num as row_num, X1.col_num as col_num,Y.count as count
from Y JOIN 
(select term,row_num,rowid-1 as col_num,count from X) AS X1
 ON Y.term = X1.term
 order by row_num;

select Y.term as term,Y.row_num as row_num, X1.col_num as col_num,Y.count as count
from Y JOIN 
(select term,row_num,rowid-1 as col_num,count from X) AS X1
 ON Y.term = X1.term

CREATE TABLE Dt AS
select term, col_num as row_num, row_num as col_num, count
from D;

--D*Dt = Singular matrix
select D.row_num,Dt.col_num,sum(D.count*Dt.count) 
from D, Dt where D.col_num = Dt.row_num
group by D.row_num, Dt.col_num;

-- normal sum
select sum(Y.count * X1.count)
from Y JOIN 
(select term,row_num,rowid-1 as col_num,count from X) AS X1
 ON Y.term = X1.term 

 --------------------------------------
 i)

CREATE TABLE Q As
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count

-- Get the documents where query words appear most
select docid,count(term) 
from frequency 
where term in (select term from Q) 
group by docid 
having count(term)=3;

--
select f.docid, sum(f.count)
from frequency as f JOIN Q
ON f.term = Q.term
JOIN 
(select docid,count(term) 
from frequency 
where term in (select term from Q) 
group by docid 
having count(term)>=1) T
ON f.docid = T.docid
group by f.docid
order by sum(f.count)


