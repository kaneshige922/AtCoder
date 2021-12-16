/**
*    author:  kaneshige
*    created: 08.09.2021 00:09:10
**/

#include <bits/stdc++.h>
#include <algorithm>
#include <functional>

using namespace std;
using ll = long long;
#define rep(i,n) for(ll (i)=0;(i)<(n);++(i))

int main() {
    int n; cin >> n;
    vector<ll> A;
    rep(i,n){
        ll a; cin >> a;
        A.push_back(a);
    }
    sort(A.begin(),A.end());
    int q; cin >> q;
    ll b[q];
    rep(i,q){cin >> b[i];}
    rep(i,q){
        int left = 0;
        int right = n;
        int mid = n/2;
        while (right-left>1){
            if(A[mid]>b[i]){
                right = mid;
            }else{
                left = mid;
            }
            mid = (left+right)/2;
        }
        //cout << abs(b[i]-A[left]) << " " << abs(b[i]-A[right])<< " ";
        cout<< min(abs(b[i]-A[left]),abs(b[i]-A[right])) << endl;
    }
}
