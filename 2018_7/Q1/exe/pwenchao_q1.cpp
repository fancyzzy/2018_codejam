#include<iostream>
#include<string>
using namespace std;
int main()
{
	string A,B;
	int a=0,b=0,c=0;
	getline(cin,A);
	getline(cin,B);
	for(int i=0;i<A.size();i++)
	{
		a+=(int)(A[i]);
	}
	for(int i=0;i<B.size();i++)
	{	
		b+=(int)(B[i]);
	}
	c=b-a;
	cout<<(char)c<<endl;
	return 0;
	
}
