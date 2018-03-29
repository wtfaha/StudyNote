
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
	+ D : 完整日期模式  
		D2代表兩位數的小數  
	+ N、n : number  
*****
[String.Format](https://msdn.microsoft.com/zh-tw/library/system.string.format(v=vs.110).aspx)  
[標準數值格式字串](https://docs.microsoft.com/zh-tw/dotnet/standard/base-types/standard-numeric-format-strings)

