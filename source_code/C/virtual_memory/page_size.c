#include <stdio.h>
#include <Windows.h>

int main(int argc, char ** argv)
{
	SYSTEM_INFO sys_info;

	GetSystemInfo(&sys_info);

	printf("page size : %u bytes \n", sys_info.dwPageSize);

	return 0;
}