# 資料結構
*****

+ ### 河內塔  
	有3根直立的木棒(A, B, C)，最左邊的木棒(A)有n個由小到大的盤子  
	將全部盤子由最左邊的棒子移到最右邊(A → C)  
  	一次只能移動一個盤子  
  	較大的盤子不能放在較小的盤子上面 ⇒ 只能移動最上面的盤子  
	
	解法  
	```
	把問題分成數個步驟，每步驟的目的皆為將還沒移到目的地的盤子中最大的盤子移到目的地
	3根木棒可視為：出發點、輔助移動、目的地
	先將非最大的盤子移到輔助的木棒，再將最大盤子移到目的地，再將剩餘的盤子移到目的地
	```
  	
	**若盤子為n個 ⇒ 需移動![equation](http://latex.codecogs.com/gif.latex?2^{n}-1)次**  
	
	設計遞迴
	```
  	Base Case： if n = 1 ⇒ 直接由來源木棒移到目的木棒
  	General Case：
  	將n-1盤子 ⇒ 由來源木棒(A)移到輔助木棒(B)
  	將最大盤子 ⇒ 由來源木棒(A)移到目的木棒(C)
  	將還沒到目的盤子中最大者 ⇒ 由新的來源木棒(B)透過新的輔助木棒(A)移到目的木棒(C)	
  	```
  	演算法(JAVA)  
	```
  	void Towers(int Disk, char Src, char Dest, char Aux)
  	{
		if(Disk == 1)
			System.out.println("移動盤子" + Disk + "由" + Src + "到" + Dest);
		else
		{
			//先將較小的盤子移到輔助木棒
			Towers( Disk - 1, Src, Aux, Dest);

			//移最大的盤子到目的
			System.out.println("移動盤子" + Disk + "由" + Src + "到" + Dest);

			//將較小的盤子移到目的
			Towers(  Disk - 1, Aux, Dest, Src);
		}
  	}
  	```
	
	
*****
[河內塔](http://notepad.yehyeh.net/Content/DS/CH02/4.php)	

