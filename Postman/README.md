# Postman
******
嘛，網路上很多介紹，在這邊我就不贅述它的功能了  
我簡單講一下我花了比較多時間才解決的問題   

+ ### (基本) form-data 轉換成 raw  
	[參考連結_用postman但收不到值解決之方法](http://lifunny.me/2017/11/01/java-%E9%97%9C%E6%96%BCspringmvc%E7%94%A8postman%E4%BD%86%E6%94%B6%E4%B8%8D%E5%88%B0%E5%80%BC%E8%A7%A3%E6%B1%BA%E4%B9%8B%E6%96%B9%E6%B3%95/)
	+ ### form-data
		header : 基本上不用打Content-type也可以  
		(我用application/x-www-form-urlencoded或applicaion/json或multipart/form-data也都可以)  
		body :  name: 10  id : 123456  
	+ ### 轉換成raw  
		header : application/x-www-form-urlencoded  
		body : name=10&&id=123456  
+ ### (List) form-data 轉換成 raw  
	[參考連結_Postman输入List参数](http://blog.csdn.net/qq125537082/article/details/52298518)
	+ ### form-data
		body :  name[]: 10 name[]: 11 id : 123456  
	+ ### 轉換成raw  
		body : name[]=10&&name[]=11&&id=123456
