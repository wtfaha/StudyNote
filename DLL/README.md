
# C#語法
*****  
找不到「型別或命名空間名稱」錯誤、Timer 類別  
*****  
+ ### 找不到「型別或命名空間名稱」錯誤  
	今天引用參考時候發生的錯誤，原因竟然就在寫在警告warning訊息中，害我找了好久  
	原來只是版本問題，把.net version改成4.5就可以了XDD
	```
	無法解析主要參考 "Newtonsoft.Json, Version=11.0.0.0, Culture=neutral, PublicKeyToken=30ad4fe6b2a6aeed, processorArchitecture=MSIL"，
	因為它是針對 ".NETFramework,Version=v4.5" Framework 建置的。這個版本高於目前的目標 Framework ".NETFramework,Version=v4.0"。	
	```
  	[怪異的「找不到型別或命名空間名稱」錯誤](https://dotblogs.com.tw/johnny/2015/12/10/type_or_namespace_not_found)  

+ ### Timer 類別  
	+ Timer.Interval屬性  
	取得或設定引發 Elapsed 事件的間隔 (以毫秒為單位)  
	+ Timer.Enabled 屬性  
	取得或設定值，表示 Timer 是否應引發 Elapsed 事件  
	
	+ Timer.Elapsed 事件  
	發生於間隔耗盡時  
	
	+ Timer.Start 方法 ()  
	將 Enabled 設定為 true，開始引發 Elapsed 事件  
	+ Timer.Stop 方法 ()  
	將 Enabled 設定為 false，停止引發 Elapsed 事件  
	
	
	
*****
[怪異的「找不到型別或命名空間名稱」錯誤](https://dotblogs.com.tw/johnny/2015/12/10/type_or_namespace_not_found)  

