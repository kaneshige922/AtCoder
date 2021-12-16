/**
*    author:  kaneshige
*    created: 01.09.2021 18:03:21
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;

int main() {
    string S;
    cin >> S;
    string S2 = S;
    reverse(S2.begin(),S2.end());
    int n = S.size();
    if (S != S2){
        cout << "No" << endl;
    }else{
        string sb = S.substr(0,(n-1)/2);
        string sb2 = sb;
        reverse(sb2.begin(),sb2.end());
        if (sb != sb2 ){
            cout << "No" << endl;
        }else{
            string sa = S.substr((n+3)/2-1);
            string sa2 = sa;
            reverse(sa2.begin(),sa2.end());
            if (sa != sa2){
                cout << "No" << endl;
            }else{
                cout << "Yes" << endl;
            }
        }
    }
}
