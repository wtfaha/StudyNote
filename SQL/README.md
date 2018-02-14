# SQL
*****

+ ### Join
	+ inner join  
		join跟inner join是ㄧ樣，只是inner join表達更加完整  
		```
		--INNER JOIN
		SELECT keyNo
		FROM A INNER JOIN B ON A.keyNo = B.keyNo

		--JOIN
		SELECT keyNo
		FROM A JOIN B ON A.keyNo = B.keyNo
		```
		
	+ outer join  
	
	+ left join  
		以資料表1的資料為主，若資料存在於資料表1，但資料表2沒有對應值時，仍顯示資料表1中的資料。  
	+ right join  
		以資料表2的資料為主，若資料存在於資料表2，但資料表1沒有對應值時，仍顯示資料表2中的資料。  
	+ natural join  
	
+ ### Curral 序列  
	currval取得的是當前會話的序列值，在當前會話中該值不會因為其他會話取了nextval而變化。  
	會變化的是全局的last_value值,並且當前會話中如果沒有讀過nextval值時直接讀currval是會報錯的。   
	```
	select currval('table_id_seq')
	```
*****
[PostgreSQL 序列使用](https://my.oschina.net/Kenyon/blog/60091)  

