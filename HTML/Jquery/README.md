# Jquery
*****
hide、selector、字串
*****

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
+ ### selector
	
	+ :eq() : 第幾個  
		ex : id為name底下的第二個li  
		```
		$("#name li:eq(0)")
		```
+ ### 字串  
	```   
	'<td width="25%%">
		<p class="title2"><a href="#" onclick="doEdit(\\\''+response[i].bmac+'\\\')">'+response[i].bmac+'</a></p>
	</td>'                        
	```
	\\\'	\\\'  	參數為字串  
	'+	+'	取得參數  
	合併的例子如下 :  
	```   
	onclick="doEdit(\\\''+response[i].bmac+'\\\')"                       
	```
+ ### array操作
	+ includes()  
		會判斷陣列是否包含特定的元素，並以此來回傳 true 或 false
		```
		成功oao
		```
	+ in operator  
		如果指定的屬性位於指定對像或其原型鏈中，則該in運算符返回true
		```
		// 不知道為什麼有點問題，他只有辦法判斷id_List長度的值(len = 6)
		// 也就是只有1跟5會alert，其他都不會，不知道為什麼，所以先使用上一個方法
		id_List = 1,33,25,5,10,18;
		response.length = 20;
		for(var i = 0; i < response.length; i++){
		    if(id in id_List){
		    	alert("in");
		    }
		}
		```
	+ indexOf()  
		回傳給定元素於陣列中第一個被找到之索引，若不存在於陣列中則回傳-1  
	
	
*****
[Array.prototype.includes()](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Global_Objects/Array/includes)  
[Array.prototype.indexOf()](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf)  
[in operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/in)  
