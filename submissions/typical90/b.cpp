/**
*    author:  kaneshige
*    created: 07.09.2021 18:06:48
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;
#define rep(i,n) for(ll (i)=0;(i)<(n);++(i))

int main() {
    int n;
    cin >> n;
    if(n%2 != 0){
        cout << endl;
        exit(0);
    }
    string s;
    rep(i,n/2) s += "(";
    rep(i,n/2) s += ")";
    for(ll bit=0;bit<(1<<n);bit++){
        string s;
        ll cnt = 0;
        bool t = true;
        for(int i=0;i<n;i++){
            if(bit & (1<<i)){
                s = ")" + s;
                cnt += 1;
            }else{
                s = "(" + s;
                cnt += -1;
            }
            if(cnt<0){
                t = false;
            }
        }
        if(t && cnt == 0){
            cout << s << endl;
        }
    }
}
