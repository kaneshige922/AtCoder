/**
*    author:  kaneshige
*    created: 02.09.2021 01:14:14
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;

int main() {
    int n,r;
    cin >> n >> r;
    int ans = r + 100*(max(0,10-n));
    cout << ans << endl;
}
