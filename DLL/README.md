# C#語法
*****
String.Trim()、#region、NetworkInterface、Path、Directory 
*****
+ ### String.Trim()  
    傳回新的 String，等於從開頭和結尾移除泛空白字元後的這個執行個體  
  
+ ### #region  
    指定在使用 Visual Studio 程式碼編輯器的大綱功能時，可以展開或摺疊的程式碼區塊  
    簡單的說，就是可以把許多的程式碼區塊 (放在同一個區域(region)內)，讓程式更好理解及管理  
    
+ ### NetworkInterface  
	+ GetAllNetworkInterfaces  
    		Returns objects that describe the network interfaces on the local computer.

+ ### Path  
	+ GetDirectoryName  
    		返回指定路径字符串的目录信息  
		```
		string filePath = @"C:\MyDir\MySubDir\myfile.ext";
		string directoryName;

   		directoryName = Path.GetDirectoryName(filePath);
    		Console.WriteLine("GetDirectoryName('{0}') returns '{1}'",filePath, directoryName);
		
		/*
		GetDirectoryName('C:\MyDir\MySubDir\myfile.ext') returns 'C:\MyDir\MySubDir'
		*/
		```
+ ### Directory  
	+ CreateDirectory(String)  
		在指定的路徑建立所有目錄和子目錄 (如果這些目錄尚不存在)  
	+ Exists(String)  
		判斷指定路徑是否參考磁碟上的現有目錄  


*****
[String.Trim 方法 ()](https://msdn.microsoft.com/zh-tw/library/t97s7bs3(v=vs.80).aspx)  
[C# 裡面的 #region 用法](http://goodlucky.pixnet.net/blog/post/30349716-c%23-%E8%A3%A1%E9%9D%A2%E7%9A%84-%23region-%E7%94%A8%E6%B3%95)  
[NetworkInterface](https://msdn.microsoft.com/en-us/library/system.net.networkinformation.networkinterface(v=vs.110).aspx)  
[Path.GetDirectoryName](https://msdn.microsoft.com/zh-cn/library/system.io.path.getdirectoryname(v=vs.110).aspx)  
[Directory ](https://msdn.microsoft.com/zh-tw/library/system.io.directory(v=vs.110).aspx)  
