/**
*    author:  kaneshige
*    created: 05.09.2021 01:49:44
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;

int main() {
    ll n;cin>>n;
    deque<ll>a;
    for(int i=0;i<3*n;i++){
        int ai; cin>>ai; a.push_back(ai);
    }
    priority_queue<ll,vector<ll>,greater<ll>> quered;
    priority_queue<ll,vector<ll>> queblue;
    ll suma=0;ll sumb=0;
    for(int i=0;i<n;i++){
        ll toa= a.front();
        a.pop_front();
        ll tob = a.back();
        a.pop_back();
        suma+= toa; sumb+= tob;
        quered.push(toa);
        queblue.push(tob);
    }
    ll ans = -pow(10,14);
    
    vector<vector<ll>> sasb(n+1,vector<ll>(2,0ll));
    sasb[0][0] = suma;
    sasb[n][1] = sumb;
    priority_queue<ll,vector<ll>,greater<ll>> qr = quered;
    priority_queue<ll,vector<ll>> qb = queblue;
    deque<ll> b = a;
    deque<ll> c = a;
    ll sa = suma; ll sb =sumb;
    for(int i = 1;i<=n;i++){
        ll koho = b.front();
        b.pop_front();
        if(koho > qr.top()){
            ll bye = qr.top();
            qr.pop();
            qr.push(koho);
            sa += koho - bye;
        }
        koho = c.back();
        c.pop_back();
        if(koho < qb.top()){
            ll bye = qb.top();
            qb.pop();
            qb.push(koho);
            sb += koho - bye;
        }
        sasb[i][0] = sa;
        sasb[n-i][1] = sb;
    }
    for(int i=0;i<=n;i++){
        ans = max(ans,sasb[i][0]-sasb[i][1]);
    }
    cout << ans << endl;
}
