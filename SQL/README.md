# SQL
*****

+ ### Join

	
+ ### Curral 序列  
	currval取得的是當前會話的序列值，在當前會話中該值不會因為其他會話取了nextval而變化。  
	會變化的是全局的last_value值,並且當前會話中如果沒有讀過nextval值時直接讀currval是會報錯的。   
	```
	select currval('table_id_seq')
	```
*****
[PostgreSQL 序列使用](https://my.oschina.net/Kenyon/blog/60091)  

