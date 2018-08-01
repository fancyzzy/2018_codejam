#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int main( )
{
   char s[1000]={'\0'};
   char t[1000]={'\0'};
   int len_s;
   int len_t;   
  
   int i=0,j=0,l=0;

   char small;    char temp;
   
   char one;
   
   int  k;
   
/*	for(k = 0; k < 1000; k++ )
    {
      s[k]=0;       
	  t[k]=0;
	 }   */
    
	scanf("%s",s); 
	scanf("%s",t);
	
/*	printf("%s\n",s);
	printf("%s\n",t);  */
	
	len_s=strlen(s);
	len_t=strlen(t);
	
/*	printf("%d\n",len_s);
	printf("%d\n",len_t);  */
	
	
	for(i=0;i<len_s-1;i++)
	{
     small=s[i];
	 
   	for(j=i+1;j<len_s;j++)
	 {
	   
	 if(small>s[j])
	 {
	  temp=small;
	  small=s[j];
	  s[i]=small;
	  s[j]=temp;
/*	  printf("small=%c,temp=%c\n",small,temp);
	  printf("s[%d]=%c,s[%d]=%c\n",i,s[i],j,s[j]);   */
	  }
	  }
	  }
	  
	for(i=0;i<len_t-1;i++)
	{
     small=t[i];
   	for(j=i+1;j<len_t;j++)
	 {
	   
	 if(small>t[j])
	 {
	  temp=small;
	  small=t[j];
	  t[i]=small;
	  t[j]=temp;
/*	  printf("small=%c,temp=%c\n",small,temp); */
	  }
	  }
	  }
	  
/*	printf("%s\n",s);
	printf("%s\n",t);  */
	  
	  one=0;
	  
	  for(i=0;i<len_s && one==0;i++)
	  {
	   if(s[i]!=t[i])
	   {
	    one=t[i];
		}
		}
/*		printf("i=%d, one=%d\n",i,one);   */
		if(one==0)
		{
		 one=t[i];
		}
		
		printf("%c\n",one);		
		}
	  
	
	
	
	
	