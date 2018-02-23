# 作業系統
*****

+ ### 記憶體管理 : 內部碎片、外部碎片  
	+ 內部碎片 ：  
		內部碎片就是已經被分配出去（能明確指出屬於哪個行程）卻不能被利用的內存空間   
		```
		單道連續分配只有內部碎片。
		多道固定連續分配既有內部碎片，又有外部碎片 ex : 分頁
		```
	+ 外部碎片 ：  
		外部碎片指的是還沒有被分配出去（不屬於任何行程），但由於太小了無法分配給申請內存空間的新進程的內存空閒區域  
		```
		多道可變連續分配只有外部碎片 ex : 分段
		```
	+ 上述兩種記憶體碎片是否能完全避免其發生?
		```
		無論是記憶體內部碎片或是記憶體外部碎片皆無法完全避免
		```

+ ### 網路題目  
	+ 何謂虛擬記憶體(Virtual Memory)？其功能為何?  
		```
		一種經由作業系統控制的的記憶體管理技術
		利用分頁式(Paging)或分段式(Segment)記憶體管理技術
		使得程式及資料在主記憶體與次儲存間作置換(Swapping)
		```  
		```
		功能主要讓程式可以不受主記憶體實際大小的限制，允許程式使用比主記憶體更大的空間。
		程式執行時不需要同時將整個程式完全置於主記憶體，僅需將要執行的部分載入主記憶體即可。
		```  
		
	+ 分頁式記憶體管理系統(Paging System)與分段式記憶體管理系統(Segmentation System)的優缺點  
		分頁式記憶體管理系統(Paging System) ：  
		```
		優點：
		(1)可以減低記憶體碎片(Fragmentation)的程度。
		雖然解決了記憶體外部碎片(ExternalFragmentation)的問題，
		但卻也產生了記憶體內部碎片(Internal Fragmentation)。
		(2)可以提升多程式(Multiprogramming)的程度，使多個程式能同時被執行。
		(3)免於需要做記憶體壓擠(Compaction)的工作。
		(4)具有虛擬記憶體(Virtual Memory)的功能。
		(5)可有效的利用記憶體。
		缺點：
		(1)需要增加額外的硬體來處裡頁與頁幅之位址對應。
		(2)由於需要用到頁映成表(Page Map Table)，因此會造成表格碎片。
		(3)會產生記憶體內部碎片。
		(4)由於取頁失敗(Page Fault)時需要作頁的置換(Replacement)，因而造成 CPU 的負擔。
		(5)可能會產生動盪現象(Thrashing)，造成系統的效能降低)。
		```  
		分段式記憶體管理系統(Segmentation System)：  
		```
		優點：
		(1)動態性的連結(Linking)與載入(Loading)。
		(2)提供虛擬記憶體(Virtual Memory)的功能。
		(3)提供資料段共享(Sharable)的能力。
		(4)強化了存取控制(Access Control)的能力。
		缺點：
		(1)為了減少記憶體的外部碎片，因此需要浪費許多時間在記憶體壓擠的工作上。
		(2)段(Segment)的最大尺寸要受到實際記憶體大小的限制。
		(3)可能會造成動盪(Thrashing)的現象。
		```
		相似點 (Similarity)  
		```
		(1)兩者皆不需要配置連續的記憶體空間。
		(2)都用動態位址轉換的技巧(Dynamic Address Translation Mechanism,DAT Mechanism)及一
		些映成表(External Fragmentation)問題輔助。
		(3)可以改善記憶體的外部碎片(Internal Fagmentation)問題，仍是無法徹底解決。
		```
		相異點(Difference)  
		
		| # | 分段式記憶體管理系統 | 分頁式記憶體管理系統 |
		| :-----------------------:| :------------------------------:| :------------------------------:|
		| 記憶體碎片(Fragmentation) | 外部碎片(External Fragmentation) | 內部碎片(Internal Fragmrtation) |
		| 資料分享之處理(Sharable) | 容易(Easy) | 困難(Difficult) |
		| 系統的存取控制(Access Control) | 簡單(Simple) | 複雜(Complex) |
		| 每個單位的大小(Size) | 可變動(Arbitrary) | 固定(Fixed) |
		| 看待資料的觀點 | 邏輯單位(Logical Unit) | 實際單位(Physical Unit) |

	+ 何謂記憶體碎片 (Fragmentation)?何謂表格碎片 (Table Fragmentation)?  
		```
		```
		
	+ 為什麼分頁(Paging)系統與分段(Segmentation)系統有時會被整合起來使用？試說明其理由    
		```
		```
		
	+ 何謂虛擬記憶體(Virtual Memory)？其功能為何?  
		```
		```
	
	
	
	[九十三學年度_記憶體管理 參考解答](http://larrymao.myweb.hinet.net/2004fall/sp/exer/sphw06_ans.pdf)

		
*****
[組譯、編譯、直譯](http://blog.xuite.net/x_3kkk/java/11466883-%E7%B7%A8%E8%AD%AF%E3%80%81%E7%B5%84%E8%AD%AF%E3%80%81%E7%9B%B4%E8%AD%AF)  

