/**
*    author:  kaneshige
*    created: 02.09.2021 01:33:13
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;

int main() {
    int a,b,c;
    cin >> a >> b>> c;
    if ((a==b&&b!=c)||(b==c&&c!=a)||(c==a&&a!=b)){
        cout <<"Yes"<<endl;
    }else{
        cout <<"No" << endl;
    }
}
