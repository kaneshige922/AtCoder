/**
*    author:  kaneshige
*    created: 03.09.2021 16:33:18
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;

int main() {
    int n;
    vector<int> p;
    cin >> n;
    for(int i=0;i<n;i++){int pi;cin>>pi;p.push_back(pi);}
    vector<vector<int>> dp;
    vector<int> dpi(100*n+1,0);
    dp.push_back(dpi);
    dp[0][0] = 1;
    for(int i=1;i<n+1;i++){
        vector<int> dpi;
        for(int j=0;j<100*n+1;j++){
            if (j-p[i-1]>=0){
                if(dp[i-1][j-p[i-1]] == 1 || dp[i-1][j]==1){
                    dpi.push_back(1);
                }else{
                    dpi.push_back(0);
                }
            }else if(dp[i-1][j]==1){
                dpi.push_back(1);
            }else{
                dpi.push_back(0);
            }
        }
        dp.push_back(dpi);
    }
    int ans = accumulate(dp[n].begin(),dp[n].end(),0);
    cout << ans << endl;
}
