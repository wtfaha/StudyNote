#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>

// pass value
void swapPassValue(int c, int d) {
	int temp = c;
	c = d;
	d = temp;
}

// pass address
// *的意思是”指標Pointer”指標是用來儲存記憶體位址的
void swapPassAddress(int *c, int *d) {
	int temp = *c;
	*c = *d;
	*d = temp;
}

// pass reference
void swapPassReference(int &c, int &d) {
	int temp = c;
	c = d;
	d = temp;
}

int main() {
	int a = 5, b = 10;
	swapPassValue(a, b);	// pass value
	printf("pass value\n");
	printf(" %d %d \n", a, b);

	// pass address 1
	// 把a跟b的位址給swap副程式c跟d使用
	// &的意思就是要領出該變數的”位址”
	swapPassAddress(&a, &b);	
	printf("pass address 1\n");
	printf(" %d %d \n", a, b);

	// pass address 2 
	// 當第一個printf執行後，印出來的c跟d都是5
	// 可是下一行的d = &b執行後在印一次，c卻仍然是5，d卻變成了10
	// 傳指標，仍然也是call by value，只是那個value是指標本身，
	// 複製的內容也是指標本身，只不過那個值Value剛好就是位址address
	// 所以各位要大概瞭解call by address本質上也是call by value或者叫call by value of pointer
	printf("pass address 2\n");
	int *c = &a;
	int *d = c;
	printf("*c=%d *d=%d\n", *c, *d);
	printf("c=%d d=%d\n", c, d);
	d = &b;
	printf("*c=%d *d=%d\n", *c, *d);
	printf("c=%d d=%d\n", c, d);

	// 指標是專門用來儲存記憶體的位址，但指標本身也有自己的記憶體位址
	
	// pass reference
	// 傳參考的意思其實簡單來說就是變數的別名、綽號，因此c的記憶體位址跟主程式的a的位址一樣
	// 因為一樣，所以c做任何改變a也會跟著改變，d改變b也會跟著改變
	swapPassReference(a, b);	
	printf("pass reference\n");
	printf(" %d %d \n", a, b);
	
	return 0;
}