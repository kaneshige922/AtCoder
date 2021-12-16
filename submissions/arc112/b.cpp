/**
*    author:  kaneshige
*    created: 07.09.2021 22:13:36
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;
#define rep(i,n) for(ll (i)=0;(i)<(n);++(i))

int main() {
    ll b,c; cin >> b >> c;
    ll maxp,minp,maxm,minm;
    ll ans;
    maxp = b + (c-2)/2;
    minp = b - c/2;
    maxm = -b + (c-1)/2;
    minm = -b - (c-1)/2;
    if(b>0){
        if(minp > maxm){
            ans = maxp-minp+1 +maxm-minm+1;
        }else{
            ans = maxp-minm+1;
        }
    }else if(b == 0){
        maxp = b + (c-1)/2;
        ans = maxp-minp+1;
    }else{
        if(minm > maxp){
            ans = maxp-minp+1 +maxm-minm+1;
        }else{
            ans = maxm-minp+1;
        }
    }
    cout << ans << endl;
}
