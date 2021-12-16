/**
*    author:  kaneshige
*    created: 01.09.2021 21:14:56
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;

int main() {
    long long n,a,b;
    cin >> n >> a >> b;
    long long ans = 0;
    ans += n/(a+b)*a;
    ans += min(n%(a+b),a);
    cout << ans << endl;
}
