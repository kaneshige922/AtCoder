/**
*    author:  kaneshige
*    created: 03.09.2021 19:57:46
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;

//‰ðàAC
int main() {
    ll n,d;cin >> n >> d;
    vector<int> cnt;
    for(const auto& v:{2,3,5}){
        int c = 0;
        while (d%v==0){
            d /= v;
            c++;
        }
        cnt.push_back(c);
    }
    //cout << cnt[0] << " " << cnt[1] << " " << cnt[2] << endl;
    if(d!=1){cout << 0 << endl;exit(0);}
    //–Ú‚²‚Æ‚Ì‘fˆö”ƒŠƒXƒg
    int d2[6] = {0,1,0,2,0,1};
    int d3[6] = {0,0,1,0,0,1};
    int d5[6] = {0,0,0,0,1,0};

    vector<vector<vector<vector<double>>>> dp(n+1,vector<vector<vector<double>>>(cnt[0]+1,vector<vector<double>>(cnt[1]+1,vector<double>(cnt[2]+1,0))));
    dp[0][0][0][0] = 1.0;

    for(int i=1;i<=n;i++){
        for(int x=0;x<cnt[0]+1;x++){
            for(int y=0;y<cnt[1]+1;y++){
                for(int z=0;z<cnt[2]+1;z++){
                    for(int t=0;t<6;t++){
                        int dx = min(x+d2[t],cnt[0]);
                        int dy = min(y+d3[t],cnt[1]);
                        int dz = min(z+d5[t],cnt[2]);
                        dp[i][dx][dy][dz] += dp[i-1][x][y][z]/6.0;
                    }
                }
            }
        }
    }
    cout << dp[n][cnt[0]][cnt[1]][cnt[2]] << endl;
}
