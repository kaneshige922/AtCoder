/**
*    author:  kaneshige
*    created: 09.09.2021 00:39:08
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;
#define rep(i,n) for(ll (i)=0;(i)<(n);++(i))

int main() {
    ll n;ll C[3];
    cin >> n>> C[0]>> C[1]>> C[2];
    sort(C,C+3,greater<ll>());
    ll ans = 10000;
    rep(i,10000){
        ll m = n;
        rep(j,10000-i){
            ll x = n-C[0]*i-C[1]*j;
            if(x>=0 && x%C[2]==0){
                ans = min(ans,i+j+x/C[2]);
            }
        }
    }
    cout << ans << endl;
}
