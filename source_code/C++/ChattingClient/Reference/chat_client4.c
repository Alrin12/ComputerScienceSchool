#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <WinSock2.h>
#include <Windows.h>
#include <process.h>

#pragma comment(lib, "ws2_32.lib")

#define NAME_LEN    20
#define BUF_SIZE    1024

unsigned WINAPI SendMsg(void *);
unsigned WINAPI RecvMsg(void *);
void ErrorHandling(char * message);

static char name[NAME_LEN] = "[DEFAULT]";

int main(int argc, char * argv[])
{
	WSADATA wsaData;
	SOCKET hSocket;
	SOCKADDR_IN servAddr;

	HANDLE hThrd_Send;
	HANDLE hThrd_Recv;

	if (argc != 4)
	{
		printf("Usage : %s <IP> <port> <name> \n", argv[0]);
		exit(1);
	}

	if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0)
		ErrorHandling("WSAStartup() error!");

	sprintf(name, "[%s]", argv[3]);

	hSocket = socket(PF_INET, SOCK_STREAM, 0);
	if (hSocket == INVALID_SOCKET)
		ErrorHandling("socket() error!");
	memset(&servAddr, 0, sizeof(servAddr));
	servAddr.sin_family = AF_INET;
	servAddr.sin_addr.s_addr = inet_addr(argv[1]);
	servAddr.sin_port = htons(atoi(argv[2]));

	if (connect(hSocket, (SOCKADDR*)&servAddr, sizeof(servAddr)) == SOCKET_ERROR)
		ErrorHandling("connect() error!");

	hThrd_Recv = (HANDLE)_beginthreadex(NULL, 0, RecvMsg, (void*)&hSocket, 0, NULL);
	hThrd_Send = (HANDLE)_beginthreadex(NULL, 0, SendMsg, (void*)&hSocket, 0, NULL);

	WaitForSingleObject(hThrd_Send, INFINITE);
	WaitForSingleObject(hThrd_Send, INFINITE);
	
	closesocket(hSocket);
	WSACleanup();
	return 0;
}

unsigned WINAPI SendMsg(void * arg)
{
	SOCKET hsocket = *((SOCKET*)arg);
	char message[BUF_SIZE];
	char nameMsg[NAME_LEN + BUF_SIZE];
	int strLen;

	while (1)
	{
		fgets(message, BUF_SIZE, stdin);
		sprintf(nameMsg, "%s %s", name, message);
		strLen = strlen(nameMsg)+1;
		send(hsocket, nameMsg, strLen, 0);
	}
	return 0;
}

unsigned WINAPI RecvMsg(void * arg)
{
	int recvLen = 0;
	SOCKET hsocket = *((SOCKET*)arg);
	char nameMsg[NAME_LEN + BUF_SIZE];
	char cpyMsg[NAME_LEN + BUF_SIZE];
	char * exitPtr;

	while (1)
	{
		recvLen = recv(hsocket, nameMsg, NAME_LEN + BUF_SIZE - 1, 0);
		if (recvLen == -1)
			return -1;

		strcpy(cpyMsg, nameMsg);
		strtok(cpyMsg, " ");
		exitPtr = strtok(NULL, " ");

		if (!strcmp("q\n", exitPtr) || !strcmp("Q\n", exitPtr))
		{
			if (!strcmp(cpyMsg, name))
			{
				closesocket(hsocket);
				exit(0);
			}
			sprintf(nameMsg, "%s %s", cpyMsg, "¥‘¿Ã ≈¿Â«ﬂΩ¿¥œ¥Ÿ!\n");
		}
		fputs(nameMsg, stdout);
	}

	return 0;
}

void ErrorHandling(char * message)
{
	fputs(message, stderr);
	fputc('\n', stderr);
	exit(1);
}
