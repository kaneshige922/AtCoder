/**
*    author:  kaneshige
*    created: 31.08.2021 00:33:09
**/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int k;
    string s;
    cin >> k >> s;
    if (k >= s.length()){
        cout << s << endl;
    }else{
        cout << s.substr(0,k) << "..." << endl;
    }
}
