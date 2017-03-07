#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <process.h>
#include <WinSock2.h>

#pragma comment(lib, "ws2_32.lib")

#define BUF_SIZE    1024

enum MODE {RECV = 0, SEND};

typedef struct __sockmodule
{
	SOCKET clntSock;
	SOCKADDR_IN clntAddr;
}SOCKMODULE, *LPSOCKMODULE;

typedef struct __buffermodule
{
	OVERLAPPED overlapped;
	char buf[BUF_SIZE];
	WSABUF databuf;
	int rsMode;
}BUFFERMODULE, *LPBUFFERMODULE;

int WINAPI ThreadMain(void * lpCompletionPort);
void ErrorHandling(char * message);

int main(int argc, char ** argv)
{
	WSADATA wsaData;
	SOCKET hServSock, hClntSock;
	SOCKADDR_IN servAddr, clntAddr;
	int sz_clntAddr;
	SYSTEM_INFO system_info;
	HANDLE hCompletionPort;

	DWORD recvBytes;
	int flag = 0;

	if (argc != 2)
	{
		printf("usage %s <port> \n", argv[0]);
	}

	if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0)
		ErrorHandling("WSAStartup() error!");

	hServSock = WSASocket(PF_INET, SOCK_STREAM, 0, NULL, 0, WSA_FLAG_OVERLAPPED);
	if (hServSock == INVALID_SOCKET)
		ErrorHandling("WSASocket() error!");

	hCompletionPort = CreateIoCompletionPort(INVALID_HANDLE_VALUE, NULL, 0, 0);
	
	memset(&servAddr, 0, sizeof(servAddr));
	servAddr.sin_family = AF_INET;
	servAddr.sin_addr.s_addr = htonl(INADDR_ANY);
	servAddr.sin_port = htons(atoi(argv[1]));

	if (bind(hServSock, (SOCKADDR*)&servAddr, sizeof(servAddr)) == SOCKET_ERROR)
		ErrorHandling("bind() error!");

	if (listen(hServSock, 5) == SOCKET_ERROR)
		ErrorHandling("listen() error!");

	GetSystemInfo(&system_info);

	for (int i = 0; i < system_info.dwNumberOfProcessors; i++)
	{
		_beginthreadex(NULL, 0, ThreadMain, (void*)hCompletionPort, 0, NULL);
	}

	while (1)
	{
		LPSOCKMODULE lpsock_mod;
		LPBUFFERMODULE lpbuf_mod;

		sz_clntAddr = sizeof(clntAddr);
		hClntSock = accept(hServSock, (SOCKADDR*)&clntAddr, &sz_clntAddr);
		if (hClntSock == INVALID_SOCKET)
			ErrorHandling("accept() error!");
		puts("new client connected.....");
		lpsock_mod = (LPSOCKMODULE)malloc(sizeof(SOCKMODULE));
		lpbuf_mod = (LPBUFFERMODULE)malloc(sizeof(BUFFERMODULE));

		lpsock_mod->clntSock = hClntSock;
		memcpy(&lpsock_mod->clntAddr, &clntAddr, sizeof(clntAddr));

		lpbuf_mod->databuf.len = BUF_SIZE;
		lpbuf_mod->databuf.buf = lpbuf_mod->buf;
		lpbuf_mod->rsMode = RECV;
		memset(&lpbuf_mod->overlapped, 0, sizeof(lpbuf_mod->overlapped));

		CreateIoCompletionPort((HANDLE)hClntSock, hCompletionPort, (ULONG_PTR)lpsock_mod, 0);

		if (WSARecv(hClntSock, &lpbuf_mod->databuf, 1, &recvBytes, &flag, &lpbuf_mod->overlapped, NULL) == SOCKET_ERROR)
		{
			if (WSAGetLastError() != WSA_IO_PENDING)
				ErrorHandling("WSARecv() in main error!");
		}
	}

	closesocket(hServSock);
	WSACleanup();
	return 0;
}

int WINAPI ThreadMain(void * lpCompletionPort)
{
	HANDLE hCompletionPort = (HANDLE)lpCompletionPort;
	LPSOCKMODULE lpsock_mod;
	LPBUFFERMODULE lpbuf_mod;

	DWORD transBytes;
	int flag = 0;

	while (1)
	{
		GetQueuedCompletionStatus(hCompletionPort, &transBytes, &lpsock_mod, &lpbuf_mod, INFINITE);

		if (transBytes == 0)
		{
			puts("client disconnected!");
			closesocket(lpsock_mod->clntSock);
			free(lpsock_mod);
			free(lpbuf_mod);
			continue;
		}

		switch (lpbuf_mod->rsMode)
		{
		case RECV:
			puts("message received!");
			memset(&lpbuf_mod->overlapped, 0, sizeof(lpbuf_mod->overlapped));
			lpbuf_mod->databuf.len = strlen(lpbuf_mod->buf)+1;
			lpbuf_mod->rsMode = SEND;
			
			if (WSASend(lpsock_mod->clntSock, &lpbuf_mod->databuf, 1, NULL, 0, lpbuf_mod, NULL) == SOCKET_ERROR)
			{
				if (WSAGetLastError() != WSA_IO_PENDING)
					ErrorHandling("WSASend() error!");
			}

			lpbuf_mod = (LPBUFFERMODULE)malloc(sizeof(BUFFERMODULE));
			memset(&lpbuf_mod->overlapped, 0, sizeof(lpbuf_mod->overlapped));
			lpbuf_mod->databuf.len = BUF_SIZE;
			lpbuf_mod->databuf.buf = lpbuf_mod->buf;
			lpbuf_mod->rsMode = RECV;

			if (WSARecv(lpsock_mod->clntSock, &lpbuf_mod->databuf, 1, NULL, &flag, lpbuf_mod, NULL) == SOCKET_ERROR)
			{
				if (WSAGetLastError() != WSA_IO_PENDING)
					ErrorHandling("WSARecv() in threadMain error!");
			}
			break;
		case SEND:
			puts("message sent!");
			free(lpbuf_mod);
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
