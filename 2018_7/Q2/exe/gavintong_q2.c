#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


  int M[10000]={'\0'};
  int P[10000]={'\0'};
  
  int len;
  int min,L;
  int n=0;
  
int cal_r(int x)
{
 /* printf("x=%d\n",x); */
   int i,j;
  
   i=x+1;
  
   if(M[i+1]<M[i] && i<len-1)
   {
 /*   printf("M[%d+1]=%d,M[%d]=%d\n",i,M[i+1],i,M[i]); */
	cal_r(i); 
	}
	
	  n=n+1;
	  if(P[i-1]<P[i]+1)
	  {
	    P[i-1]=P[i]+1;
	   }
	  
/*	  printf("n=%d, P[%d]=%d\n",n,i,P[i]); */
    
}
  
  
int cal_l(int x)
{
/*  printf("x=%d\n",x); */
   int i,j;
    
   i=x-1;
  
   if(M[i-1]<M[i] && i>0)
   {
/*    printf("M[%d-1]=%d,M[%d]=%d\n",i,M[i-1],i,M[i]); */
	 cal_l(i); 
	}
	  n=n+1;
	  if(P[i+1]<P[i]+1)
	  {
	   P[i+1]=P[i]+1;
	   }
/*	  printf("n=%d, P[%d]=%d\n",n,i,P[i]);  */

    
}  
  
int main( )
{

   int i,j,k;
   char ch;
  
   int sum=0;
  
   i=0;
   while(1)
   {
     scanf("%d",&M[i++]);
	 P[i-1]=1;
	 ch=getchar();
/*	 printf("M[%d]=%d,P[%d]=%d\n",i-1,M[i-1],i-1,P[i-1]);  */
     if(ch=='\n') 
	 {break;}
	}    
	len=i;
	
	min=M[0];
	L=0;
	
	for(i=1;i<len;i++)
	{
	 if (M[i]<min)
	 {
	  min=M[i];
	  L=i;
	  }
	 }
	 
/*	 printf("min=%d,L=%d\n",min,L);  */
	 
	 for(j=L;j<len-1;j++)
	 {
	   if(M[j+1]>M[j])
	   {
	    P[j+1]=P[j]+1;
		}
		
		if(M[j+1]<M[j])
		{
		 cal_r(j);

		  j=j+n-1;
		  n=0;
		 }
	  }
	 
	 for(j=L;j>0;j--)
	 {
	  if(M[j-1]>M[j])
	  {
	   P[j-1]=P[j]+1;
	   }
	   
	   	if(M[j-1]<M[j])
		{
		 cal_l(j);
	 
		 j=j-n+1;
		 n=0;
		 }
	   }
	  
     sum=0;
     
     for(i=0;i<len;i++)
     { 
      sum=sum+P[i];
 /*    printf("%d ",P[i]); */ 
      }
     
     printf("\n%d\n",sum);	 
	   
	 
	
	}
  
