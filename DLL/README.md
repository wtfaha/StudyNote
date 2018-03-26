
# C#語法
*****  
WndProc、InitializeComponent、StreamReader  
*****  
+ ### WndProc  
  用來接收Windows Message  
	```
	protected override void WndProc(ref Message m)
        {
            base.WndProc(ref m);
        }
	```
+ ### InitializeComponent  
	載入元件的已編譯網頁  
+ ### StreamReader  
	+ ReadLine()  
		自目前資料流讀取一行字元，並將資料以字串傳回  
		輸入資料流的下一行，或為 null (如果已到達輸入資料流末端)  
+ ### String.StartsWith()  
	判斷這個字串執行個體的開頭是否符合指定的字串  
+ ### Controll  
	定義控制項的基底類別，它們屬於具視覺表示的元件  
	+ Find()  : 控制項查找  
		+ 參數key  
			Type: System.String  
			要在 Control.ControlCollection 中尋找的索引鍵  
		+ 參數searchAllChildren  
			Type: System.Boolean  
			true 若要搜尋所有子控制項，否則， false  
		```
		public Control[] Find(
			string key,
			bool searchAllChildren
		)
		((TextBox) this.Controls.Find("textBox"+i.ToString(), true)[0]).Text = "1234";
		```
		
	+ 判斷型態的方法判斷控制項種類  
		```
		int i = 0;
		//方法一 用 GetType() ，不建議...太麻煩
		if (i.GetType() == typeof(int))
		{
			Console.WriteLine("i.GetType() == typeof(int)");
		}
		```

*****
[[C#.NET][WinForm] Windows 視窗訊息接收 - WndProc](https://dotblogs.com.tw/yc421206/2011/01/23/20971)  
[InitializeComponent](https://msdn.microsoft.com/zh-tw/library/system.windows.markup.icomponentconnector.initializecomponent(v=vs.110).aspx)  
[StreamReader.ReadLine()](https://msdn.microsoft.com/zh-tw/library/system.io.streamreader.readline(v=vs.110).aspx)  
[Controll](https://msdn.microsoft.com/zh-tw/library/system.windows.forms.control(v=vs.110).aspx)  
[C#尋找控制項篇](https://dotblogs.com.tw/markit/2014/06/25/145697)  

