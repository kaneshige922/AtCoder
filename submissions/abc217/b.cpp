/**
*    author:  kaneshige
*    created: 10.09.2021 21:12:34
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;
#define rep(i,n) for(ll (i)=0;(i)<(n);++(i))

int main() {
    string s[3];
    cin >> s[0] >> s[1] >> s[2];
    if(!(count(s,s+3,"ABC"))){
        cout << "ABC" << endl;
    }
    if(!(count(s,s+3,"ARC")))    {
        cout << "ARC" << endl;
    }
    if(!(count(s,s+3,"AHC"))){
        cout << "AHC" << endl;
    }
    if(!(count(s,s+3,"AGC"))){
        cout << "AGC" << endl;
    }
}
