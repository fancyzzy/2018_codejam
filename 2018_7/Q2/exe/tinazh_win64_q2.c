#include<stdio.h>
#include<string.h>
int gift_sum=0;


int main()
{
    int i=0;int sum=0;int flag=0;
    int a[100000];
    int v[100000];
    v[0]=1;

    char ch;
    do
    {
       scanf("%d",&a[i++]);
       sum++;
    }while((ch=getchar())!='\n');

    for (i=0;i<(sum-1);i++)

    {

        if (a[i]<a[i+1])
        {
            v[i+1]=v[i]+1;
        }
        else if (a[i]==a[i+1])
            {
                v[i+1]=1;
            }
        else if  (a[i]>a[i+1])
            {
                v[i+1]=1;
                if (v[i]==1)
                    v[i]++;
            }

        else
        {

        }

    }

       for(i=0;i<sum;i++)
        {
            gift_sum+=v[i];
        }

    printf("%d",gift_sum);
        return 0;
    }





