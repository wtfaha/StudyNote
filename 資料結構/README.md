# 資料結構
*****
# 樹
*****

+ ### 樹基本觀念  
	![](http://120.101.70.10/ds/lib/exe/fetch.php?media=wiki:complete_binary_tree.jpg)  
	+ 根節點(Root)/樹根 :  沒有父節點的節點  
		ex : A  
	+ 子節點(Children)/分支(Branch)/樹枝 :  
		ex : B、C為A的子節點  
	+ 父節點(Parent) :  
		ex : A為B、C的父節點  
	+ 兄弟節點(Siblings) :  
		ex : B、C擁有共同父節點，為兄弟節點  
	```
	定義 1：樹的節點個數是一或多個有限集合，且：
	(1) 存在一個節點稱為根節點。
	(2) 在根節點下的節點分成n >= 0 個沒有交集的多個子集合t1、t2…, tn
	每一個子集合也是一棵樹，而這些樹稱為根節點的「子樹」（Subtree）
	樹在各節點之間不可以有迴圈，或不連結的左、右子樹
	```
	
	+ n元樹：樹的一個節點最多擁有n個子節點  
	+ 二元樹（Binary Trees）：樹的節點最多只有兩個子節點  
	+ 葉節點（Leaf）：節點沒有子節點的節點稱為葉節點  
		ex：節點F、G、H、I、J和K  
	+ 祖先節點（Ancenstors）：指某節點到根節點之間所經過的所有節點，都是此節點的祖先節點  
	+ 非終端節點（Noterminal Nodes）：除了葉節點之外的其它節點稱為非終端節點  
		ex：A、B、C、D和E  
	+ 分支度（Dregree）：指每個節點擁有的子節點數
		ex：節點B的分支度是2  
	+ 階層（Level）：如果樹根是1，其子節點是2，依序可以計算出樹的階層數。
		例如：上述圖例的節點A階層是1，B、C是階層2，D、E、F、G是階層3。
	+ 樹高（Height）：樹高又稱為樹深（Depth），指樹的最大階層數。
		ex：上述圖例的樹高是3   

*****
[資料結構的樹與二元樹](http://wayne.cif.takming.edu.tw/datastru/tree.pdf)  

