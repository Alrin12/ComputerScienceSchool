#include <stdio.h>
#include <Windows.h>
#include <process.h>

#define ARR_SIZE   100
#define THREAD_NUM    4

long long gSum = 0;
int cnt = 0;
HANDLE hMutex;

unsigned WINAPI SumArr(void *);

int main(int argc, char ** argv)
{
	unsigned int threadIDArr[THREAD_NUM];
	//threadArray
	HANDLE threadArray[THREAD_NUM];
	hMutex = CreateMutex(NULL, FALSE, NULL);
	
	int arr1[ARR_SIZE];
	int arr2[ARR_SIZE];
	int arr3[ARR_SIZE];
	int arr4[ARR_SIZE];

	int i = 0;
	int start_i = 0;
	int end_i = ARR_SIZE;
	long long sum = 0;

	for (i = start_i; i < end_i; i++)
		arr1[i] = i + 1;
	start_i += ARR_SIZE;
	end_i += ARR_SIZE;

	for (i = start_i; i < end_i; i++)
		arr2[i-start_i] = i + 1;
	start_i += ARR_SIZE;
	end_i += ARR_SIZE;

	for (i = start_i; i < end_i; i++)
		arr3[i- start_i] = i + 1;
	start_i += ARR_SIZE;
	end_i += ARR_SIZE;

	for (i = start_i; i < end_i; i++)
		arr4[i- start_i] = i + 1;
	
	threadArray[0] = (HANDLE)_beginthreadex(NULL, 0, SumArr, (void*)arr1, 0, &threadIDArr[0]);
	printf("threadID %d starts running!\n", threadIDArr[0]);

	threadArray[1] = (HANDLE)_beginthreadex(NULL, 0, SumArr, (void*)arr2, 0, &threadIDArr[1]);
	printf("threadID %d starts running!\n", threadIDArr[1]);

	threadArray[2] = (HANDLE)_beginthreadex(NULL, 0, SumArr, (void*)arr3, 0, &threadIDArr[2]);
	printf("threadID %d starts running!\n", threadIDArr[2]);
	threadArray[3] = (HANDLE)_beginthreadex(NULL, 0, SumArr, (void*)arr4, 0, &threadIDArr[3]);
	printf("threadID %d starts running!\n", threadIDArr[3]);

	WaitForMultipleObjects(4, threadArray, TRUE, INFINITE);
	printf("the gSum is %d \n", gSum);
	printf("the number of threads is %d \n", cnt);
	
	CloseHandle(hMutex);

	return 0;
}

unsigned WINAPI SumArr(void * arg)
{
	long long sum = 0;
	int * arr = (int*)arg;

	for (int i = 0; i < ARR_SIZE; i++)
	{
		sum += arr[i];
		printf("%d is added!\n", arr[i]);
	}
	WaitForSingleObject(hMutex, INFINITE);
	gSum += sum;
	cnt++;
	ReleaseMutex(hMutex);
	return 0;
}
