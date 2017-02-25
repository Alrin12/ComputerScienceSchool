#include <stdio.h>
#include <string.h>
#include <WinSock2.h>

#pragma comment(lib, "ws2_32.lib")

#define BUF_SIZE   1024

void ErrorHandling(char * errmsg);

void CALLBACK OnCompleteReceive(DWORD, DWORD, LPWSAOVERLAPPED, DWORD);
void CALLBACK OnCompleteSend(DWORD, DWORD, LPWSAOVERLAPPED, DWORD);

typedef struct __module
{
	SOCKET clntsock;
	WSABUF databuf;
	char buf[BUF_SIZE];
} Module;

int main(int argc, char ** argv)
{
	WSADATA wsaData;
	SOCKET hServSock, hClntSock;
	SOCKADDR_IN servAddr, clntAddr;
	int sz_clntAddr;
	DWORD recvBytes;
	Module * clntModule;
	LPWSAOVERLAPPED lpOverlapped;
	int mode = 1;
	int flag = 0;
	
	if (argc != 2)
	{
		printf("usage : %s <port>\n", argv[0]);
		exit(-1);
	}

	if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0)
		ErrorHandling("WSAStartup() error!");

	hServSock = WSASocket(PF_INET, SOCK_STREAM, 0, NULL, 0, WSA_FLAG_OVERLAPPED);
	if (hServSock == INVALID_SOCKET)
		ErrorHandling("socket() for server socket error!");
	ioctlsocket(hServSock, FIONBIO, &mode);

	memset(&servAddr, 0, sizeof(servAddr));
	servAddr.sin_family = AF_INET;
	servAddr.sin_addr.s_addr = htonl(INADDR_ANY);
	servAddr.sin_port = htons(atoi(argv[1]));

	if (bind(hServSock, (SOCKADDR*)&servAddr, sizeof(servAddr)) == SOCKET_ERROR)
		ErrorHandling("bind() error!");

	if (listen(hServSock, 5) == SOCKET_ERROR)
		ErrorHandling("listen() error!");

	
	while (1)
	{
		SleepEx(100, TRUE);

		sz_clntAddr = sizeof(clntAddr);
		hClntSock = accept(hServSock, (SOCKADDR*)&clntAddr, &sz_clntAddr);
		
		if (hClntSock == INVALID_SOCKET)
		{
			if (WSAGetLastError() == WSAEWOULDBLOCK)
				continue;
			else
				ErrorHandling("accept() error!");
		}
		puts("new client connected!");
		
		lpOverlapped = (LPWSAOVERLAPPED)malloc(sizeof(WSAOVERLAPPED));
		memset(lpOverlapped, 0, sizeof(WSAOVERLAPPED));

		clntModule = (Module*)malloc(sizeof(Module));
		
		clntModule->clntsock = (DWORD)hClntSock;
		(clntModule->databuf).len = BUF_SIZE;
		(clntModule->databuf).buf = clntModule->buf;

		lpOverlapped->hEvent = (HANDLE)clntModule;
		if (WSARecv(hClntSock, &(clntModule->databuf), 1, &recvBytes,
			&flag, lpOverlapped, OnCompleteReceive) == SOCKET_ERROR)
		{
			if (WSAGetLastError() != WSA_IO_PENDING)
				ErrorHandling("WSARecv()_1 error!");
		}

	}
	closesocket(hServSock);
	WSACleanup();
	return 0;
}

void ErrorHandling(char * errmsg)
{
	fputs(errmsg, stderr);
	fputc('\n', stderr);
	exit(-1);
}

void CALLBACK OnCompleteReceive(DWORD dwError, DWORD recvSize , LPWSAOVERLAPPED lpoverlapped, DWORD flags)
{
	DWORD sendBytes = 0;
	
	Module * mod = (Module*)lpoverlapped->hEvent;
	SOCKET sock = (SOCKET)mod->clntsock;

	if (recvSize == 0)
	{
		closesocket(sock);
		free(mod);
		free(lpoverlapped);
		puts("client disconnected!");
	}
	else
	{
		mod->databuf.len = recvSize;
		if (WSASend(sock, &(mod->databuf), 1, &sendBytes, 0, lpoverlapped, OnCompleteSend) == SOCKET_ERROR)
		{
			if (WSAGetLastError() != WSA_IO_PENDING)
				ErrorHandling("WSASend() error!");
		}
	}
}

void CALLBACK OnCompleteSend(DWORD dwError, DWORD sendSize, LPWSAOVERLAPPED lpoverlapped, DWORD flags)
{
	if (dwError != 0)
		ErrorHandling("Send error!");

	DWORD recvBytes = 0;
	int flag = 0;

	Module * mod = (Module*)lpoverlapped->hEvent;
	SOCKET sock = (SOCKET)mod->clntsock;

	mod->databuf.len = BUF_SIZE;
	if (WSARecv(sock, &(mod->databuf), 1, &recvBytes, &flag, lpoverlapped, OnCompleteReceive) == SOCKET_ERROR)
	{
		if (WSAGetLastError() != WSA_IO_PENDING)
			ErrorHandling("WSARecv()_2 error!");
	}
}
