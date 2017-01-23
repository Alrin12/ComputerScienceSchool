#include <stdio.h>
#include <Windows.h>
#include <process.h>

#define THREAD_NUM    30

//전역변수, 즉 공유자원
long long num = 0;

//multithread main function
unsigned WINAPI AddOne(void *);
unsigned WINAPI SubtractOne(void *);

int main(void)
{
	HANDLE threadArr[THREAD_NUM];

	for (int i = 0; i < THREAD_NUM; i += 2)
	{
		threadArr[i] = (HANDLE)_beginthreadex(0, 0, AddOne, 0, 0, 0);
		threadArr[i + 1] = (HANDLE)_beginthreadex(0, 0, SubtractOne, 0, 0, 0);
	}

	WaitForMultipleObjects((DWORD)THREAD_NUM, threadArr, TRUE, INFINITE);

	printf("result = %lld \n", num);
	return 0;
}

unsigned WINAPI AddOne(void *)
{
	for (int i = 0; i <= 100000; i++)
		num++;
	return 0;
}

unsigned WINAPI SubtractOne(void *)
{
	for (int i = 0; i <= 100000; i++)
		num--;

	return 0;
}
