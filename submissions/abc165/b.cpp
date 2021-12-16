/**
*    author:  kaneshige
*    created: 31.08.2021 02:56:47
**/

#include <bits/stdc++.h>

using namespace std;

int main() {
    long long n = 100;
    long long b = 100;
    int cnt = 0;
    long long x;
    cin >> x;
    while (n < x)
    {
        n += n/b;
        cnt ++;
    }
    cout << cnt << endl;
}
