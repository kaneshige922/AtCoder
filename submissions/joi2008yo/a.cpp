/**
*    author:  kaneshige
*    created: 02.09.2021 20:42:11
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;

int main() {
    int n;
    cin >> n;
    int turi = 1000-n;
    const int m[6] = {500,100,50,10,5,1};
    int i = 0;
    int ans = 0;    
    while (turi != 0)
    {
        ans += turi/m[i];
        turi -= turi/m[i]*m[i];
        i ++;
    }
    cout << ans << endl;
}
