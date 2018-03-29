
# C#語法
*****  
WndProc、InitializeComponent、StreamReader、String.StartsWith()、Controll  
*****  
+ ### WndProc  
  用來接收Windows Message  
	```
	protected override void WndProc(ref Message m)
        {
            base.WndProc(ref m);
        }
	```
+ ### StreamReader  
	+ ReadLine()  
		自目前資料流讀取一行字元，並將資料以字串傳回  
		輸入資料流的下一行，或為 null (如果已到達輸入資料流末端)  
*****
[[C#.NET][WinForm] Windows 視窗訊息接收 - WndProc](https://dotblogs.com.tw/yc421206/2011/01/23/20971)  

