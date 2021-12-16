/**
*    author:  kaneshige
*    created: 31.08.2021 11:24:14
**/

#include <bits/stdc++.h>

using namespace std;

int main() {
    int n,m;
    cin >> n >> m;
    int ans = 0;
    for(int i = 0 ; i < m; i++){
        int a;
        cin >> a;
        ans += a;
    }
    if (ans > n){
        cout << -1 << endl;
    }else{
        cout << n - ans << endl;
    }
}
