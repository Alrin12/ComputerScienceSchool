#include <stdio.h>
#include <stdlib.h>
#include <process.h>
#include <string.h>
#include <WinSock2.h>

#pragma comment(lib, "ws2_32.lib")

#define BUF_SIZE    1024
enum MODE { READ = 0, WRITE };

typedef struct __sockmodule
{
	SOCKET clntSock;
	SOCKADDR_IN clntAddr;
}SOCKMODULE, *LPSOCKMODULE;

typedef struct __bufmodule
{
	OVERLAPPED overlapped;
	char buf[BUF_SIZE];
	WSABUF databuf;
	int rwMode;
}BUFFERMODULE, *LPBUFFERMODULE;

DWORD WINAPI threadMain(LPVOID *);
void ErrorHandling(char * message);

int main(int argc, char ** argv)
{
	WSADATA wsaData;
	SOCKET hServSock;
	SOCKADDR_IN servAddr;
	HANDLE hCompletionPort;
	SYSTEM_INFO systemInfo;

	int recvBytes;
	int flag = 0;
	
	if (argc != 2)
	{
		printf("usage : %s <port> \n", argv[0]);
		exit(-1);
	}

	if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0)
		ErrorHandling("WSAStartup() error!");

	hServSock = WSASocket(PF_INET, SOCK_STREAM, 0, NULL, 0, WSA_FLAG_OVERLAPPED);
	if (hServSock == INVALID_SOCKET)
		ErrorHandling("WSASock() error!");

	hCompletionPort = CreateIoCompletionPort(INVALID_HANDLE_VALUE, NULL, 0, 0);
	GetSystemInfo(&systemInfo);

	memset(&servAddr, 0, sizeof(servAddr));
	servAddr.sin_family = AF_INET;
	servAddr.sin_addr.s_addr = htonl(INADDR_ANY);
	servAddr.sin_port = htons(atoi(argv[1]));

	if (bind(hServSock, (SOCKADDR*)&servAddr, sizeof(servAddr)) == SOCKET_ERROR)
		ErrorHandling("bind() error!");

	if (listen(hServSock, 5) == SOCKET_ERROR)
		ErrorHandling("listen() error!");

	for (int i = 0; i < systemInfo.dwNumberOfProcessors; i++)
	{
		_beginthreadex(NULL, 0, threadMain, (void *)hCompletionPort, 0, NULL);
	}

	while (1)
	{
		SOCKET hClntSock;
		SOCKADDR_IN clntAddr;
		int sz_clntAddr;
		LPSOCKMODULE lpclntmod;
		LPBUFFERMODULE lpbufmod;

		sz_clntAddr = sizeof(clntAddr);
		hClntSock = accept(hServSock, (SOCKADDR*)&clntAddr, &sz_clntAddr);
		if (hClntSock == INVALID_SOCKET)
			ErrorHandling("accept() error!");
		puts("new client connected.......");

		lpclntmod = (LPSOCKMODULE)malloc(sizeof(SOCKMODULE));
		lpbufmod = (LPBUFFERMODULE)malloc(sizeof(BUFFERMODULE));

		lpclntmod->clntSock = hClntSock;
		memcpy(&lpclntmod->clntAddr, &clntAddr, sizeof(SOCKADDR_IN));
		CreateIoCompletionPort((HANDLE)hClntSock, hCompletionPort, (DWORD)lpclntmod, 0);
		memset(&(lpbufmod->overlapped), 0, sizeof(lpbufmod->overlapped));
		lpbufmod->databuf.len = BUF_SIZE;
		lpbufmod->databuf.buf = lpbufmod->buf;
		lpbufmod->rwMode = READ;
		if (WSARecv(hClntSock, &lpbufmod->databuf, 1, &recvBytes, &flag, &lpbufmod->overlapped, NULL) == SOCKET_ERROR)
		{
			if (WSAGetLastError() != WSA_IO_PENDING)
				ErrorHandling("WSARecv()_1 error");
		}
	}

	closesocket(hServSock);
	WSACleanup();
	return 0;
}

DWORD WINAPI threadMain(LPVOID * lpcompletionport)
{
	int transBytes;
	DWORD flag = 0;
	LPSOCKMODULE sock_mod;
	LPBUFFERMODULE buf_mod;
	HANDLE hCompletionPort = (HANDLE)lpcompletionport;
	while (1)
	{
		GetQueuedCompletionStatus(hCompletionPort, &transBytes, &(LPDWORD)sock_mod, (LPOVERLAPPED *)&buf_mod, INFINITE);

		switch (buf_mod->rwMode)
		{
		case READ:
			if (transBytes == 0)
			{
				puts("client disconnected!");
				closesocket((SOCKET)sock_mod->clntSock);
				free(sock_mod);
				free(buf_mod);
				continue;
			}	
			puts("message received!");
			memset(&buf_mod->overlapped, 0, sizeof(buf_mod->overlapped));
			buf_mod->rwMode = WRITE;
			buf_mod->databuf.len = transBytes;

			if (WSASend((SOCKET)sock_mod->clntSock, &buf_mod->databuf, 1, NULL, 0, &buf_mod->overlapped, NULL) == SOCKET_ERROR)
			{
				if (WSAGetLastError() != WSA_IO_PENDING)
				{
					ErrorHandling("WSASend() error!");
				}
			}

			buf_mod = (LPBUFFERMODULE)malloc(sizeof(BUFFERMODULE));
			memset(&buf_mod->overlapped, 0, sizeof(buf_mod->overlapped));
			buf_mod->databuf.len = BUF_SIZE;
			buf_mod->databuf.buf = buf_mod->buf;
			buf_mod->rwMode = READ;

			if (WSARecv((SOCKET)sock_mod->clntSock, &(buf_mod->databuf), 1, NULL, &flag, &buf_mod->overlapped, NULL) == SOCKET_ERROR)
			{
				if (WSAGetLastError() != WSA_IO_PENDING)
					ErrorHandling("WSARecv()_2 error!");
			}
			break;
		case WRITE:
			puts("message transmitted");
			free(buf_mod);
			break;
		}
	}
	return 0;
}

void ErrorHandling(char * message)
{
	fputs(message, stderr);
	fputc('\n', stderr);
	exit(-1);
}
