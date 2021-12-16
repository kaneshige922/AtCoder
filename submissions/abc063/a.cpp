/**
*    author:  kaneshige
*    created: 07.09.2021 21:50:35
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;
#define rep(i,n) for(ll (i)=0;(i)<(n);++(i))

int main() {
    int n; cin >> n;
    vector<int> s(n);
    rep(i,n){cin >> s[i];}
    sort(s.begin(),s.end());
    int ans = accumulate(s.begin(),s.end(),0);
    int i = 0;
    while ((ans%10 == 0) && (i < n))
    {
        if(s[i]%10 != 0){
            ans -= s[i];
        }
        i++;
    }
    if(ans%10 == 0){
        cout << 0 << endl;
        exit(0);
    }
    cout << ans << endl;
}
