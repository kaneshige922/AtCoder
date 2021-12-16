/**
*    author:  kaneshige
*    created: 02.09.2021 01:21:06
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;

int main() {
    int n,k;
    int cnt = 1;
    cin >> n >> k;
    int a = k;
    while (n >= a){
        a *= k;
        cnt ++;
    }
    cout << cnt << endl;
}
