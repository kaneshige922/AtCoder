/**
*    author:  kaneshige
*    created: 31.08.2021 02:48:31
**/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int k,a,b;
    cin >> k >> a >> b;
    int c,d;
    c =  a % k;
    d = b % k;
    if (c == 0 or c > d  or (b-a) >= k){
        cout << "OK" << endl;
    }else{
        cout << "NG" << endl;
    }
}
