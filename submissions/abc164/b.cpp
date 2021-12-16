/**
*    author:  kaneshige
*    created: 31.08.2021 11:04:59
**/

#include <bits/stdc++.h>

using namespace std;

int main() {
    double a,b,c,d;
    cin >> a>> b>> c>> d;
    int x = ceil(c/b);
    int y = ceil(a/d);
    if (x <= y){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
}
