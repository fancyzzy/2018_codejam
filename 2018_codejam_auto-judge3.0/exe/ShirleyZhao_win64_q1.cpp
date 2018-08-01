#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h> 

#define Max 2000
char string1[Max];
char string2[Max];
int s_alpha[200] = {0};
int t_alpha[200] = {0};

int main ()
{
	int len1 = 0, len2 = 0;
	int i = 0, j = 0, k = 0, l = 0, m = 0;
	char ch;

	/*Enter the parameter*/
	scanf("%s", string1);
	scanf("%s", string2);

	len1 = strlen(string1);
	len2 = strlen(string2);

	//printf("%d", strlen(string1));
	//printf("%d", strlen(string2));
	
	for (i = 0; i < len1; i++)
	{
		s_alpha[string1[i]]++;
	}
	
	for (j = 0; j < len2; j++)
	{
		t_alpha[string2[j]]++;
	}
	
	for (ch = 'a'; ch <= 'z'; ch++)
	{
		if (s_alpha[ch] != t_alpha[ch])
		{
			printf("%c\n", ch);
			break;
		}
	}

	return 0;
}