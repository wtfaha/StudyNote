# Cherrypy 安裝
******
有鑑於教學好少，只能看著官方文件學習，因此我要來記錄看著官方學習的艱辛之路XDD  
+ ### (List) form-data 轉換成 raw  
	[參考連結_Postman输入List参数](http://blog.csdn.net/qq125537082/article/details/52298518)
	+ ### form-data
		body :  name[]: 10 name[]: 11 id : 123456  
	+ ### 轉換成raw  
		body : name[]=10&&name[]=11&&id=123456
