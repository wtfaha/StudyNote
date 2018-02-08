# Cherrypy 安裝
******
有鑑於教學好少，只能看著官方文件學習，因此我要來記錄看著官方學習的艱辛之路XDD  
+ ### 安裝
	1.可以透過普通的Python軟件包(如setuptools或pip)安裝  
	打開普通的cmd後，輸入以下指令即可
	```
	$ easy_install cherrypy
	```
	```
	$ pip install cherrypy
	```
	我一開始用easy_install cherrypy安裝，但嘗試兩次都出現
	```
	SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Building pywin32", pywin32_version)?
	```
	我以為安裝不成功，因此我換pip install cherrypy來安裝，但仍然出現以下訊息
	```
	Exception:
	Traceback (most recent call last):
	  File "C:\Users\user\Anaconda3\lib\site-packages\pip\basecommand.py", line 215, in main
	    status = self.run(options, args)
	  File "C:\Users\user\Anaconda3\lib\site-packages\pip\commands\install.py", line 342, in run
	    prefix=options.prefix_path,
	  File "C:\Users\user\Anaconda3\lib\site-packages\pip\req\req_set.py", line 784, in install
	    **kwargs
	  File "C:\Users\user\Anaconda3\lib\site-packages\pip\req\req_install.py", line 851, in install
	    self.move_wheel_files(self.source_dir, root=root, prefix=prefix)
	  File "C:\Users\user\Anaconda3\lib\site-packages\pip\req\req_install.py", line 1064, in move_wheel_files
	    isolated=self.isolated,
	  File "C:\Users\user\Anaconda3\lib\site-packages\pip\wheel.py", line 345, in move_wheel_files
	    clobber(source, lib_dir, True)
	  File "C:\Users\user\Anaconda3\lib\site-packages\pip\wheel.py", line 323, in clobber
	    shutil.copyfile(srcfile, destfile)
	  File "C:\Users\user\Anaconda3\lib\shutil.py", line 121, in copyfile
	    with open(dst, 'wb') as fdst:
	PermissionError: [Errno 13] Permission denied: 'C:\\Users\\user\\Anaconda3\\Lib\\site-packages\\win32\\win32api.pyd'
	```
	感覺就安裝不成功，但是當我接下來嘗試用easy_install cherrypy或pip install cherrypy再來安裝一次  
	卻說我已成功安裝，我真的有點母煞煞，不太清楚到底怎麼回事，希望之後能正常使用 
	因此我就沒有嘗試透過Github獲取來源代碼來獲得最新的Cherrypy版本的安裝方式
	
	2.可以透過Github獲取來源代碼來獲得最新的Cherrypy版本
	```
	$ git clone https://github.com/cherrypy/cherrypy 
	$ cd cherrypy 
	$ python setup.py install
	```
+ ### 測試安裝
	CherryPy提供了一套簡單的教程，一旦你部署了包，就可以執行。
	```
	$ python -m cherrypy.tutorial.tut01_helloworld
	```
	一旦啟動，上述命令將顯示以下logs  
	```
	[15/Feb/2014:21:51:22] ENGINE Listening for SIGHUP.
	[15/Feb/2014:21:51:22] ENGINE Listening for SIGTERM.
	[15/Feb/2014:21:51:22] ENGINE Listening for SIGUSR1.
	[15/Feb/2014:21:51:22] ENGINE Bus STARTING
	[15/Feb/2014:21:51:22] ENGINE Started monitor thread 'Autoreloader'.
	[15/Feb/2014:21:51:22] ENGINE Serving on http://127.0.0.1:8080
	[15/Feb/2014:21:51:23] ENGINE Bus STARTED
	```
	打開遊覽器 http://127.0.0.1:8080 則會顯示
	```
	Hello World
	```
+ ### 運行
	只要myapp.py定義了一個“__main__”部分，就會運行的很好。
	```
	$ python myapp.py
	```
+ ### cherryd
	運行應用程序的另一種方法是通過與cherrydCherryPy一起安裝的腳本。
	```
	NOTE:
	如果您將應用程序嵌入到另一個框架中，此實用程序命令將不會涉及到您。
	```
+ ### Command
	-c, --config	指定配置文件（s）  
	-d	作為守護程序運行服務器  
	-e, --environment	應用給定的配置環境（默認為None）  
	-f	啟動FastCGI服務器而不是默認的HTTP服務器  
	-s	啟動一個SCGI服務器，而不是默認的HTTP服務器  
	-i, --import	指定要導入的模塊  
	-p, --pidfile	將進程ID存儲在給定的文件中（默認為None）  
	-P, --Path	將給定的路徑添加到sys.path  
	
	
