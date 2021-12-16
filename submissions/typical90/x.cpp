/**
*    author:  kaneshige
*    created: 13.09.2021 19:34:58
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;
#define rep(i,n) for(ll (i)=0;(i)<(n);++(i))

int main() {
    ll n,k; cin >> n >> k;
    ll A[n],B[n];
    rep(i,n){cin >> A[i];}
    rep(i,n){cin >> B[i];}
    ll dif = 0;
    rep(i,n){
        dif += abs(A[i]-B[i]);
    }
    if(dif<=k && (k-dif)%2==0){
        cout << "Yes" << endl;
    }else
    {
        cout << "No" << endl;
    }
}
