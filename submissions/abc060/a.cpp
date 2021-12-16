/**
*    author:  kaneshige
*    created: 10.09.2021 21:23:13
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;
#define rep(i,n) for(ll (i)=0;(i)<(n);++(i))

int main() {
    string a,b,c;
    cin >> a >> b >> c;
    if(a[a.size()-1]==b[0] && b[b.size()-1]==c[0]){
        cout << "YES" <<endl;
    }else{
        cout << "NO"<< endl;
    }
}
