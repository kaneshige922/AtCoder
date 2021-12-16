/**
*    author:  kaneshige
*    created: 09.09.2021 10:39:01
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>
#include <math.h>

using namespace std;
using ll = long long;
#define rep(i,n) for(ll (i)=0;(i)<(n);++(i))
#define PI 3.141592653589

int main() {
    long double t; cin >> t;
    long double l,x,y; cin >> l >> x >> y;
    ll q; cin >> q;
    ll E[q];
    rep(i,q){
        cin >> E[i];
    }
    rep(i,q){
        long double xx = -l*sin(2*PI*E[i]/t)/2.0;
        long double yy = (1-cos(2*PI*E[i]/t))*l/2.0;
        long double ans = atan(yy/sqrt(pow(x,2)+pow(xx-y,2)))*180/PI;
        printf("%.12Lf\n", ans);
    }
}
