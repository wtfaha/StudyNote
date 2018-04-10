#include <stdio.h>
#include <stdlib.h>


int gapNumber(int state[], int totalPancakes) {
	int count = 0;
	for (int i = 1; i < totalPancakes; i++) {
		if (abs(state[i] - state[i - 1]) != 1)
			count++;
	}
	return count;
}

int main() {
	int n;
	scanf_s("%d", &n);
	for (int j = 0; j < n; j++) {
		int totalPancakes;
		scanf_s("%d", &totalPancakes);
		int *ptr;
		ptr = (int*)malloc(sizeof(double)*totalPancakes);	// 配置n個記憶體
		// 配置完後，和一般陣列的存取方式都一樣，可以用 *(ptr+i)、ptr[i]進行存取

		for (int i = 0; i < totalPancakes; i++) {
			scanf_s("%d", &ptr[i]);
		}

		int result = gapNumber(ptr, totalPancakes);
		printf("%d\n", result);
	}
	system("pause");
}