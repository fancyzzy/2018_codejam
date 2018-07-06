#include<iostream>
#include<string.h>
using namespace std;

bool used[20];
int a[20][20];
int n, ans;

void dfs(int deep, int sum){

    if(deep == n/2){
        ans = max(ans, sum);
        return;
    }
    for(int i = 1; i <= n; i++){
        if(!used[i]){
            for(int j = i+1; j <= n; j++){
                if(!used[j]){
                    used[i] = used[j] = true;
                    dfs(deep+1, sum + a[i][j]);
                    used[i] = used[j] =false;
                }
            }
        }

    }
}

int main(){
    int i, j;
    cin>>n;
    for(i = 1; i <= n; i++){
        for(j = 1; j <= n; j++)
            cin>>a[i][j];
    }
    memset(used, false, sizeof(used));
    ans = 0;
    dfs(0,0);
    cout<<ans<<endl;
    return 0;
}

