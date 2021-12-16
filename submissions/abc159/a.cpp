/**
*    author:  kaneshige
*    created: 01.09.2021 17:48:33
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;

int main() {
    int n,m;
    cin >> n >> m;
    int ans = n*(n-1)/2 + m*(m-1)/2;
    cout << ans << endl;
}
