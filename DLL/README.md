
# C#語法
*****  
Dictionary  
*****  
+ ### Dictionary  
  表示索引鍵和值的集合  
  + ContainsKey  

+ ### LIST & Dictionary  
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



*****
[Dictionary](https://msdn.microsoft.com/zh-tw/library/xfhwa508(v=vs.110).aspx)  

