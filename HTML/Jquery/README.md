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
		同時天殺的，前面兩個方式他媽的我怎麼嘗試都無法使用，所以只好使用傳統的判斷了  
	```
	$(selector).css("display") != "none"
	```

