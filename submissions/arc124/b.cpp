/**
*    author:  kaneshige
*    created: 12.09.2021 23:00:40
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;
#define rep(i,n) for(ll (i)=0;(i)<(n);++(i))

int main() {
    ll n; cin >> n;
    vector<ll> A,B;
    rep(i,n){ll a; cin >> a;A.push_back(a);}
    rep(i,n){ll a; cin >> a;B.push_back(a);}
    sort(B.begin(),B.end());

    vector<ll> ans;
    unordered_set<ll> sans;

    rep(i,n){
        ll x = A[0]^B[i];
        vector<ll> C;
        rep(j,n){
            C.push_back(A[j]^x);
        }
        sort(C.begin(),C.end());
        if(B==C){
            if(!(sans.count(x))){
                ans.push_back(x);   
            }
            sans.insert(x);
        }
    }
    sort(ans.begin(),ans.end());
    cout << ans.size() << endl;
    rep(i,ans.size()){
        cout << ans[i] << endl;
    }
}
