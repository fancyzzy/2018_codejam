#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define people_max 100000
#define True 1
#define False 0
int score[people_max] = {0};
int gift_num[people_max] = {0};


void Compare_add_gift (int people_num)
{
	int aa = 1;
	
	for (aa = 1; aa < people_num; aa++)
	{
		if (score[aa - 1] < score[aa])
		{
			if (gift_num[aa] <= gift_num[aa - 1])
			{
				gift_num[aa]++;
			}
		}
		else if (score[aa - 1] > score[aa])
		{
			if (gift_num[aa - 1] <= gift_num[aa])
			{
				gift_num[aa - 1]++;
			}
		}
	}

	/*for (aa = 0; aa < people_num; aa++)
	{
		printf ("%d ", gift_num[aa]);
	}
	printf ("\n");*/
	
	return;
}

int Check_result (int people_num)
{
	int bb = 1;
	int value = True;

	for (bb = 1; bb < people_num; bb++)
	{
		if (score[bb - 1] < score[bb])
		{
			if (gift_num[bb - 1] < gift_num[bb])
			{
				value = True;
			}
			else 
			{
				value = False;
				break;
			}
		}
		else if (score[bb - 1] > score[bb])
		{
			if (gift_num[bb - 1] > gift_num[bb])
			{
				value = True;
			}
			else
			{
				value = False;
				break;
			}
		}
	}
	
	return value;
}

int main ()
{
	int i = 0, j = 0;
	int people_num = 0;
	int result = 0;
	int final_gift = 0;
	char y;
	int sum = 0;
	
	do 
	{
		scanf ("%d", &score[i]);
		//printf ("score[%d] = %c\n", i, score[i]);
		i++;
	} while (y = getchar() != '\n');
	
	people_num = i;
	//printf ("people_num = %d\n", people_num);
	
	Compare_add_gift (people_num);
	result = Check_result(people_num);
	
	while (!result)
	{
		Compare_add_gift (people_num);
		result = Check_result(people_num);
		
		/*debug code*/
		sum++;
		if (sum >= 100000)
		{
			break;
		}
	}
	
	for (j = 0; j < people_num; j++)
	{
		final_gift += gift_num[j];
	}
	
	final_gift += people_num; 
	printf ("%d\n", final_gift);

	return 0;

}