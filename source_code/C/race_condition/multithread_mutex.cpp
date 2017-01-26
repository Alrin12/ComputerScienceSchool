#include <stdio.h>
#include <Windows.h>
#include <process.h>

#define THREAD_NUM    30
#define SWITCH    1

//전역변수, 즉 공유자원
long long num = 0;
int cnt = 0;

//multithread main function
unsigned WINAPI AddOne(void *);
unsigned WINAPI SubtractOne(void *);

#if SWITCH
HANDLE hMutex;
#endif

int main(void)
{
	HANDLE threadArr[THREAD_NUM];
	
#if SWITCH
	hMutex = CreateMutex(0, FALSE, 0);
#endif

	for (int i = 0; i < THREAD_NUM; i+=2)
	{
		//매개변수 
		//보안관련 정보, 디폴트는 NULL 전달
		//스레드에 할당할 스택 크기, 0 전달하면 디폴트 크기의 스택
		//스레드 메인 함수
		//스레드 메인에 전달할 arguments
		//스레드 생성 이후의 행동, 0 전달하면 생성과 동시에 실행 가능
		//스레드 ID를 저장하기 위한 변수의 주소값
		threadArr[i] = (HANDLE)_beginthreadex(0, 0, AddOne, 0, 0, 0);
		threadArr[i+1] = (HANDLE)_beginthreadex(0, 0, SubtractOne, 0, 0, 0);
	}

	WaitForMultipleObjects((DWORD)THREAD_NUM, threadArr, TRUE, INFINITE);

	printf("result = %lld in %d cnts \n", num, cnt);
	return 0;
}

unsigned WINAPI AddOne(void *)
{
#if SWITCH
	WaitForSingleObject(hMutex, INFINITE);
#endif
	for (int i = 0; i <= 100000; i++)
		num++;
	cnt++;
#if SWITCH
	ReleaseMutex(hMutex);
#endif
	return 0;
}

unsigned WINAPI SubtractOne(void *)
{
#if SWITCH
	WaitForSingleObject(hMutex, INFINITE);
#endif
	for (int i = 0; i <= 100000; i++)
		num--;
	cnt++;
#if SWITCH
	ReleaseMutex(hMutex);
#endif
	return 0;
}
