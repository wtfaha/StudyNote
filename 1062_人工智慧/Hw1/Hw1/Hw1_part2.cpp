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
		ptr = (int*)malloc(sizeof(double)*totalPancakes);	// �t�mn�ӰO����
		// �t�m����A�M�@��}�C���s���覡���@�ˡA�i�H�� *(ptr+i)�Bptr[i]�i��s��

		for (int i = 0; i < totalPancakes; i++) {
			scanf_s("%d", &ptr[i]);
		}

		int result = gapNumber(ptr, totalPancakes);
		printf("%d\n", result);
	}
	system("pause");
}