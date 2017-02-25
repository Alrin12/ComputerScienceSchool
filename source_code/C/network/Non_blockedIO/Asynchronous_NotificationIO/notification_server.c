#include <stdio.h>
#include <string.h>
#include <WinSock2.h>

#pragma comment(lib, "ws2_32.lib")

#define BUF_SIZE 1024

void CompressEvents(WSAEVENT hEventArr[], int idx, int total)
{
	for (int i = idx; i < total; i++)
		hEventArr[i] = hEventArr[i + 1];
}

void CompressSockets(SOCKET hSockArr[], int idx, int total);

void ErrorHandling(char * message);

int main(int argc, char * argv[])
{
	WSADATA wsaData;
	SOCKET hServSock, hClntSock;
	SOCKADDR_IN servAddr, clntAddr;
	int sz_clntAddr;

	WSAEVENT evObj;
	WSANETWORKEVENTS netEvents;

	SOCKET hSockArr[WSA_MAXIMUM_WAIT_EVENTS];
	WSAEVENT hEventArr[WSA_MAXIMUM_WAIT_EVENTS];

	int numOfSock = 0;
	int strLen, i;
	int posInfo, startIdx;

	char buf[BUF_SIZE];

	if (argc != 2)
	{
		printf("usage : %s <IP> <port> \n", argv[0]);
		exit(-1);
	}

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

	if (listen(hServSock, 5) == SOCKET_ERROR)
		ErrorHandling("listen() error!");

	evObj = WSACreateEvent();
	if (WSAEventSelect(hServSock, evObj, FD_ACCEPT) == SOCKET_ERROR)
		ErrorHandling("WSAEventSelect() error!");

	hSockArr[numOfSock] = hServSock;
	hEventArr[numOfSock] = evObj;
	numOfSock++;

	while (1)
	{
		posInfo = WSAWaitForMultipleEvents(numOfSock, hEventArr, FALSE, WSA_INFINITE, FALSE);
		startIdx = posInfo - WSA_WAIT_EVENT_0;

		for (i = startIdx; i < numOfSock; i++)
		{
			int signaled_obj_idx = WSAWaitForMultipleEvents(1, &hEventArr[i], TRUE, 0, FALSE);
			
			if (signaled_obj_idx == WSA_WAIT_FAILED || signaled_obj_idx == WSA_WAIT_TIMEOUT)
				continue;
			else
			{
				signaled_obj_idx = i;
				WSAEnumNetworkEvents(hSockArr[signaled_obj_idx], hEventArr[signaled_obj_idx], &netEvents);

				if (netEvents.lNetworkEvents & FD_ACCEPT)
				{
					if (netEvents.iErrorCode[FD_ACCEPT_BIT] != 0)
					{
						puts("Accept Error!");
						return -1;
					}

					sz_clntAddr = sizeof(clntAddr);
					hClntSock = accept(hSockArr[signaled_obj_idx], (SOCKADDR*)&clntAddr, &sz_clntAddr);
					evObj = WSACreateEvent();
					WSAEventSelect(hClntSock, evObj, FD_READ | FD_CLOSE);

					hSockArr[numOfSock] = hClntSock;
					hEventArr[numOfSock] = evObj;
					numOfSock++;
					puts("connected new client");
				}

				if (netEvents.lNetworkEvents & FD_READ)
				{
					if (netEvents.iErrorCode[FD_READ_BIT] != 0)
					{
						puts("Read Error!");
						return -1;
					}
					strLen = recv(hSockArr[signaled_obj_idx], buf, BUF_SIZE, 0);
					send(hSockArr[signaled_obj_idx], buf, strLen, 0);
				}

				if (netEvents.lNetworkEvents & FD_CLOSE)
				{
					if (netEvents.iErrorCode[FD_CLOSE_BIT] != 0)
					{
						puts("Close error!");
						return -1;
					}
					WSACloseEvent(hEventArr[signaled_obj_idx]);
					closesocket(hSockArr[signaled_obj_idx]);

					numOfSock--;
					CompressSockets(hSockArr, signaled_obj_idx, numOfSock);
					CompressEvents(hEventArr, signaled_obj_idx, numOfSock);
				}
			}
		}
	}

	WSACleanup();
	return 0;
}

void CompressSockets(SOCKET hSockArr[], int idx, int total)
{
	for (int i = idx; i < total; i++)
		hSockArr[i] = hSockArr[i + 1];
}



void ErrorHandling(char * message)
{
	fputs(message, stderr);
	fputc('\n', stderr);
	exit(-1);
}
