
# C#語法
*****  
Dictionary  
*****  
+ ### Dictionary  
  表示索引鍵和值的集合  
  + ContainsKey  

+ ### LIST & Dictionary  
  obj 明明是List的東西  
  可是如果寫obj["ptInfo"]就會變成可以使用Dictionary的ContainsKey語法  
  不知道為何可以這樣oao  
  ...查到了，好像是因為變成JObject物件的關係，所以會變成像這樣子  
  而且好像...obj.ptInfo也會變成可以使用Dictionary的ContainsKey語法  
  ```  
  // results = {"RoomList": [{"id": 1, "ptInfo": {"patient": "pt01", "name": "Sandy"}}, {"id": 2, "ptInfo": {"patient": "pt02", "name": "Leo"}}]}
  
  List<dynamic> tmpList = new List<dynamic>(results.RoomList);
  foreach (var obj in tmpList){
    string id = obj.id;   //1 //2
    if (obj["ptInfo"].ContainsKey("patient"))
    {
        // obj["ptInfo"].patient = obj.ptInfo.patient
        // obj["ptInfo"] => Dictionary
        // obj.ptInfo.patient => List
        string patid = obj["ptInfo"].patient;  //Sandy  //Leo
    }
  }
  ```  
+ ### Type  
  + .GetType()  
    取得Type  
    ```
    // .Name -> 取得這個type的名稱字串
    string test3 = obj.GetType().Name;
    ```


*****
[Dictionary](https://msdn.microsoft.com/zh-tw/library/xfhwa508(v=vs.110).aspx)  

