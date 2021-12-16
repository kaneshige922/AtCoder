/**
*    author:  kaneshige
*    created: 07.09.2021 21:05:29
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;
#define rep(i,n) for(ll (i)=0;(i)<(n);++(i))

int main() {
    int n; cin >> n;
    vector<tuple<int,double,double>> tlr;
    rep(i,n){
        int t; double l,r;
        cin >> t >> l >> r;
        tlr.push_back(tuple<int,double,double>(t,l,r));
    }

    int ans = 0;

    for(int i=0;i<n-1;i++){
        double si,sj,ti,tj;
        int tx = get<0>(tlr[i]);
        double lx = get<1>(tlr[i]);
        double rx = get<2>(tlr[i]);
        if(!(tx == 1 || tx == 2)){
            lx += 0.5;
        }
        if(!(tx == 1 || tx == 3)){
            rx -= 0.5;
        } 
        for(int j=i+1;j<n;j++){
            int t = get<0>(tlr[j]);
            double l = get<1>(tlr[j]);
            double r = get<2>(tlr[j]);
            if(!(t == 1 || t == 2)){
                l += 0.5;
            }
            if(!(t == 1 || t == 3)){
                r -= 0.5;
            }
            if(!(rx < l || r < lx)){
                ans ++;
            }
        }
    }
    cout << ans << endl;
}
