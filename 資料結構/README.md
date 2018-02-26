# 資料結構
*****
# 樹
*****

+ ### 樹基本觀念  
	![](http://120.101.70.10/ds/lib/exe/fetch.php?media=wiki:complete_binary_tree.jpg) 
	+ 根節點(Root)/樹根 :  
		ex : A
	+ 子節點(Children)/分支(Branch)/樹枝 :  
		ex : B、C為A的子節點
	+ 父節點(Parent) :  
		ex : A為B、C的父節點
	+ 兄弟節點(Siblings) :  
		ex : B、C擁有共同父節點，為兄弟節點
	
	定義 1：樹的節點個數是一或多個有限集合，且：
	(1) 存在一個節點稱為根節點。
	(2) 在根節點下的節點分成n >= 0 個沒有交集的多個子集合t1、t2…, tn
	每一個子集合也是一棵樹，而這些樹稱為根節點的「子樹」（Subtree）
	樹在各節點之間不可以有迴圈，或不連結的左、右子樹
	

+ ### 字串  
	C 語言裡面沒有字串，字串其實是由字元陣列組成的
	```
	char name[] = "NoobTW";
	```
	**字串需要一個 ‘\0’ 符號做結尾**，來判斷這個字串已經結束了  
	![](http://120.101.70.10/ds/lib/exe/fetch.php?media=wiki:complete_binary_tree.jpg)  

	
*****
[資料結構的樹與二元樹](http://wayne.cif.takming.edu.tw/datastru/tree.pdf)  

[資料結構筆記(二)：陣列、字串與指標](https://noob.tw/data-structure-array)  

[資料結構筆記(三)：抽象資料結構(ADT)與Struct](https://noob.tw/data-structure-adt)  
