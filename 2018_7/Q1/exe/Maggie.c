#include<stdio.h>
#include<string.h>
#include<stdlib.h>

void bubble(char* str)
{
	int i, j, len;
	len = 0;
	len = strlen(str);//计算你输入的字符串的长度
	//冒泡排序（从小到大）
	for (i = 0; i<len - 1; i++)
		for (j = 0; j<len - i - 1; j++)
			if (*(str + j)>*(str + j + 1))
			{
				char t = *(str + j);
				*(str + j) = *(str + j + 1);
				*(str + j + 1) = t;
			}
	//printf("排序后的结果: %s\n", str);
}
void main()
{
	char str1[1000];
	char str2[1000];
	int  i,len1,len2;
	gets(str1);//键盘输入字符串
	gets(str2);
	len1 = strlen(str1);//获取字符串长度==》len
	len2 = strlen(str2);
	//printf("%d  %d\n", len1, len2);
	bubble(str1);//字符串排序
	bubble(str2);
	//if (strcmp(str1, str2) <0)//比较字符串长度
	if(len1>len2)
	{
		for (i = 0; i < len1; i++)
		{
			if (str1[i] != str2[i])//比较字符串内容
				break;
		}
		printf("%c \n", str1[i]);
	}
	else
	{
		for (i = 0; i < len2; i++)
		{
			if (str1[i] != str2[i])
				break;
		}
		printf("%c \n", str2[i]);
	}
	system("pause");
}