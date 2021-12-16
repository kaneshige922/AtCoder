/**
*    author:  kaneshige
*    created: 13.09.2021 21:13:45
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;
#define rep(i,n) for(ll (i)=0;(i)<(n);++(i))

int main() {
    ll w,h,n; cin >> w >> h >> n;
    ll xmi=0;ll xma=w;
    ll ymi=0;ll yma=h;
    rep(i,n){
        ll x,y,a;
        cin >> x >> y >> a;
        if(a==1){
            xmi= max(xmi,x);
        }else if(a==2){
            xma= min(xma,x);
        }else if(a==3){
            ymi= max(ymi,y);
        }else{
            yma= min(yma,y);
        }
    }
    if(xma-xmi<=0 || yma-ymi<=0){
        cout << 0 << endl;
    }else{
        cout << (xma-xmi)*(yma-ymi) << endl;
    }
}
