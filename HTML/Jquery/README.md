# Jquery

+ ### hide()
	基本語法 :   
	
	+ 把元素變可見或隱藏是:
	```
	$(selector).show()  
	$(selector).hide()
	```
	
	+ 判別元素是否為可見或隱藏是:
	```
	$(selector).is(':visible')
	$(selector).is(':hidden')
	```
	
	+ 有時會透豆, 只好使用傳統的判斷:  
		進去網頁的css裡面看，發現我$(selector).hide()後，style變成display:none  
		同時天殺的，前面兩個判別是否隱藏或可見方式他媽的我怎麼嘗試都無法使用，所以只好使用傳統的判斷了  
		  
		過了一周後再寫，莫名前面兩個判別是否隱藏或可見方式突然可以用了= =?  
		以防出了問題，我還是用傳統的方式判斷  
		
	```
	$(selector).css("display") != "none"
	```
		

