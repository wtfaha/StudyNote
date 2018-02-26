# 資料結構
*****
# 樹
*****

+ ### 樹基本觀念  
	![](http://120.101.70.10/ds/lib/exe/fetch.php?media=wiki:complete_binary_tree.jpg)  
	```
	定義 1：樹的節點個數是一或多個有限集合，且：
	(1) 存在一個節點稱為根節點。
	(2) 在根節點下的節點分成n >= 0 個沒有交集的多個子集合t1、t2…, tn
	每一個子集合也是一棵樹，而這些樹稱為根節點的「子樹」（Subtree）
	樹在各節點之間不可以有迴圈，或不連結的左、右子樹
	```
	+ 根節點(Root)/樹根 :  沒有父節點的節點  
		ex : A  
		
	+ 子節點(Children)/分支(Branch)/樹枝 :  
		ex : B、C為A的子節點  
		
	+ 父節點(Parent) :  
		ex : A為B、C的父節點  
		
	+ 兄弟節點(Siblings) :  
		ex : B、C擁有共同父節點，為兄弟節點  
		
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
		例如：上述圖例的節點A階層是1，B、C是階層2，D、E、F、G是階層3  
		
	+ 樹高（Height）：樹高又稱為樹深（Depth），指樹的最大階層數。
		ex：上述圖例的樹高是3   

+ ### 二元樹
	```
	定義2：二元樹的節點個數是一個有限集合，或是沒有節點的空集合。
	二元樹的節點可以分成兩個沒有交集的子樹，稱為「左子樹」（Left Subtree）和「右子樹」（Right Subtree）。
	```
	+ 歪斜樹 :  
	![](http://slidesplayer.com/11358378/61/images/10/7-2+%E4%BA%8C%E5%85%83%E6%A8%B9%E7%9A%84%E5%9F%BA%E7%A4%8E-%E6%AD%AA%E6%96%9C%E6%A8%B9+%E5%B7%A6%E9%82%8A%E9%80%99%E6%A3%B5%E6%A8%B9%E6%B2%92%E6%9C%89%E5%8F%B3%E5%AD%90%E6%A8%B9%EF%BC%8C%E5%8F%B3%E9%82%8A%E9%80%99%E6%A3%B5%E6%A8%B9%E6%B2%92%E6%9C%89%E5%B7%A6%E5%AD%90%E6%A8%B9%EF%BC%8C%E9%9B%96%E7%84%B6%E6%93%81%E6%9C%89%E7%9B%B8%E5%90%8C%E7%AF%80%E9%BB%9E%EF%BC%8C%E4%BD%86%E6%98%AF%E9%80%99%E6%98%AF%E5%85%A9%E6%A3%B5%E4%B8%8D%E5%90%8C%E7%9A%84%E4%BA%8C%E5%85%83%E6%A8%B9%EF%BC%8C%E5%9B%A0%E7%82%BA%E6%89%80%E6%9C%89%E7%AF%80%E9%BB%9E%E9%83%BD%E6%98%AF%E5%90%91%E5%B7%A6%E5%AD%90%E6%A8%B9%E6%88%96%E5%8F%B3%E5%AD%90%E6%A8%B9%E6%AD%AA%E6%96%9C%EF%BC%8C%E7%A8%B1%E7%82%BA%E3%80%8C%E6%AD%AA%E6%96%9C%E6%A8%B9%E3%80%8D%EF%BC%88Skewed+Tree%EF%BC%89%EF%BC%8C%E5%A6%82%E4%B8%8B%E5%9C%96%E6%89%80%E7%A4%BA%EF%BC%9A.jpg)
	
	+ 完滿二元樹（FullBinary Tree）: 滿足二元樹的樹高是h且二元樹的節點數是2h-1
	![](http://pic.pimg.tw/emn178/1354416838-422111732.png)
		

*****
[資料結構的樹與二元樹](http://wayne.cif.takming.edu.tw/datastru/tree.pdf)  

