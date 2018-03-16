# Python
*****
檔案  
*****
+ ### 建檔  
+ ### 開檔  
  ```
  f = open('檔案', '模式')
  ```
  r - 讀取(檔案需存在)  
  w - 新建檔案寫入(檔案可不存在，若存在則清空)  
  a - 資料附加到舊檔案後面(游標指在EOF)  
  r+ - 讀取舊資料並寫入(檔案需存在且游標指在開頭)  
  w+ - 清空檔案內容，新寫入的東西可在讀出(檔案可不存在，會自行新增)  
  a+ - 資料附加到舊檔案後面(游標指在EOF)，可讀取資料  
  b - 二進位模式  
  
+ ### 讀檔  
  ```
  f.read(size) - 回傳檔案內容
  ```
  size為要讀取進來的字串長度，若不填則讀取整份文件  
  
  f.readline() - 讀取一行,最後面會加上一個 \n  
  f.readlines() - 傳回一list ，每一行文字最後面會加上一個 \n 為一個list的資料項  
  
  + while  
    ```
    ## Open file
    fp = open('filename.txt', "r")
    line = fp.readline()

    ## 用 while 逐行讀取檔案內容，直至檔案結尾
    while line:
        print line
        line = fp.readline()

    fp.close()
    ```
  + with  
    ```
    with open(filename.txt,'r') as fp:
     all_lines = fp.readlines()
    ```
  + readlines  
    ```
    ## Open file
    fp = open('filename.txt', "r")

    # 變數 lines 會儲存 filename.txt 的內容
    lines = fp.readlines()

    # close file
    fp.close()

    # print content
    for i in range(len(lines)):
            print lines[i]
    ```
  + iter  
    ```
    fp = open('filename.txt', "r")
    for line in iter(fp):
        print line
    fp.close()
    ```
  
+ ### 寫檔  
  ```
  f.write(string) - 寫入檔案，並回傳寫入的string長度
  ```

+ ### 關檔  
  ```
  f.close();
  ```
  
  
  
*****
[Python初學起步走-Day29] - 檔案讀寫](https://ithelp.ithome.com.tw/articles/10161708)  

[Python 逐行讀取檔案內容的 4 個方法] - 檔案讀寫](https://www.phpini.com/perl/4-ways-write-file-line-by-line-in-python)  
