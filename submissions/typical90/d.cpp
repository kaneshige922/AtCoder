/**
*    author:  kaneshige
*    created: 07.09.2021 23:53:45
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;
#define rep(i,n) for(ll (i)=0;(i)<(n);++(i))

int main() {
    int h,w;
    cin >> h >> w;
    int a[h][w];
    rep(i,h){
        rep(j,w){
            cin >> a[i][j];
        }
    }
    vector<int> tate(w,0);
    vector<int> yoko(h,0);
    rep(i,h){
        rep(j,w){
            tate[j] += a[i][j];
            yoko[i] += a[i][j];
        }
    }
    rep(i,h){
        rep(j,w){
            cout << tate[j]+yoko[i]-a[i][j] << " ";
        }
        cout << endl;
    }
}
