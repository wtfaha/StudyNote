# Postman
******
嘛，網路上很多介紹，在這邊我就不贅述它的功能了  
我簡單講一下我花了比較多時間才解決的問題   

+ ### form-data 轉換成 raw
	+ ### form-data
		header : 基本上不用打Content-type也可以  
		(我用application/x-www-form-urlencoded或applicaion/json或multipart/form-data也都可以)  
		body :  name: 10  id : 123456  
	+ ### 轉換成raw  
		header : application/x-www-form-urlencoded  
		body : name=10&&id=123456  
