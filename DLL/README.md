
# C#語法
*****  
String.Format、HttpClient、await、HttpResponseMessage  
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
+ ### HttpClient  
	提供基底類別，用來傳送 HTTP 要求，以及從 URI 所識別的資源接收 HTTP 回應  
	+ GetAsync(String)  
		以非同步作業的方式，將 GET 要求傳送至指定的 URI。  
	```
	 static async void Main()
	{

	    // Create a New HttpClient object.
	    HttpClient client = new HttpClient();

	    // Call asynchronous network methods in a try/catch block to handle exceptions
	    try	
	    {
	       HttpResponseMessage response = await client.GetAsync("http://www.contoso.com/");
	       response.EnsureSuccessStatusCode();
	       string responseBody = await response.Content.ReadAsStringAsync();
	       // Above three lines can be replaced with new helper method below
	       // string responseBody = await client.GetStringAsync(uri);

	       Console.WriteLine(responseBody);
	    }  
	    catch(HttpRequestException e)
	    {
	       Console.WriteLine("\nException Caught!");	
	       Console.WriteLine("Message :{0} ",e.Message);
	    }

	    // Need to call dispose on the HttpClient object
	    // when done using it, so the app doesn't leak resources
	    client.Dispose(true);
	 }
	```
+ ### await  
	會套用至非同步方法中的工作，以在執行方法中插入暫停點，直到等候的工作完成為止。 工作代表進行中的工作  
+ ### HttpResponseMessage  
	+ EnsureSuccessStatusCode  
		如果HTTP響應的IsSuccessStatusCode屬性為false ，則會引發異常  
	+ Content  
		獲取或設置HTTP響應消息的內容  
+ ### HttpContent  
	+ ReadAsStringAsync  
		以非同步作業方式將 HTTP 內容序列化為字串  
+ ### dynamic  
	dynamic 類型可讓發生它的作業略過編譯時期類型檢查。相反地，這些作業會在執行階段解決。因此，dynamic 類型只存在於編譯時期，而非執行階段  
	
	
	
*****
[String.Format](https://msdn.microsoft.com/zh-tw/library/system.string.format(v=vs.110).aspx)  
[標準數值格式字串](https://docs.microsoft.com/zh-tw/dotnet/standard/base-types/standard-numeric-format-strings)  
[HttpClient 類別](https://msdn.microsoft.com/zh-tw/library/system.net.http.httpclient(v=vs.110).aspx)  
[await](https://docs.microsoft.com/zh-tw/dotnet/csharp/language-reference/keywords/await)  
[HttpResponseMessage 類別](https://msdn.microsoft.com/en-us/library/system.net.http.httpresponsemessage(v=vs.118).aspx)  
[HttpContent 類別](https://msdn.microsoft.com/zh-tw/library/system.net.http.httpcontent(v=vs.118).aspx)  
[dynamic](https://docs.microsoft.com/zh-tw/dotnet/csharp/language-reference/keywords/dynamic)  



