/**
*    author:  kaneshige
*    created: 08.09.2021 01:56:54
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;
#define rep(i,n) for(ll (i)=0;(i)<(n);++(i))

int main() {
    ll n; cin >> n;
    string s; cin >> s;
    ll dp[n+1][8];
    rep(i,n+1){
        rep(j,8){
            dp[i][j] = 0;
        }
    }
    dp[0][0] = 1;
    rep(i,n){
        rep(j,8){
            dp[i+1][j] = dp[i][j];
        }
        if(s[i] == 'a'){
            dp[i+1][1] += dp[i][0];
        }else if(s[i] == 't'){
            dp[i+1][2] += dp[i][1];
        }else if(s[i] == 'c'){
            dp[i+1][3] += dp[i][2];
        }else if(s[i] == 'o'){
            dp[i+1][4] += dp[i][3];
        }else if(s[i] == 'd'){
            dp[i+1][5] += dp[i][4];
        }else if(s[i] == 'e'){
            dp[i+1][6] += dp[i][5];
        }else if(s[i] == 'r'){
            dp[i+1][7] += dp[i][6];
        }
        rep(j,8){
            dp[i+1][j] %= 1000000007;
        }
    }
    /*
    rep(i,8){
        rep(j,n+1){
            cout << dp[j][i]<< " ";
        }
        cout << endl;
    }
    */
    cout << dp[n][7]%1000000007ll << endl;
}
