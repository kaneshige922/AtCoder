/**
*    author:  kaneshige
*    created: 07.09.2021 00:53:25
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;
#define rep(i,n) for(ll (i)=0;(i)<(n);++(i))

int main() {
    int n; cin >> n;
    ll ans;
    cin >> ans;
    rep(i,n-1){
        ll t;
        cin >> t;
        ans = ans/__gcd(ans,t)*t;
    }
    cout << ans << endl;
}
