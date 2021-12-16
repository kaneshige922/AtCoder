/**
*    author:  kaneshige
*    created: 13.09.2021 19:23:09
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;
#define rep(i,n) for(ll (i)=0;(i)<(n);++(i))

int main() {
    ll a,b,c;
    cin >> a >> b >> c;
    ll g = __gcd(a,b);
    g = __gcd(g,c);
    ll ans = (a+b+c)/g-3ll;
    cout << ans << endl;
}
