/**
*    author:  kaneshige
*    created: 31.08.2021 01:56:42
**/

#include <bits/stdc++.h>

using namespace std;

int main() {
    string s,t;
    cin >> s >> t;
    if (s == t.substr(0,s.size())){
        cout << "Yes\n" ;
    }else
    {
        cout << "No\n";
    }    
}
