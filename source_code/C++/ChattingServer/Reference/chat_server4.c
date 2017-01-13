#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <WinSock2.h>
#include <Windows.h>
#include <process.h>

#pragma comment(lib, "ws2_32.lib")

#define BUF_SIZE    1024
#define CLNT_SIZE    512

unsigned WINAPI HandleClnt(void *);
void SendMsg(char * msg, int len);
void ErrorHandling(char * message);

static int clntCnt=0;
static SOCKET hClntSocks[CLNT_SIZE];
static HANDLE hMutex;

int main(int argc, char * argv[])
{
	WSADATA wsaData;
	SOCKET hServSock, hSocket;
	SOCKADDR_IN servAddr, clntAddr;

	HANDLE hThread;

	int szClntAddr;

	if (argc != 2)
	{
		printf("Usage : %s <port> \n", argv[0]);
		exit(1);
	}

	hMutex = CreateMutex(NULL, FALSE, NULL);

	if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0)
		ErrorHandling("WSAStartup() error!");

	hServSock = socket(PF_INET, SOCK_STREAM, 0);
	if (hServSock == INVALID_SOCKET)
		ErrorHandling("socket() error!");
	memset(&servAddr, 0, sizeof(servAddr));
	servAddr.sin_family = AF_INET;
	servAddr.sin_addr.s_addr = htonl(INADDR_ANY);
	servAddr.sin_port = htons(atoi(argv[1]));

	if (bind(hServSock, (SOCKADDR*)&servAddr, sizeof(servAddr)) == SOCKET_ERROR)
		ErrorHandling("bind() error!");

	if (listen(hServSock, CLNT_SIZE) == SOCKET_ERROR)
		ErrorHandling("listen() error!");

	while (1)
	{
		szClntAddr = sizeof(clntAddr);
		hSocket = accept(hServSock, (SOCKADDR*)&clntAddr, &szClntAddr);
		if (hSocket == INVALID_SOCKET)
			ErrorHandling("accept() error!");

		WaitForSingleObject(hMutex, INFINITE);
		hClntSocks[clntCnt++] = hSocket;
		ReleaseMutex(hMutex);

		hThread = (HANDLE)_beginthreadex(NULL, 0, HandleClnt, (void*)&hSocket, 0, NULL);
		printf("Connected Client IP : %s, port : %d \n", inet_ntoa(clntAddr.sin_addr), clntAddr.sin_port);
	}
	closesocket(hServSock);
	CloseHandle(hMutex);
	WSACleanup();
	return 0;
}

unsigned WINAPI HandleClnt(void * arg)
{
	SOCKET hsocket = *((SOCKET*)arg);
	char message[BUF_SIZE];
	int recvLen = 0;

	while ((recvLen = recv(hsocket, message, BUF_SIZE, 0)) != 0)
	{
		if (recvLen == -1)
			break;

		SendMsg(message, recvLen);
	}

	WaitForSingleObject(hMutex, INFINITE);
	for (int i = 0; i < clntCnt; i++)
	{
		if (hsocket == hClntSocks[i])
		{
			for (int j = i; j < clntCnt - 1; j++)
				hClntSocks[j] = hClntSocks[j + 1];
		}
	}
	clntCnt--;
	ReleaseMutex(hMutex);
	printf("this socket is about to be closed!\n");
	closesocket(hsocket);

	return 0;
}

void SendMsg(char * msg, int len)
{
	WaitForSingleObject(hMutex, INFINITE);
	for (int i = 0; i < clntCnt; i++)
	{
		send(hClntSocks[i], msg, len, 0);
	}
	ReleaseMutex(hMutex);
}

void ErrorHandling(char * message)
{
	fputs(message, stderr);
	fputc('\n', stderr);
	exit(1);
}
