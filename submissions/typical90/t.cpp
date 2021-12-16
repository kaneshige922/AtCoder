/**
*    author:  kaneshige
*    created: 13.09.2021 18:46:47
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;
#define rep(i,n) for(ll (i)=0;(i)<(n);++(i))

int main() {
    ll a,b,c; 
    cin >> a >> b >> c;
    ll cc = 1;
    rep(i,b){
        cc = cc*c;
    }
    if(a<cc){
        cout << "Yes" << endl;
    }else
    {
        cout << "No" << endl;
    }
    
}
