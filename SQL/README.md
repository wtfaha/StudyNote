# SQL
*****
正規化
*****
+ ### 正規化  
	建構「資料模式」所運用的一個技術，其目的是為了  
	1. 降低資料的「重覆性」  
	2. 避免「更新異常」的情況發生  
	
	+ 無損失分解觀念  
	當關聯表R被「分解」成數個關聯表R1, R2, R1, R2,…, Rn 時，則可以再透過「合併」R1 R2 R1 R2… Rn得到相同的資訊R。  

	+ 第一正規化(1NF)  
	定義 : 是指在資料表中的所有記錄之屬性內含值都是基元值(Atomic (Atomic Value)。亦即無重覆項目群  
	
	規則 :  
	1.每一個欄位只能有一個基元值(Atomic) (Atomic)即單一值。  
	2. 沒有任何兩筆以上的資料是完全重覆。  
	3.資料表中有主鍵, 而其他所有的欄位都相依於「主鍵」。  
	
	步驟 :  
	1. 將重複的資料項分別儲存到不同的記錄中, 並加上適當的主鍵。  
	2. 將重複資料項分別儲存到不同的記錄中, 並加上適當的主鍵  
	
	+ 第二正規化(2NF)  
	在完成了第一正規化之後，是否發現在資料表中產生許多重複的資料。如此, 不但浪費儲存的空間, 更容易造成新增、修改及刪除資料時的異常狀況  
	(1) 新增異常檢查(Insert Anomaly) (Insert Anomaly)  
	(2)修改異常檢查(Update Anomaly) (Update Anomaly)  
	(3)刪除異常檢查(Delete Anomaly) (Delete Anomaly)  
	
	綜合上述的三種異常現象，所以 綜合上述的三種異常現象，所以, 我們必須進行「第二階正規化」 行「第二階正規化」, 來消除這些問題。 
	
	規則 :  
	1. 符合1NF  
	2. 每一非鍵屬性(如：姓名、性別…)必須「完全相依」於主鍵(學號)；即不可「部分功能相依」於主鍵。  
	
	步驟 :  
	1. 檢查是否存在「部分功能相依」  
	2. 將「部分功能相依」的欄位分割出去，再另外組成新的資料表  
	
	+ 第三正規化(3NF)  
	規則 :  
	1. 符合2NF  
	2. 各欄位與「主鍵」之間沒有「遞移相依」的關係  
	
	【如何找遞移相依呢？】  
	若要找出資料表中各欄位與「主鍵」之間的遞移相依性, 最簡單的方法就是從左到右掃瞄資料表中各欄位有沒有『與主鍵無關的相依性』存在。  
	可能的情況如下：  
	1.如果有存在時，則代表有「遞移相依」的關係  
	2. 如果有不存在時，則代表沒有「遞移相依」的關係  
	
	分割資料表；亦即將「遞移相依」或「間接相依」的欄位「分割」出去，再另外組成「新的資料表」。  
	步驟 :  
	1. 檢查是否存在「遞移相依」  
	2. 將「遞移相依」的欄位「分割」出去，再另外組成「新的資料表」  
	
	
*****
[正規化](http://cc.cust.edu.tw/~ccchen/doc/db_04.pdf)  

[T-SQL 中的 JOIN 語法解析 (for SQL Server)](https://dotblogs.com.tw/caubekimo/2010/07/28/16874)  

[SQL裡頭的各種JOIN(NATURAL JOIN、OUTER JOIN、INNER JOIN)](http://ponshanecode.blogspot.tw/2014/08/sqljoinnatural-joinouter-joininner-join.html)  

