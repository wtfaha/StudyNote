# Jquery
*****
file
*****

+ ### FileReader()  
  ```
    <input id="importFile" type="file" align="center" name="importFile" accept=".txt,.csv" style="border:1px solid #d5d5d5; width:85%%" onchange="chkExcel();"/>
  ```
  ```
    function chkExcel(){
      var obj_file = document.getElementById("importFile");
      var file = obj_file.files[0];
      console.log("file : " + file);

      // reader
      var reader = new FileReader();
      reader.onloadend = (function(self) {
          return function(e) {
              var re = /\,/i; 
              console.log("e.target.result : " + e.target.result);
          }
      })(file);
      reader.readAsBinaryString(file);
    }
  ```
