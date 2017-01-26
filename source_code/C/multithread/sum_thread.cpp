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

	int arr[ARR_SIZE];
	int offset = ARR_SIZE / 4;
	for (int i = 0; i < ARR_SIZE; i++)
		arr[i] = i + 1;


	for (int i = 0; i < THREAD_NUM; i++)
	{
		threadArray[i] = (HANDLE)_beginthreadex(NULL, 0, SumArr, (void*)(arr+ (i * offset)), 0, &threadIDArr[i]);
		printf("threadID %d is running \n", threadIDArr[i]);
	}

	WaitForMultipleObjects(4, threadArray, TRUE, INFINITE);
	printf("the gSum is %d \n", gSum);
	printf("the number of threads is %d \n", cnt);
	
	CloseHandle(hMutex);

	/*
	//to compare the sum with single thread!
	int sum = 0;
	for (int i = 0; i < ARR_SIZE; i++)
		sum += (i + 1);
	printf("single thread sum is %d \n", sum);
	*/

	return 0;
}

unsigned WINAPI SumArr(void * arg)
{
	long long sum = 0;
	int * arr = (int*)arg;
	int end_point = ARR_SIZE / 4;
	
	for (int i = 0; i < end_point; i++)
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
