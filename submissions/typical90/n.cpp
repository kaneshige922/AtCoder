/**
*    author:  kaneshige
*    created: 09.09.2021 00:29:58
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;
#define rep(i,n) for(ll (i)=0;(i)<(n);++(i))

int main() {
    ll n; cin >> n;
    vector<ll> A;
    vector<ll> B;
    rep(i,n){
        ll a; cin >> a;
        A.push_back(a);
    }
    rep(i,n){
        ll b; cin >> b;
        B.push_back(b);
    }
    sort(A.begin(),A.end());
    sort(B.begin(),B.end());
    ll ans = 0;
    rep(i,n){
        ans += abs(A[i]-B[i]);
    }
    cout << ans << endl;
}
