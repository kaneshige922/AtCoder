/**
*    author:  kaneshige
*    created: 10.09.2021 21:31:35
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;
#define rep(i,n) for(ll (i)=0;(i)<(n);++(i))

long long modpow(long long a, long long n, long long mod) {
    long long res = 1;
    while (n > 0) {
        if (n & 1) res = res * a % mod;
        a = a * a % mod;
        n >>= 1;
    }
    return res;
}

int main() {
    ll n,p; cin >> n >>p;
    ll mod = 1000000007;
    ll ans = modpow(p-2,n-1,mod);
    ans = (p-1)*ans%mod;
    cout << ans << endl;
}
