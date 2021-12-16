/**
*    author:  kaneshige
*    created: 07.09.2021 01:23:17
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;
#define rep(i,n) for(ll (i)=0;(i)<(n);++(i))

int main() {
    ll n,l,k;
    cin >> n >> l >> k;
    vector<ll> A;
    A.push_back(0);
    rep(i,n){
        ll a; cin >> a;
        A.push_back(a);
    }
    A.push_back(l);
    ll left = 1;
    ll right = l/(k+1ll)+1ll;
    while(right-left>1ll){
        ll middle = (left+right)/2ll;
        ll cnt = 0; ll length = 0;
        for(ll i=1;i<=n+1;i++){
            length += A[i]-A[i-1];
            if(length >= middle){
                cnt += 1ll;
                length = 0ll;
            }
        }
        if(cnt >= k+1){
            left = middle;
        }else{
            right = middle;
        }
    }
    cout << left << endl;
}
