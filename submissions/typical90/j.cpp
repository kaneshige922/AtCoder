/**
*    author:  kaneshige
*    created: 08.09.2021 15:35:31
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;
#define rep(i,n) for(ll (i)=0;(i)<(n);++(i))

int main() {
    int n; cin >> n;
    int A[n+1];
    int B[n+1];
    A[0] = B[0] = 0;
    rep(i,n){
        int c,a; cin >> c >> a;
        if(c == 1){
            A[i+1] = A[i] + a;
            B[i+1] = B[i];
        }else
        {
            A[i+1] = A[i];
            B[i+1] = B[i] + a;
        }
        
    }
    int q; cin >> q;
    vector<int> ans;
    rep(i,q){
        int l,r; cin >> l >> r;
        cout << A[r] - A[l-1] << " " << B[r] - B[l-1] << endl;
    }
}
