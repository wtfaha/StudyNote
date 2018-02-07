# Cherrypy 安裝
******
有鑑於教學好少，只能看著官方文件學習，因此我要來記錄看著官方學習的艱辛之路XDD  
+ ### 安裝
	1.可以透過普通的Python軟件包(如setuptools或pip)安裝
```
$ easy_install cherrypy
```
```
$ pip install cherrypy
```
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
	瀏覽器指向http://127.0.0.1:8080  
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
