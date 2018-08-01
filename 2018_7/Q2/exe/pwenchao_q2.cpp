#include<iostream>
#include<vector>
#include<string>
#include<sstream>
using namespace std;
int main()
{
	vector<int> arr;
	vector<int> tmp;
	string score;
	getline(cin,score);
	stringstream stringin(score);
	int num;
	while(stringin>>num)
	{
		arr.push_back(num);
	}
	for(int i=0;i<arr.size();i++)
	{
		tmp.push_back(0);
	}
	int z(0);
	int y(0);
	int sum(0);
	for(int i=0;i<arr.size();i++)
	{
		if(i==0)
		{
			if(arr[0]<=arr[1])
			{
				tmp[0]=1;
			}
			else
			{
				for(int j=1;j<(arr.size()-1);j++)
				{
					if(arr[j]>arr[j+1])
					{
						z++;
					}
					else
					{
						break;
					}
				}
				tmp[0]=z+2;
				z=0;
			}
			
		}
		else if(i==(arr.size()-1))
		{
			if(arr[(arr.size()-2)]<arr[(arr.size()-1)])
			{
				tmp[(arr.size()-1)]=tmp[(arr.size()-2)]+1;
			}
			else if(arr[(arr.size()-2)]==arr[(arr.size()-1)])
			{
				tmp[(arr.size()-1)]=1;
			}
			else 
			{
				tmp[(arr.size()-1)]=1;
			}
		}
		else
		{
			if(arr[i]>arr[i-1])
			{
				if(arr[i]>arr[i+1])
				{
					for(int j=i+1;j<(arr.size()-i);j++)
					{
						if(arr[j]>arr[j+1])
						{
							z++;
						}
						else
						{
							break;
						}
					}
					tmp[i]=tmp[i-1]+1+z;
					z=0;
				}
				else
				{
					tmp[i]=tmp[i-1]+1;
				}
			}
			else if(arr[i]==arr[i-1])
			{
				if(arr[i]>arr[i+1])
				{
					for(int j=i+1;j<(arr.size()-i);j++)
					{
						if(arr[j]>arr[j+1])
						{
							z++;
						}
						else
						{
							break;
						}
					}
					tmp[i]=2+z;
					z=0;
				}
				else 
				{
					tmp[i]=1;
				}
			}
			else if(arr[i]<arr[i-1])
			{
				if(arr[i]>arr[i+1])
				{
					for(int j=i+1;j<(arr.size()-i);j++)
					{
						if(arr[j]>arr[j+1])
						{
							z++;
						}
						else
						{
							break;
						}
					}
					tmp[i]=1+z;
					z=0;
					if(tmp[i]>=tmp[i-1])
					{
						tmp[i-1]+=1;
					}
				}
				else if(arr[i]==arr[i+1])
				{
					tmp[i]=1;
				}
				else 
				{
					tmp[i]=1;
					
				}
			}
		}
	}	
	
	for(int i=0;i<tmp.size();i++)
	{	
		sum+=tmp[i];
	}
	cout<<sum<<endl;
	return 0;
}


