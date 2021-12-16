/**
*    author:  kaneshige
*    created: 14.09.2021 00:14:55
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;
#define rep(i,n) for(ll (i)=0;(i)<(n);++(i))

int main() {
    ll n; cin >> n;
    vector<vector<ll>> path(n);
    rep(i,n-1){
        ll a,b; cin >> a >> b;
        path[a-1].push_back(b-1);
        path[b-1].push_back(a-1);
    }
    queue<ll> que;
    unordered_set<ll> v;
    bool ans[n];
    rep(c,n){
        if(path[c].size() == 1){
            ans[c] = 1;
            que.push(c); v.insert(c);
            while (!que.empty())
            {
                ll h = que.front(); que.pop();
                for(auto i : path[h]){
                    if(!v.count(i)){
                        ans[i] = !(ans[h]);
                        v.insert(i);
                        que.push(i);
                    }
                }
            }
            break;
        }
    }

    ll cnt = 0;
    vector<ll> x,y;
    rep(i,n){
        if(ans[i]){
            x.push_back(i);
        }else{
            y.push_back(i);
        }
    }
    if(x.size()>=y.size()){
        rep(i,n/2){
            cout << x[i]+1 << " ";
        }
    }else{
        rep(i,n/2){
            cout << y[i]+1 << " ";
        }
    }
    cout << endl;
}
