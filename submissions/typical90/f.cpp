/**
*    author:  kaneshige
*    created: 15.09.2021 22:25:43
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;
#define rep(i,n) for(ll (i)=0;(i)<(n);++(i))

int main() {
    ll n; cin >> n;
    vector<vector<ll>> A(n);
    rep(i,n){
        rep(j,n){
            ll a; cin >> a;
            A[i].push_back(a);
        }
    }
    ll m; cin >> m;
    vector<unordered_set<ll>>  XY(n);
    rep(i,m){
        ll x,y; cin >> x >> y;
        XY[x-1].insert(y-1);
        XY[y-1].insert(x-1);
    }
    vector<ll> P(n); rep(i,n){P[i]=i;}
    ll ans = -1;
    do
    {
        ll cnt = 0;
        bool T = true;
        rep(i,n){
            if(i!=n-1){
                if(XY[P[i+1]].count(P[i])){
                    T =false; break;
                }else{
                    cnt += A[P[i]][i];
                }
            }else{
                cnt += A[P[i]][i];
            }
        }
        if(T){
            if(ans!=-1){ans = min(ans,cnt);}
            else{ans = cnt;}
        }
    } while (next_permutation(P.begin(),P.end()));
    cout << ans << endl;
}
