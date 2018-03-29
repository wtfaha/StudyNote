
# C#語法
*****  
String.Format  
*****  
+ ### String.Format  
  根據指定的格式將物件的值轉換為字串，並將它們插入到另一個字串  
	```
	Decimal pricePerOunce = 17.36m;
	String s = String.Format("The current price is {0} per ounce.",
				 pricePerOunce);
	```
+ ### StreamReader  
	+ ReadLine()  
		自目前資料流讀取一行字元，並將資料以字串傳回  
		輸入資料流的下一行，或為 null (如果已到達輸入資料流末端)  
*****
[String.Format](https://msdn.microsoft.com/zh-tw/library/system.string.format(v=vs.110).aspx)  
[標準數值格式字串](https://docs.microsoft.com/zh-tw/dotnet/standard/base-types/standard-numeric-format-strings)

