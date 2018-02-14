# SQL
*****

+ ### Join
	![](https://az787680.vo.msecnd.net/user/caubekimo/1508/2015813152628267.png)  
	
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
		如果匹對沒有的話，就是顯示 NUL
		+ left outer join  
			以資料表1的資料為主，若資料存在於資料表1，但資料表2沒有對應值時，仍顯示資料表1中的資料。  
		+ right outer join  
			以資料表2的資料為主，若資料存在於資料表2，但資料表1沒有對應值時，仍顯示資料表2中的資料。  
			
		```
		-- 這兩個其實是相同的，left join 就是顯示左邊表格所有資料，right 則是相反
		SELECT a.*, b.* FROM `test1` as a LEFT JOIN `test2` as b on a.id = b.id
		```
		
	+ natural join  
		natural join的作用與inner join一樣，只是只能在兩張table有一樣欄位名稱的狀況下才能使用。
		```
		--NATRAL JOIN
		SELECT keyNo
		FROM A NATURAL JOIN B 
		```

	
+ ### Curral 序列  
	currval取得的是當前會話的序列值，在當前會話中該值不會因為其他會話取了nextval而變化。  
	會變化的是全局的last_value值,並且當前會話中如果沒有讀過nextval值時直接讀currval是會報錯的。   
	```
	select currval('table_id_seq')
	```
*****
[PostgreSQL 序列使用](https://my.oschina.net/Kenyon/blog/60091)  

